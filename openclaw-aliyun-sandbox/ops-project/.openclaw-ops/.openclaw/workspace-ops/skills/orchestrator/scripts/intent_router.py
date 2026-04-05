#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orchestrator 意图路由器 v2 (Intent Router + Scenario Dispatch)
解析用户的自然语言指令，匹配最佳场景模板，构建任务蓝图。

使用方法: python intent_router.py "用户的原始指令"

v2 升级: 现在基于 scenario_registry 进行场景级调度，
不再仅做简单关键词匹配。
"""

import json
import sys
import uuid
from datetime import datetime, timezone
from scenario_registry import SCENARIO_REGISTRY

# ============================================================
# 场景关键词映射 (Scenario Keywords)
# ============================================================
SCENARIO_KEYWORDS = {
    "marketing_campaign": [
        "营销", "推广", "活动", "品牌", "内容", "发布",
        "小红书", "抖音", "B站", "微博", "微信", "公众号",
        "TikTok", "Twitter", "Reddit", "Instagram", "YouTube",
        "KOL", "种草", "热搜", "campaign", "marketing",
        "social media", "content", "launch",
    ],
    "startup_mvp": [
        "MVP", "原型", "prototype", "创业", "startup",
        "前端", "后端", "开发", "deploy", "build",
        "React", "Next.js", "API", "数据库", "增长",
        "growth", "app", "应用", "产品",
    ],
    "paid_media_takeover": [
        "广告", "付费", "SEM", "PPC", "Google Ads",
        "竞价", "投放", "ROI", "CPA", "CPC",
        "转化", "追踪", "tracking", "审计", "优化",
        "搜索词", "否定关键词", "paid media", "ads",
    ],
    "enterprise_feature_dev": [
        "企业", "功能开发", "feature", "设计系统", "design system",
        "UI", "UX", "组件库", "A/B测试", "实验", "experiment",
        "QA", "质检", "项目管理", "任务清单", "规格说明",
        "Laravel", "Livewire", "FluxUI", "Three.js",
        "截图证据", "验收", "交付", "enterprise",
    ],
    "academic_site_optimization": [
        "学术", "academic", "acadai", "教育", "education",
        "课程", "论文", "research", "学习", "知识",
        "大学", "university", "学者", "scholar", "文献",
        "心理学", "历史", "人类学", "叙事", "地理",
        "SEO", "优化", "追踪", "用户体验", "站点",
    ],
}

# ============================================================
# 通用意图 (Fallback generic intents — used when no scenario matches)
# ============================================================
INTENT_KEYWORDS = {
    "media_crawl": [
        "爬取", "抓取", "采集", "crawl", "scrape", "xhs",
    ],
    "content_create": [
        "写文案", "撰写", "创作", "脚本", "文章", "copywriting",
    ],
    "video_generate": [
        "视频", "数字人", "TTS", "D-ID", "短视频", "video",
    ],
    "code_ops": [
        "部署", "代码", "debug", "review", "上线", "Docker",
    ],
    "doc_publish": [
        "飞书", "文档", "发布", "推送", "feishu", "publish",
    ],
    "research": [
        "搜索", "查找", "调研", "研究", "分析", "research",
    ],
}

AGENT_CAPABILITIES = {
    "media":   ["media_crawl", "research"],
    "creator": ["content_create", "video_generate"],
    "ops":     ["code_ops", "doc_publish", "video_generate"],
    "monitor": ["research"],
    "main":    ["content_create", "research", "code_ops"],
}


def match_scenario(user_input: str) -> str | None:
    """尝试匹配用户输入到预定义的场景模板。返回场景 ID 或 None。"""
    text = user_input.lower()
    scores = {}
    for scenario_id, keywords in SCENARIO_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score > 0:
            scores[scenario_id] = score

    if not scores:
        return None

    # 返回得分最高的场景
    return max(scores, key=scores.get)


def classify_intents(user_input: str) -> list[str]:
    """从用户输入中识别所有匹配的通用意图标签（用于无场景匹配时的降级）。"""
    text = user_input.lower()
    matched = []
    for intent, keywords in INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                matched.append(intent)
                break
    return matched if matched else ["research"]


def assign_agents(intents: list[str]) -> dict[str, list[str]]:
    """根据通用意图分配 Agent（降级模式）。"""
    assignments: dict[str, list[str]] = {}
    for intent in intents:
        best_agents = [
            agent for agent, caps in AGENT_CAPABILITIES.items()
            if intent in caps
        ]
        assignments[intent] = best_agents if best_agents else ["main"]
    return assignments


def build_task_blueprint(user_input: str) -> dict:
    """构建完整的任务蓝图 JSON。优先使用场景模板，否则降级为通用意图匹配。"""
    task_id = str(uuid.uuid4())[:8]

    # 优先尝试场景匹配
    scenario_id = match_scenario(user_input)

    if scenario_id:
        scenario = SCENARIO_REGISTRY[scenario_id]
        subtasks = []
        for i, member in enumerate(scenario["team"], 1):
            subtasks.append({
                "id": f"sub-{i}",
                "assignee": member["role"],
                "agent_skill": member["agent_skill"],
                "action": member["task"],
                "priority": member["priority"],
                "result": None,
                "status": "pending",
            })
        return {
            "taskId": task_id,
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "scenario": scenario_id,
            "scenarioName": scenario["name"],
            "intent": [scenario_id],
            "status": "pending",
            "teamSize": len(scenario["team"]),
            "executionOrder": scenario["execution_order"],
            "deliverables": scenario["deliverables"],
            "subtasks": subtasks,
            "finalOutput": None,
        }
    else:
        # 降级: 通用意图匹配
        intents = classify_intents(user_input)
        assignments = assign_agents(intents)
        subtasks = []
        for i, (intent, agents) in enumerate(assignments.items(), 1):
            subtasks.append({
                "id": f"sub-{i}",
                "assignee": agents[0],
                "action": intent,
                "params": {"raw_input": user_input},
                "result": None,
                "status": "pending",
            })
        return {
            "taskId": task_id,
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "scenario": None,
            "intent": intents,
            "status": "pending",
            "subtasks": subtasks,
            "finalOutput": None,
        }


def main():
    if len(sys.argv) < 2:
        print("用法: python intent_router.py \"你的指令\"")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    blueprint = build_task_blueprint(user_input)

    print(json.dumps(blueprint, ensure_ascii=False, indent=2))
    return blueprint


if __name__ == "__main__":
    main()
