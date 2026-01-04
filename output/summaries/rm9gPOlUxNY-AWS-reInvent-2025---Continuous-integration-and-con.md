# AWS re:Invent 2025 - Continuous integration and continuous delivery (CI/CD) for AWS (DVT202)

**URL**: [https://www.youtube.com/watch?v=rm9gPOlUxNY](https://www.youtube.com/watch?v=rm9gPOlUxNY)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `cicd` `ai-automation` `feature-flags` `infrastructure-as-code` `devops`

## Key Insights

- AWS releases with three core pillars: gradual rollout across waves/regions, automatic rollback on alarm triggers, and validation at each stage - a pattern platform teams should adopt for reducing blast radius.
- AI-driven CI/CD through AWS MCP server can deploy full applications (React frontend, Lambda backend, infrastructure) in minutes by describing deployment intent in natural language to AI agents.
- Feature flags enable continuous configuration changes without code deployments, allowing teams to separate feature releases from code deployments and respond to production issues in seconds rather than hours.
- AWS uses Agent SOPs (Standard Operating Procedures) as reusable markdown workflows for AI agents to follow best practices automatically during deployments and troubleshooting.
- Operational flags can automate responses to production anomalies - example shown where CloudWatch alarms automatically toggle logging verbosity from info to debug when suspicious API activity is detected.

## Summary

## Overview
This AWS re:Invent session covers the evolution of CI/CD practices, introducing AI-powered deployment workflows through AWS MCP server and demonstrating advanced feature flagging patterns for continuous configuration management.

## Technical Details
- AWS MCP (Model Context Protocol) server enables natural language deployment commands that generate CDK infrastructure code automatically
- Agent SOPs provide reusable markdown workflows for AI agents to follow deployment and troubleshooting procedures
- AWS releases use wave-based deployments across 30+ regions with automatic rollback capabilities
- Feature flags stored in AWS App Config support gradual rollouts, kill switches, and operational toggles
- Integration with CloudWatch alarms enables automated feature flag responses to production anomalies
- Kira IDE provides native MCP support for seamless AI-assisted development workflows

## Architecture/Patterns
- Trunk-based development with feature flags eliminates long-lived branches and merge conflicts
- Separation of feature releases from code deployments allows independent control of both processes
- Infrastructure as Code generation through AI reduces manual CDK/CloudFormation writing
- Automated operational responses using feature flags as circuit breakers for production issues

## Practical Takeaways
- Implement gradual rollouts with automatic rollback mechanisms to limit blast radius of changes
- Explore AWS MCP server for AI-assisted deployments, especially valuable for startup teams lacking DevOps expertise
- Use feature flags not just for feature releases but as operational controls for logging verbosity, background processes, and emergency responses

## AWS/Cloud Services Mentioned
AWS App Config, Parameter Store, CodePipeline, CodeBuild, CloudFormation, CDK, Lambda, CloudFront, S3, API Gateway, CloudWatch

## Keywords
AWS-App-Config, MCP-server, Agent-SOPs, Kira-IDE, CDK, CloudFormation, CodePipeline, feature-flags, trunk-based-development, gradual-rollout

---
*Generated on 2026-01-04 04:07 UTC*
