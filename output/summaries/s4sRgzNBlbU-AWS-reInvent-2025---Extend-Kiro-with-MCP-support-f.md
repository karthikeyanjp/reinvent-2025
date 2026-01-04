# AWS re:Invent 2025 - Extend Kiro with MCP support for richer context (DVT213)

**URL**: ![https://www.youtube.com/watch?v=s4sRgzNBlbU](https://www.youtube.com/watch?v=s4sRgzNBlbU)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`ai-agents` `developer-tools` `integration-patterns` `context-management` `sdlc-automation`

## Key Insights

- Model Context Protocol (MCP) enables agents to close the feedback loop by observing outcomes of their actions and iterating on solutions, moving beyond one-shot implementations to true agentic behavior.
- Context engineering is the critical factor separating prototype agents from production systems - it's about pruning, summarizing and reloading context at the right time, not just having more information.
- RAG has fundamental limitations as a passive system that can't request different information or follow multi-hop dependencies, while MCP provides dynamic, on-demand context retrieval through tools and resources.
- Remote MCP deployment via HTTPS with OAuth authentication solves the scalability problem of local MCP servers, enabling multi-user production systems with hosted, secure integrations.
- Codebase steering files combined with MCP tools can automate project management workflows, allowing agents to create GitHub issues, update tickets, and maintain documentation without breaking developer flow state.

## Summary

## Overview
This session explores how Ciro (AI coding assistant) leverages Model Context Protocol (MCP) to move beyond traditional RAG limitations and enable production-ready agentic workflows. The speakers demonstrate how context engineering - not just prompt engineering - is the key to successful agent deployments.

## Technical Details
- MCP provides three core primitives: resources (data access), prompts (context templates), and tools (actions agents can take)
- Two transport mechanisms: stdio for local development and streamable HTTP with SSE for production multi-user deployments
- Remote MCP supports OAuth authentication and secure environment variable expansion for production credentials
- Agent feedback loops enable observation of outcomes through terminal output, service logs, breakpoints, and API responses
- Powers feature combines steering files and MCP tools into just-in-time context loading to avoid context window bloat
- Integration spans entire SDLC: ideation (backlog retrieval), implementation (code authoring + testing), deployment (log analysis + fault injection)

## Architecture/Patterns
- Context engineering pattern: dynamic context management through pruning, summarizing and reloading rather than static information injection
- Feedback loop architecture: reason → act → observe → iterate, enabling agents to check and refine their work
- Remote MCP pattern: HTTPS-based servers with OAuth for scalable, secure external system integration
- Steering file pattern: declarative workflow instructions that guide agent behavior across project management tasks

## Practical Takeaways
- Implement MCP servers for your critical data sources using the standard protocol to avoid N*M integration complexity
- Use remote MCP for production deployments to eliminate local setup requirements and credential management issues
- Design context engineering strategies that provide responsive, just-in-time information rather than overwhelming agents with static data

## AWS/Cloud Services Mentioned
GitHub, Figma, AWS-Nova, Slack, Jira

## Keywords
Model-Context-Protocol, MCP, Ciro, context-engineering, agentic-workflows, RAG-limitations, feedback-loops, OAuth-authentication, steering-files, powers-feature

---
*Generated on 2026-01-04 04:01 UTC*
