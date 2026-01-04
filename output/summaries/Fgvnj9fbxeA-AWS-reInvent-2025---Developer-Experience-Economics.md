# AWS re:Invent 2025 - Developer Experience Economics: Moving Past Productivity Metrics (DVT207)

**URL**: [https://www.youtube.com/watch?v=Fgvnj9fbxeA](https://www.youtube.com/watch?v=Fgvnj9fbxeA)
**Channel**: AWS Events
**Difficulty**: advanced
**Platform Eng Relevance**: 9/10

## Tags
`developer-experience` `metrics` `ai-tooling` `platform-engineering` `devops` `productivity`

## Key Insights

- Amazon's 'Cost to Serve Software' framework measures developer experience ROI by dividing total development costs by software delivery units (deployments, PRs, or commits), achieving 15.9% business value improvement year-over-year.
- Focus on team-level metrics rather than individual developer productivity since software development is fundamentally a team endeavor where individual velocity returns to team mean.
- AI-native development requires two-loop SDLC (plan-develop-test and release-monitor-operate) with AI agents handling undifferentiated work like code transformations, maintenance, and incident response.
- Tension metrics like 'human-actioned high severity tickets per normalized deployment' balance velocity improvements with quality to prevent breaking things while moving fast.
- Platform teams should eliminate, automate, and assist across the full SDLC rather than just focusing on coding productivity metrics like lines of code or time-based measurements.

## Summary

## Overview
Amazon's software builder experience team presents their Cost to Serve Software framework for measuring developer experience economics beyond traditional productivity metrics. The session covers how Amazon quantifies AI tooling impacts and drives business value through holistic developer experience improvements.

## Technical Details
- Cost to Serve Software formula: Total Development Costs / Software Delivery Units (deployments, PRs, commits)
- Amazon achieved 18.3% increase in weekly production deployments per builder and 30% reduction in manual interventions
- AI agents integrated across SDLC using Amazon Bedrock, Q Developer, and Model Context Protocol (MCP)
- Tension metrics track quality indicators (high severity tickets) alongside velocity improvements
- Code transformation agents handle migrations (JDK 8/11 to 17+) without developer intervention
- Two-loop SDLC architecture separating planning/development from release/operations

## Architecture/Patterns
- Unified platform organization (ASBX) consolidating tool-based teams into outcome-focused approach
- Core/Common/Custom knowledge model for scaling AI context across enterprise systems
- Synchronous AI assistants embedded in developer tools (IDE, CLI) plus autonomous workflow agents
- Security and safety mechanisms protecting agent-driven release and operational workflows

## Practical Takeaways
- Start with team-chosen software delivery units and evolve metrics over time based on your deployment patterns
- Implement tension metrics to balance velocity gains with quality indicators in real-time
- Focus platform investments on eliminating, automating, and assisting rather than just measuring individual productivity

## AWS/Cloud Services Mentioned
Amazon Bedrock, Amazon Q Developer, Amazon Q CLI, Amazon Q Business

## Keywords
Cost to Serve Software, ASBX, Amazon Q Developer, Kira, Amazon Bedrock, MCP, developer productivity, SDLC, AI agents, code transformation

---
*Generated on 2026-01-04 04:05 UTC*
