# AWS re:Invent 2025 - Accelerate development with Kiro's new agentic AI capabilities (DVT228)

[![Video Thumbnail](https://img.youtube.com/vi/XpgcpsGKIio/maxresdefault.jpg)](https://www.youtube.com/watch?v=XpgcpsGKIio)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`ai-development` `developer-experience` `tooling` `automation`

## Key Insights

- Kira Powers solve the context overload problem in AI agents by bundling specialized capabilities with guided workflows, preventing performance degradation as more tools are added to development environments.
- Powers combine MCP (Model Context Protocol) servers with steering files and onboarding instructions, providing a standardized way to give AI agents domain-specific knowledge without overwhelming them with context.
- The power.md format enables teams to codify coding conventions, technology-specific workflows, and best practices into reusable bundles that can be shared across development teams for consistent AI-assisted development.
- Integration with lifecycle hooks allows Powers to automatically enforce standards and run validations (like security checks, testing) when developers make changes, creating closed-loop development workflows.
- The marketplace model for Powers enables community-driven extensibility while maintaining governance - teams can create private power repositories for internal standards while leveraging curated public powers.

## Summary

## Overview
AWS re:Invent 2025 session introducing Kira Powers, a new feature that extends AI development agents with specialized capabilities for specific technologies and workflows. The talk demonstrates how Powers solve context overload in AI agents while enabling domain expertise through bundled MCP servers, steering files, and guided workflows.

## Technical Details
- Powers bundle MCP (Model Context Protocol) servers with markdown-based steering files and workflow instructions
- Each power contains a power.md file with front matter metadata, keywords, and onboarding workflows
- Progressive disclosure architecture prevents context rot by giving agents minimal upfront information about capabilities
- Lifecycle hooks enable automatic validation, testing, and standard enforcement on file save/create events
- Powers marketplace supports both curated partner integrations and custom organizational power repositories
- Integration with popular development tools (Figma, Postman, Supabase, Stripe) through standardized MCP interfaces

## Architecture/Patterns
- Specialized agent capabilities through bundled context and tools rather than monolithic general-purpose agents
- Progressive disclosure pattern to manage AI agent context without performance degradation
- Hook-based automation for enforcing standards and running validations in development workflows
- Community-driven extensibility model with governance controls for organizational power management

## Practical Takeaways
- Teams can codify technology-specific best practices and coding standards into reusable Power bundles for consistent AI-assisted development
- Powers enable automatic security validation, testing, and compliance checks through lifecycle hooks integrated with development workflows
- Organizations can create private power repositories to share internal standards while leveraging public community powers for common technologies

## AWS/Cloud Services Mentioned
None mentioned

## Keywords
kira-powers, mcp, model-context-protocol, ai-agents, steering-files, figma, postman, supabase, development-workflows

---
*Generated on 2026-01-04 04:01 UTC*
