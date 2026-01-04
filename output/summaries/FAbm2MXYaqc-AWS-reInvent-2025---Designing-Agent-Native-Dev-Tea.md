# AWS re:Invent 2025 - Designing Agent-Native Dev Teams: Coding Agents in Real Workflows (DVT226)

**URL**: ![https://www.youtube.com/watch?v=FAbm2MXYaqc](https://www.youtube.com/watch?v=FAbm2MXYaqc)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`ai-agents` `developer-experience` `automation` `cicd` `platform-engineering`

## Key Insights

- Agent-native development requires structured workflows beyond simple code generation - implement spec-driven development where agents handle planning, design, and task breakdown before code implementation.
- Autonomous agents need sandboxed environments with proxy controls and persistent context to work safely across multiple repositories while maintaining security boundaries.
- Context management at enterprise scale requires ontologies and structured data relationships rather than brute-force feeding raw data into LLMs - quality over quantity is critical.
- Team-level agents with multiplayer capabilities can integrate with existing tools (GitHub, Slack, Jira) to handle background tasks while maintaining proper attribution and audit trails.
- Agentic workflows should use graph-based task orchestration rather than linear workflows, allowing sub-agents to make decisions that can change the entire execution path.

## Summary

## Overview
Kyle and Ben from Curo present their agent-native development platform that moves beyond simple code generation to autonomous agents capable of handling complex, multi-repository workflows. They demonstrate how structured agent workflows can transform developer productivity from coding-heavy to planning and testing-focused work.

## Technical Details
- Curo IDE implements spec-driven development with planning, design, and task breakdown phases before code generation
- Autonomous agents run in sandboxed Docker environments with proxy controls and persistent context management
- Context management uses steering files, embeddings, and graph structures rather than raw data injection
- MCP (Model Context Protocol) integration provides access to external tools and documentation
- Event journaling maintains agent memory across task sessions for continuity
- Team agents support multiplayer workflows with GitHub, Slack, Jira, and Confluence integrations

## Architecture/Patterns
- Graph-based task orchestration with sub-agents that can modify execution paths dynamically
- Layered context architecture combining repo-level, cross-repo, and organizational data structures
- Proxy-wrapped agent environments that restrict network access and prevent unauthorized actions
- Ontology-driven data relationships for enterprise-scale context management rather than vector search alone

## Practical Takeaways
- Start with structured workflows using specs or planning phases before implementing autonomous agents
- Implement proper sandboxing and security controls when deploying agents that can modify codebases
- Focus on data quality and structure rather than feeding raw enterprise data directly to LLMs for better results

## AWS/Cloud Services Mentioned
AWS Bedrock, GitHub, Docker

## Keywords
curo, autonomous-agents, spec-driven-development, mcp, bedrock, sonnet, ontologies, graph-orchestration, sandbox-environments

---
*Generated on 2026-01-04 03:59 UTC*
