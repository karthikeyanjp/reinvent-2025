# AWS re:Invent 2025 - From concept to production: Build with spec-driven development & Kiro  (DVT320)

[![Video Thumbnail](https://img.youtube.com/vi/VRw3g-v4B00/maxresdefault.jpg)](https://www.youtube.com/watch?v=VRw3g-v4B00)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`aws` `ai-development` `developer-experience` `enterprise-tools` `code-generation`

## Key Insights

- Kira introduces spec-driven development to solve LLM scalability issues by generating requirements, design, and project plans before code implementation, reducing non-deterministic outcomes across development teams.
- Agent hooks enable event-driven automation (e.g., file save triggers) that can sync changes between local specs and external tools like Jira, creating bidirectional integration workflows.
- MCP (Model Context Protocol) servers provide extensible integration with third-party tools, allowing teams to pull requirements from existing systems and maintain single sources of truth.
- Steering documents automatically reverse-engineer existing codebases to create context summaries, tech stacks, and dependency maps, enabling LLM agents to work effectively with large legacy applications.
- The tool addresses three core enterprise challenges: scaling AI development across large teams, providing control over AI decision-making, and maintaining code quality consistency.

## Summary

## Overview
AWS Kira is a new VS Code-based AI development tool that went GA two weeks before re:Invent 2024, focusing on spec-driven development to solve enterprise-scale AI coding challenges. The session demonstrates building a fitness tracking application live, showcasing how Kira generates requirements, design documents, and implementation plans before writing code.

## Technical Details
- Built as VS Code fork with 200,000 token context window
- Supports Claude Sonnet 3.5/4, Haiku, and Opus models (no bring-your-own-key)
- Generates three core documents: requirements.md, design.md, and tasks.md stored in .kira directory
- Agent hooks provide event-driven automation (file save, create, delete, manual triggers)
- MCP servers enable local and remote integrations with tools like Jira, Confluence, SharePoint
- Steering documents auto-generate from existing codebases: product summary, tech stack, and dependency mapping

## Architecture/Patterns
- Spec-driven development pattern: requirements → design → implementation plan → code generation
- Three-phase approach prevents non-deterministic LLM outputs through upfront context definition
- Collaborative development model with shared specs, steering files, and hooks across team members
- Integration pattern using MCP servers for bidirectional sync with enterprise tools

## Practical Takeaways
- Teams can standardize AI development workflows by defining requirements and design specs before code generation
- Legacy application modernization becomes more manageable through automatic steering document generation
- Enterprise tool integration (Jira, Confluence) maintains single source of truth through agent hooks and MCP servers

## AWS/Cloud Services Mentioned
AWS Kira, Q Developer

## Keywords
Kira, spec-driven-development, MCP-servers, agent-hooks, steering-documents, Claude, VS-Code, requirements-generation

---
*Generated on 2026-01-04 04:08 UTC*
