# AWS re:Invent 2025 - Epic journey: Navigating the AI-powered SDLC from backlog to production(DVT208)

[![Video Thumbnail](https://img.youtube.com/vi/qB7AobjQqsU/maxresdefault.jpg)](https://www.youtube.com/watch?v=qB7AobjQqsU)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `ai-native-development` `developer-experience` `enterprise-transformation` `sdlc`

## Key Insights

- AI-native development requires moving from human-centric to AI-orchestrated workflows where AI acts as a central collaborator, not just an assistant, enabling team-level productivity gains rather than individual efficiency improvements.
- Successful AI transformation requires three pillars: technology foundation (tools like Kura CLI), formal change management with governance frameworks, and cultural transformation including upskilling and performance incentives.
- Spec-driven development becomes critical in AI-native workflows to prevent 'stream of consciousness' problems where requirements drift and documentation gets buried in chat logs, creating structured contracts between humans and AI agents.
- Context management and system knowledge planes are essential for enterprise AI adoption - providing digested information through knowledge graphs and MCP servers enables AI agents to understand complex, million-line codebases effectively.
- Custom agent profiles and steering files allow teams to adapt AI-driven development to their specific workflows, security requirements, and coding standards rather than forcing one-size-fits-all approaches.

## Summary

## Overview
AWS presents their vision for AI-native software development lifecycle transformation, moving beyond bolt-on AI tools to AI-orchestrated workflows. Ericsson shares their 12-month journey implementing this approach across 1,500+ engineers using Kura CLI and custom agents.

## Technical Details
- Kura CLI provides both agentic IDE and command-line interfaces with spec-driven development workflows
- Model Context Protocol (MCP) servers enable AI agents to access enterprise-specific tools and knowledge
- System knowledge planes use knowledge graphs to provide digested information from massive codebases
- Agent hooks trigger autonomous actions on specific events (e.g., auto-updating localization files)
- Custom agent profiles with pre-approved tools and MCP servers adapt to team-specific workflows
- Integration with existing CI/CD pipelines through automated testing and deployment capabilities

## Architecture/Patterns
- Seven-agent blueprint including security experts, architecture experts, and UX specialists operating collaboratively
- Shift-left methodology embedding non-functional requirements from initial design through production
- Three-tier maturity model: AI-assisted → AI-driven → AI-managed development
- Context-aware development using steering files that preserve project intent and coding standards

## Practical Takeaways
- Start with specifications for production code to establish disciplined development processes and prevent code drift
- Implement formal governance frameworks and change management processes when scaling AI adoption across large engineering organizations
- Provide comprehensive context upfront including documentation, constraints, and security requirements rather than simple prompts

## AWS/Cloud Services Mentioned
Kura CLI, Model Context Protocol, AWS CodeWhisperer

## Keywords
Kura-CLI, MCP-servers, AI-native-development, spec-driven-development, custom-agents, steering-files, system-knowledge-plane, agent-hooks

---
*Generated on 2026-01-04 04:07 UTC*
