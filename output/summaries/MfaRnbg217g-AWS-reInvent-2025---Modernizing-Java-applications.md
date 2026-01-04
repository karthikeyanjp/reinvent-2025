# AWS re:Invent 2025 - Modernizing Java applications with generative AI (DVT210)

[![Video Thumbnail](https://img.youtube.com/vi/MfaRnbg217g/maxresdefault.jpg)](https://www.youtube.com/watch?v=MfaRnbg217g)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `modernization` `java` `ai` `cicd` `developer-experience` `enterprise`

## Key Insights

- AWS Transform Custom (released this week) provides a CLI-based autonomous agent for custom code transformations, supporting any language/framework and integrating with CI/CD pipelines for enterprise-scale modernization campaigns.
- ADP achieved 60% faster Java upgrades across 40+ services (600k lines of code) using AI transformation agents, reducing months of work to weeks while eliminating 85% of critical CVEs through dependency updates.
- The tool supports continual learning where transformation definitions improve over time through developer feedback and agent execution, enabling 'learn once, transform everywhere' patterns for organizations.
- Beyond runtime upgrades, the platform handles infrastructure code (Terraform, Docker), UI layers (JSP modernization), and architectural changes (x86 to Graviton migration) through customizable transformation definitions.
- Enterprise adoption requires a center of excellence approach with centralized transformation definition creation by domain experts, then distributed execution by application teams with proper governance and change management.

## Summary

## Overview
AWS announced Transform Custom, an evolution of their Java transformation agent into a general-purpose, CLI-based autonomous agent for code modernization. The session covers real-world enterprise adoption at ADP and demonstrates how AI-driven transformations can address legacy code challenges at scale.

## Technical Details
- Command-line interface supports Maven, Gradle, and other build systems with local branch management for incremental commits
- Orchestrator agent creates comprehensive transformation plans, execution agent applies changes step-by-step, validation agent runs tests and self-debugging
- Supports multi-language transformations (Java, Python, .NET, Rust) and cross-language migrations
- Knowledge base integration stores organizational context, documentation, and custom library upgrade patterns
- MCP (Model Context Protocol) integration connects with existing tools like Jira, Confluence, and GitHub during transformation stages
- Batch processing capabilities enable parallel execution across thousands of repositories using CSV configuration files

## Architecture/Patterns
- Human-in-the-loop design with feedback collection at planning, execution, and validation stages
- Registry-based transformation definitions enable reuse across teams and projects within AWS accounts
- Continual learning captures knowledge items from explicit user feedback and agent execution for future improvements
- Center of Excellence pattern recommended: domain experts create definitions, application teams execute transformations

## Practical Takeaways
- Start with AWS-managed transformation definitions (Java upgrades, Python migrations) before creating custom ones
- Implement transformation campaigns centrally through PMO/developer experience teams for consistent organizational adoption
- Use batch processing and CI/CD integration for scaling beyond individual developer IDE-based transformations

## AWS/Cloud Services Mentioned
AWS Transform Custom, Amazon Q Developer, AWS Batch, EC2

## Keywords
AWS Transform Custom, Java transformation agent, Amazon Q Developer, Gradle, Maven, Spring Boot, GitOps, MCP integration, continual learning, ADP

---
*Generated on 2026-01-04 03:58 UTC*
