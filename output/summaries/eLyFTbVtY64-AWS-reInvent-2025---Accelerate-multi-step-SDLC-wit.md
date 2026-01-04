# AWS re:Invent 2025 - Accelerate multi-step SDLC with Kiro (DVT321)

[![Video Thumbnail](https://img.youtube.com/vi/eLyFTbVtY64/maxresdefault.jpg)](https://www.youtube.com/watch?v=eLyFTbVtY64)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`aws` `ai-agents` `sdlc` `developer-experience` `enterprise-development`

## Key Insights

- AI-Driven Development Lifecycle (AIDLC) extends beyond code generation to include requirements gathering, system design, and planning phases, enabling comprehensive software development workflows with AI agents.
- Custom agents in AWS CodeWhisperer/Kiro CLI combine LLM models, context files, and MCP (Model Context Protocol) tools to create reusable, team-specific development workflows that can be shared across organizations.
- The AIDLC framework emphasizes thorough requirements and design phases before coding, involving cross-functional teams (product managers, developers, QA) to reduce back-and-forth iterations common in traditional development cycles.
- MCP serves as a 'USB protocol for agents,' allowing standardized tool integration across different AI coding platforms, enabling access to external systems like Jira, internal wikis, and AWS services.
- Context window management is critical for AI agent effectiveness - loading relevant documentation, system prompts, and tool outputs while maintaining space for continued interaction significantly impacts code quality and architectural decisions.

## Summary

## Overview
AWS presented AIDLC (AI-Driven Development Lifecycle), a framework that extends AI-powered development beyond code generation to include comprehensive software development phases. The session demonstrated building a browser game using Kiro CLI with a structured approach covering requirements, system design, and implementation.

## Technical Details
- Custom agents bundle LLM models, context files, MCP tools, and system prompts into shareable JSON configurations
- AIDLC framework includes inception phase (requirements/design), construction phase (building/packaging), and operation phase
- MCP (Model Context Protocol) provides standardized tool integration for accessing external systems and resources
- Context window management involves loading system prompts, documentation, chat history, source code, and tool outputs
- Supports both Kiro IDE (spec-driven development) and Kiro CLI (more granular AIDLC workflow)
- Framework generates Mermaid diagrams for architecture visualization and maintains audit logs of decisions

## Architecture/Patterns
- Agent composition pattern: LLM + Context + Tools in iterative loops to achieve goals
- Conditional context loading based on project type (greenfield vs legacy extension)
- Phase-based development with clear gates between requirements, design, and implementation
- Cross-functional team collaboration during requirements gathering to minimize later iterations

## Practical Takeaways
- Teams can create internal repositories of custom agents tailored to specific domains (web apps, legacy systems, compliance requirements)
- WCAG accessibility requirements and company standards can be embedded in custom agent context files
- The framework works with multiple AI coding tools beyond Kiro, making it platform-agnostic for enterprise adoption

## AWS/Cloud Services Mentioned
AWS Bedrock, AWS Amplify, CodeWhisperer, Kiro CLI

## Keywords
AIDLC, Kiro-CLI, MCP, custom-agents, context-window, requirements-gathering, CodeWhisperer, Mermaid-diagrams, cross-functional-teams

---
*Generated on 2026-01-04 04:04 UTC*
