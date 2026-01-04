# AWS re:Invent 2025 - Generative AI, agents, MCP, and the future of AI-powered software development

[![Video Thumbnail](https://img.youtube.com/vi/Kq0Se1nnT3U/maxresdefault.jpg)](https://www.youtube.com/watch?v=Kq0Se1nnT3U)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `ai-agents` `developer-experience` `sdlc` `automation`

## Key Insights

- Custom agents in Curo CLI can be configured with specific tools, contexts, and guardrails to automate repetitive SDLC tasks while maintaining security and governance controls.
- Model Context Protocol (MCP) has emerged as the de facto standard for plugging tools into AI agents, acting like a USB connector for agent capabilities.
- Spec-driven development through agents reduces context switching by converting prompts into clear requirements first, then system design, then tasks - rather than jumping directly to code generation.
- FINRA achieved 30% code quality improvement and 80% positive engineer sentiment by implementing a structured AI adoption approach: explore, scale, then augment phases.
- Context engineering is critical - less context is more effective, explicit instructions prevent hallucination, and using LLMs only for reasoning tasks (not deterministic operations) improves performance.

## Summary

## Overview
AWS re:Invent session covering generative AI agents for software development, focusing on custom agent composition using Curo CLI and real-world implementation patterns. The talk demonstrates how development teams can create specialized AI agents for SDLC automation while maintaining enterprise governance.

## Technical Details
- Agent composition includes LLM selection, context management, tool configuration (MCP servers), resources, and guardrails
- Curo CLI supports both local agents (project-specific) and global agents (cross-project workflows)
- MCP (Model Context Protocol) servers provide skills, resources, and mutative actions to agents
- Bedrock Agent Core offers scalable remote agent infrastructure with modular services for memory, identity, and observability
- Context window management requires compression strategies and careful resource allocation
- Agent hooks enable dynamic context evaluation and execution workflow customization

## Architecture/Patterns
- Spec-driven development pattern: requirements → system design → tasks → implementation
- Agentic loop: input → context → LLM reasoning → tool selection → execution → iteration
- Custom agent architecture with JSON configuration files defining behavior, tools, and constraints
- Remote agent infrastructure supporting asynchronous executions through Bedrock Agent Core

## Practical Takeaways
- Start with local custom agents for project-specific tasks, evolve to global agents for common workflows
- Implement guardrails and tool restrictions to prevent context pollution and ensure secure operations
- Use MCP servers to integrate with existing enterprise SDLC platforms (git repos, CI/CD pipelines, ticketing systems)

## AWS/Cloud Services Mentioned
Bedrock Agent Core, Lambda, DynamoDB, KMS, S3

## Keywords
Curo CLI, MCP, Bedrock Agent Core, custom agents, spec-driven development, agent hooks, context engineering

---
*Generated on 2026-01-04 03:59 UTC*
