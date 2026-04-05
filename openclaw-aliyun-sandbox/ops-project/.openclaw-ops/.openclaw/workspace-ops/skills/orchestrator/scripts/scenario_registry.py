#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
场景注册表 (Scenario Registry)
定义每个实战场景所需的 Agent 团队编制、执行顺序和交付标准。
Orchestrator 的 intent_router 通过查询本表来"按需组队"。
"""

# ============================================================
# 第一阶段 Batch 1: 营销活动启动 (Marketing Campaign Launch)
# ============================================================
MARKETING_CAMPAIGN = {
    "id": "marketing_campaign",
    "name": "营销活动启动",
    "description": "从内容策划到多平台发布到数据复盘的全链路营销战役",
    "team": [
        {
            "role": "内容创作者",
            "agent_skill": "agency-agents/converted/content-creator",
            "priority": 1,
            "task": "根据活动主题开发核心内容（文案/脚本/视觉稿）",
        },
        {
            "role": "小红书专家",
            "agent_skill": "agency-agents/converted/xiaohongshu-specialist",
            "priority": 2,
            "task": "将核心内容适配为小红书种草笔记，含标签和话题策略",
        },
        {
            "role": "抖音策略师",
            "agent_skill": "agency-agents/converted/douyin-strategist",
            "priority": 2,
            "task": "将核心内容改编为短视频脚本，规划投放节奏",
        },
        {
            "role": "B站策略师",
            "agent_skill": "agency-agents/converted/bilibili-content-strategist",
            "priority": 2,
            "task": "将核心内容改编为B站中长视频/专栏，适配弹幕文化",
        },
        {
            "role": "微博策略师",
            "agent_skill": "agency-agents/converted/weibo-strategist",
            "priority": 2,
            "task": "策划微博热搜话题，规划KOL矩阵分发",
        },
        {
            "role": "TikTok 策略师",
            "agent_skill": "agency-agents/converted/tiktok-strategist",
            "priority": 2,
            "task": "适配英文短视频内容，规划海外投放",
        },
        {
            "role": "Twitter 互动员",
            "agent_skill": "agency-agents/converted/twitter-engager",
            "priority": 2,
            "task": "适配推文内容，规划话题标签和互动策略",
        },
        {
            "role": "Reddit 社区建设者",
            "agent_skill": "agency-agents/converted/reddit-community-builder",
            "priority": 2,
            "task": "在相关 Subreddit 发起讨论，建设品牌社区",
        },
        {
            "role": "Instagram 策展人",
            "agent_skill": "agency-agents/converted/instagram-curator",
            "priority": 2,
            "task": "策划视觉内容，九宫格排版，Stories 和 Reels 规划",
        },
        {
            "role": "微信公众号运营",
            "agent_skill": "agency-agents/converted/wechat-official-account-manager",
            "priority": 2,
            "task": "将核心内容改编为公众号深度文章，规划粉丝互动",
        },
        {
            "role": "社交媒体总策略师",
            "agent_skill": "agency-agents/converted/social-media-strategist",
            "priority": 1,
            "task": "统筹多平台发布节奏，确保品牌调性一致",
        },
        {
            "role": "数据分析报告员",
            "agent_skill": "agency-agents/converted/analytics-reporter",
            "priority": 3,
            "task": "追踪所有平台的互动数据，生成活动效果报告",
        },
    ],
    "execution_order": ["并行: 内容创作 → 并行: 各平台适配 → 串行: 数据分析复盘"],
    "deliverables": ["各平台内容稿件", "投放排期表", "活动效果报告"],
}

# ============================================================
# 第一阶段 Batch 2: 打造初创公司 MVP (Startup MVP)
# ============================================================
STARTUP_MVP = {
    "id": "startup_mvp",
    "name": "打造初创公司 MVP",
    "description": "从前端到后端到增长策略的全栈快速原型开发",
    "team": [
        {
            "role": "前端开发者",
            "agent_skill": "agency-agents/converted/frontend-developer",
            "priority": 1,
            "task": "构建 React/Next.js 前端应用，实现核心 UI 组件",
        },
        {
            "role": "后端架构师",
            "agent_skill": "agency-agents/converted/software-architect",
            "priority": 1,
            "task": "设计 API 架构和数据库 Schema，搭建服务端骨架",
        },
        {
            "role": "增长黑客",
            "agent_skill": "agency-agents/converted/growth-hacker",
            "priority": 2,
            "task": "制定用户获取计划，设计增长漏斗和病毒传播机制",
        },
        {
            "role": "快速原型机",
            "agent_skill": "agency-agents/converted/rapid-prototyper",
            "priority": 1,
            "task": "快速迭代 UI/UX 原型，验证核心假设",
        },
        {
            "role": "现实检查器",
            "agent_skill": "agency-agents/converted/reality-checker",
            "priority": 3,
            "task": "上线前质量审查，检查安全漏洞、性能瓶颈和UX问题",
        },
    ],
    "execution_order": ["并行: 前端+后端+原型 → 串行: 增长策略 → 串行: 质量检查"],
    "deliverables": ["可运行的 MVP 应用", "API 文档", "增长策略报告", "QA 检查清单"],
}

# ============================================================
# 第一阶段 Batch 3: 付费媒体账号接管 (Paid Media Takeover)
# ============================================================
PAID_MEDIA_TAKEOVER = {
    "id": "paid_media_takeover",
    "name": "付费媒体账号接管",
    "description": "全面审计、优化并重建付费广告账户架构",
    "team": [
        {
            "role": "付费媒体审计员",
            "agent_skill": "agency-agents/converted/paid-media-auditor",
            "priority": 1,
            "task": "全面评估广告账户现状，识别浪费和机会点",
        },
        {
            "role": "追踪与测量专家",
            "agent_skill": "agency-agents/converted/tracking-measurement-specialist",
            "priority": 1,
            "task": "验证转化跟踪准确性，修复数据断链",
        },
        {
            "role": "PPC 广告策略师",
            "agent_skill": "agency-agents/converted/ppc-campaign-strategist",
            "priority": 2,
            "task": "重新设计账户架构，优化出价策略和广告组结构",
        },
        {
            "role": "搜索查询分析师",
            "agent_skill": "agency-agents/converted/search-query-analyst",
            "priority": 2,
            "task": "清理搜索词中浪费的支出，建立否定关键词体系",
        },
        {
            "role": "广告创意策略师",
            "agent_skill": "agency-agents/converted/paid-social-strategist",
            "priority": 2,
            "task": "刷新所有广告文案和附加信息(扩展)",
        },
        {
            "role": "分析报告员",
            "agent_skill": "agency-agents/converted/analytics-reporter",
            "priority": 3,
            "task": "构建报表仪表盘，设定 KPI 追踪体系",
        },
    ],
    "execution_order": ["并行: 审计+追踪验证 → 串行: 架构重建+搜索词清理 → 串行: 创意刷新 → 串行: 报告仪表盘"],
    "deliverables": ["账户审计报告", "转化追踪修复文档", "新账户架构方案", "否定关键词清单", "KPI 仪表盘"],
}

# ============================================================
# 第二阶段: 企业功能级开发 (Enterprise Feature Development)
# ============================================================
ENTERPRISE_FEATURE_DEV = {
    "id": "enterprise_feature_dev",
    "name": "企业功能级开发",
    "description": "从需求拆解到UI设计到开发实现到实验验证到QA把关的全链路企业级功能交付",
    "team": [
        {
            "role": "高级项目经理",
            "agent_skill": "agency-agents/converted/senior-project-manager",
            "priority": 1,
            "task": "将需求规格拆解为可执行的开发任务清单，设定验收标准",
        },
        {
            "role": "UI 设计师",
            "agent_skill": "agency-agents/converted/ui-designer",
            "priority": 1,
            "task": "创建设计系统、组件库和交互规格说明书",
        },
        {
            "role": "高级全栈开发者",
            "agent_skill": "agency-agents/converted/senior-developer",
            "priority": 2,
            "task": "按照设计稿和任务清单实现功能，确保像素级精准和60fps动画",
        },
        {
            "role": "实验追踪器",
            "agent_skill": "agency-agents/converted/experiment-tracker",
            "priority": 2,
            "task": "设计 A/B 测试方案，追踪功能上线后的关键指标变化",
        },
        {
            "role": "证据收集员",
            "agent_skill": "agency-agents/converted/evidence-collector",
            "priority": 3,
            "task": "截图驱动的 QA 审查，对比规格说明与实际实现",
        },
        {
            "role": "现实检查器",
            "agent_skill": "agency-agents/converted/reality-checker",
            "priority": 3,
            "task": "最终质量关卡，默认 NEEDS WORK，铁证如山才放行",
        },
    ],
    "execution_order": ["并行: PM任务拆解+UI设计 → 串行: 开发实现 → 并行: 实验设计+QA → 串行: 终审放行"],
    "deliverables": ["开发任务清单", "设计系统文档", "功能实现代码", "A/B测试方案", "QA证据报告", "终审认证"],
}

# ============================================================
# 学术站点优化: acadai.cn 追踪·升级·优化 (Academic Site Optimization)
# ============================================================
ACADEMIC_SITE_OPTIMIZATION = {
    "id": "academic_site_optimization",
    "name": "学术AI站点追踪升级优化",
    "description": "针对已上线学术AI产品(acadai.cn)的全链路追踪、内容质量提升、SEO优化和用户体验改进",
    "team": [
        {
            "role": "心理学家",
            "agent_skill": "agency-agents/converted/academic-psychologist",
            "priority": 1,
            "task": "分析用户行为模式，基于认知心理学优化学习路径和交互设计",
        },
        {
            "role": "叙事学家",
            "agent_skill": "agency-agents/converted/academic-narratologist",
            "priority": 1,
            "task": "优化学术内容的叙事结构，确保知识传递的逻辑性和吸引力",
        },
        {
            "role": "历史学家",
            "agent_skill": "agency-agents/converted/academic-historian",
            "priority": 2,
            "task": "审查学术内容的历史准确性，提供跨文化的学术视角补充",
        },
        {
            "role": "人类学家",
            "agent_skill": "agency-agents/converted/academic-anthropologist",
            "priority": 2,
            "task": "分析目标用户群体的文化背景，确保内容的跨文化适配性",
        },
        {
            "role": "地理学家",
            "agent_skill": "agency-agents/converted/academic-geographer",
            "priority": 2,
            "task": "提供地理与空间分析相关的学术内容支持",
        },
        {
            "role": "SEO 专家",
            "agent_skill": "agency-agents/converted/seo-specialist",
            "priority": 1,
            "task": "优化 acadai.cn 的搜索引擎排名，学术关键词研究和技术SEO审计",
        },
        {
            "role": "前端开发者",
            "agent_skill": "agency-agents/converted/frontend-developer",
            "priority": 2,
            "task": "根据用户分析结果优化前端体验，提升Core Web Vitals和可访问性",
        },
        {
            "role": "追踪与测量专家",
            "agent_skill": "agency-agents/converted/tracking-measurement-specialist",
            "priority": 1,
            "task": "部署全链路用户行为追踪，验证转化漏斗数据准确性",
        },
        {
            "role": "数据分析报告员",
            "agent_skill": "agency-agents/converted/analytics-reporter",
            "priority": 3,
            "task": "聚合所有数据源，生成 acadai.cn 整体健康度报告和优化建议",
        },
        {
            "role": "证据收集员",
            "agent_skill": "agency-agents/converted/evidence-collector",
            "priority": 3,
            "task": "截图对比优化前后的变化，提供视觉证据支撑所有改进声明",
        },
    ],
    "execution_order": [
        "并行: 心理学用户分析+SEO审计+追踪部署",
        "→ 并行: 学术内容优化(叙事+历史+人类学+地理)",
        "→ 串行: 前端体验优化",
        "→ 串行: 数据分析报告+QA证据收集",
    ],
    "deliverables": [
        "用户行为分析报告",
        "SEO优化方案",
        "追踪体系部署文档",
        "学术内容质量审查报告",
        "前端优化清单",
        "数据分析仪表盘",
        "优化前后对比证据",
    ],
}

# ============================================================
# 全局注册表 — Orchestrator 查询入口
# ============================================================
SCENARIO_REGISTRY = {
    "marketing_campaign": MARKETING_CAMPAIGN,
    "startup_mvp": STARTUP_MVP,
    "paid_media_takeover": PAID_MEDIA_TAKEOVER,
    "enterprise_feature_dev": ENTERPRISE_FEATURE_DEV,
    "academic_site_optimization": ACADEMIC_SITE_OPTIMIZATION,
}


def get_scenario(scenario_id: str) -> dict | None:
    """根据场景 ID 检索团队编制。"""
    return SCENARIO_REGISTRY.get(scenario_id)


def list_scenarios() -> list[str]:
    """列出所有可用场景。"""
    return list(SCENARIO_REGISTRY.keys())


if __name__ == "__main__":
    import json
    for sid, scenario in SCENARIO_REGISTRY.items():
        print(f"\n{'='*60}")
        print(f"场景: {scenario['name']} ({sid})")
        print(f"说明: {scenario['description']}")
        print(f"团队规模: {len(scenario['team'])} 人")
        for member in scenario["team"]:
            print(f"  P{member['priority']} | {member['role']}: {member['task'][:50]}...")
