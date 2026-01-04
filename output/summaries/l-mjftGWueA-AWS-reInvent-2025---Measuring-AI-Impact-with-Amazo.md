# AWS re:Invent 2025 - Measuring AI Impact with Amazon Q Developer and Jellyfish (DVT219)

[![Video Thumbnail](https://img.youtube.com/vi/l-mjftGWueA/maxresdefault.jpg)](https://www.youtube.com/watch?v=l-mjftGWueA)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `ai-ml` `developer-experience` `observability` `platform-engineering` `productivity`

## Key Insights

- AI impact measurement requires a three-phase approach: adoption metrics (who's using AI tools), productivity metrics (output improvements), and business outcome metrics (cost reduction, innovation velocity) - not just tool usage statistics.
- Implement Amazon's 'eliminate, automate, assist' framework for AI adoption: eliminate manual processes first, automate repetitive tasks, then use AI to assist with complex problem-solving rather than just turning on tools without strategy.
- Baseline your current development productivity metrics before AI rollout using frameworks like DORA or SPACE, then track trends over time rather than seeking a single productivity measure.
- Map AI usage to internal team and product taxonomies to identify which teams show high/low engagement, enabling targeted interventions and explaining variance to leadership rather than organization-wide mandates.
- Amazon's 'cost to serve software' framework (infrastructure + human costs / units delivered) provides a holistic way to measure AI impact including second-order effects like reduced onboarding time and increased skill flexibility.

## Summary

## Overview
AWS session covering measurement strategies for AI developer tools like Amazon Q and Codewhisperer, featuring perspectives from AWS, Jellyfish (productivity analytics platform), and Genesis (customer implementation). The talk provides frameworks for moving beyond tool adoption to measuring actual business impact from AI coding assistants.

## Technical Details
- Amazon Q Developer and Codewhisperer provide activity data mapping to SPACE framework's 'A' (Activity) but miss other productivity dimensions
- Integration between issue tracking systems (Jira, Linear), source control (GitHub, Bitbucket), and CI/CD pipelines required for comprehensive productivity measurement
- Amazon's cost-to-serve framework: (infrastructure costs + human/tool costs) / delivery units, showing 16% improvement across AWS development organization
- Jellyfish platform consumes Q metrics via AWS SSO integration, replacing custom PostgreSQL/QuickSight dashboards with automated enterprise reporting
- Context engineering and prompt precision more critical than raw tool access for AI effectiveness
- Second-order impacts include reduced onboarding time, increased skill flexibility, and enablement of projects that wouldn't exist without AI

## Architecture/Patterns
- Three-phase measurement journey: adoption → productivity → business outcomes, with leading and lagging indicators for each phase
- Eliminate-automate-assist pattern for AI implementation prioritization rather than ad-hoc tool deployment
- Unified metrics dashboard architecture combining AI usage data with team/product taxonomy for segmented analysis
- Baseline-and-trend approach rather than seeking single productivity metrics

## Practical Takeaways
- Start measuring current productivity with available tools before AI rollout to establish baseline trends
- Implement structured AI enablement programs with dedicated experimentation time rather than expecting organic adoption
- Use segmented data analysis by team, project type, and codebase age to identify AI effectiveness patterns and intervention opportunities

## AWS/Cloud Services Mentioned
Amazon Q Developer, AWS Codewhisperer, AWS SSO, AWS Lambda, QuickSight, GitHub, Jira

## Keywords
Amazon-Q-Developer, Codewhisperer, DORA-metrics, SPACE-framework, cost-to-serve, Jellyfish, developer-productivity, AI-impact-measurement, prompt-engineering, context-engineering

---
*Generated on 2026-01-04 04:06 UTC*
