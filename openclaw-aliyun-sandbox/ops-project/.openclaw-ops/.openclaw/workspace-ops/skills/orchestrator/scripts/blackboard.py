#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orchestrator 黑板管理器 (Blackboard Manager)
管理跨 Agent 共享任务状态的中央 Blackboard 文件系统。

命令:
  python blackboard.py create  <task_json>   — 从 JSON 创建新任务黑板
  python blackboard.py update  <task_id> <subtask_id> <status> [result]  — 更新子任务状态
  python blackboard.py read    <task_id>     — 读取任务黑板
  python blackboard.py cleanup <task_id>     — 销毁临时黑板（生命周期终点）
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

BLACKBOARD_DIR = Path(__file__).parent.parent.parent / "orchestrator" / "blackboard"
REPORTS_DIR = Path(__file__).parent.parent.parent / "orchestrator" / "reports"


def ensure_dirs():
    BLACKBOARD_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def create(task_json_str: str) -> str:
    """创建新任务黑板文件。"""
    ensure_dirs()
    task = json.loads(task_json_str)
    task_id = task["taskId"]
    filepath = BLACKBOARD_DIR / f"{task_id}.json"
    filepath.write_text(json.dumps(task, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[Blackboard] Created: {filepath}")
    return str(filepath)


def read(task_id: str) -> dict:
    """读取任务黑板。"""
    filepath = BLACKBOARD_DIR / f"{task_id}.json"
    if not filepath.exists():
        print(f"[Blackboard] ERROR: Task {task_id} not found")
        sys.exit(1)
    data = json.loads(filepath.read_text(encoding="utf-8"))
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return data


def update(task_id: str, subtask_id: str, status: str, result: str = None):
    """更新子任务状态。"""
    filepath = BLACKBOARD_DIR / f"{task_id}.json"
    if not filepath.exists():
        print(f"[Blackboard] ERROR: Task {task_id} not found")
        sys.exit(1)

    task = json.loads(filepath.read_text(encoding="utf-8"))
    updated = False
    for sub in task.get("subtasks", []):
        if sub["id"] == subtask_id:
            sub["status"] = status
            if result:
                sub["result"] = result
            updated = True
            break

    if not updated:
        print(f"[Blackboard] ERROR: Subtask {subtask_id} not found in {task_id}")
        sys.exit(1)

    # 自动判断整体任务状态
    all_statuses = [s["status"] for s in task["subtasks"]]
    if all(s == "completed" for s in all_statuses):
        task["status"] = "completed"
    elif any(s == "failed" for s in all_statuses):
        task["status"] = "partial_failure"
    else:
        task["status"] = "in_progress"

    filepath.write_text(json.dumps(task, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[Blackboard] Updated {subtask_id} -> {status}")

    # 如果全部完成，自动生成报告
    if task["status"] == "completed":
        _generate_report(task)


def cleanup(task_id: str):
    """销毁临时黑板（任务生命周期终点）。"""
    filepath = BLACKBOARD_DIR / f"{task_id}.json"
    if filepath.exists():
        filepath.unlink()
        print(f"[Blackboard] Destroyed: {task_id}")
    else:
        print(f"[Blackboard] Nothing to clean: {task_id}")


def _generate_report(task: dict):
    """自动生成最终报告。"""
    ensure_dirs()
    task_id = task["taskId"]
    report_path = REPORTS_DIR / f"{task_id}.md"

    lines = [
        f"# 任务完成报告: {task_id}",
        f"",
        f"- **创建时间**: {task.get('createdAt', 'N/A')}",
        f"- **完成时间**: {datetime.now(timezone.utc).isoformat()}",
        f"- **识别意图**: {', '.join(task.get('intent', []))}",
        f"- **状态**: ✅ 全部完成",
        f"",
        f"## 子任务详情",
        f"",
    ]

    for sub in task.get("subtasks", []):
        lines.append(f"### {sub['id']} — {sub['action']}")
        lines.append(f"- **执行者**: `{sub['assignee']}`")
        lines.append(f"- **状态**: {sub['status']}")
        lines.append(f"- **结果**: {sub.get('result', '无')}")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[Blackboard] Report generated: {report_path}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "create" and len(sys.argv) >= 3:
        create(sys.argv[2])
    elif cmd == "read" and len(sys.argv) >= 3:
        read(sys.argv[2])
    elif cmd == "update" and len(sys.argv) >= 5:
        result = sys.argv[5] if len(sys.argv) > 5 else None
        update(sys.argv[2], sys.argv[3], sys.argv[4], result)
    elif cmd == "cleanup" and len(sys.argv) >= 3:
        cleanup(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
