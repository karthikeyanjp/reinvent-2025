# AWS re:Invent 2025-Unlock the power of Kiro steering: Your blueprint for scalable development-DVT340

**URL**: ![https://www.youtube.com/watch?v=Ap0tXXvyn3k](https://www.youtube.com/watch?v=Ap0tXXvyn3k)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`aws` `ai-development` `developer-experience` `documentation` `code-quality`

## Key Insights

- Kuro steering documents are version-controlled files that provide domain-specific context to AI agents, dramatically improving code quality and consistency by eliminating the need to repeatedly explain organizational standards and patterns.
- Foundational steering files (product, tech stack, structure) can be auto-generated from existing codebases with one click, while custom steering files should encode organization-specific policies like logging standards, security guidelines, and architectural patterns.
- Use workspace-specific steering documents for project-unique requirements and global steering documents for organization-wide standards like security policies, architectural guidelines, and development methodologies across teams.
- MCP (Model Context Protocol) integration allows dynamic inclusion of centralized documentation from git repositories, wikis, and other sources, maintaining single source of truth for organizational standards while keeping steering documents current.
- Kuro Powers enables one-click installation of pre-packaged steering files, MCP servers, and hooks from partners like Stripe, DataDog, and Figma, or creation of custom organizational packages for internal distribution.

## Summary

## Overview
This talk introduces Kuro steering documents as the critical mechanism for providing AI agents with organizational context and domain knowledge. The speakers demonstrate how steering documents transform AI-assisted development from inconsistent outputs to reliable, standards-compliant code generation that aligns with enterprise development practices.

## Technical Details
- Foundational steering files include product requirements, technology stack documentation, and structural patterns auto-generated from existing codebases
- Custom steering files encode domain-specific knowledge like logging standards, security policies, testing frameworks, and architectural guidelines
- Three inclusion modes: always included (project-wide standards), file-specific wildcards (e.g., *.rs for Rust files), and manual inclusion for specialized tasks
- MCP integration enables dynamic context from external sources like git repositories, wikis, and project management systems
- Steering documents are treated as code with version control, pull request reviews, and collaborative maintenance
- Context window management recommends 3-5 focused documents per task rather than flooding with all available guidance

## Architecture/Patterns
- Domain-driven organization of steering documents rather than monolithic files for better maintenance and relevance
- Global vs workspace document strategy: global for organization-wide standards, workspace for project-specific requirements
- Living documentation pattern where steering documents evolve with codebase and team knowledge
- Single source of truth pattern using MCP to reference centralized documentation rather than duplicating content

## Practical Takeaways
- Start with auto-generated foundational files from existing codebases, then incrementally add custom domain knowledge as pain points emerge
- Focus on documenting what LLMs don't know (organizational patterns, business logic, custom APIs) rather than standard library usage they already understand
- Use concrete code examples in steering documents to reduce ambiguity and demonstrate preferred patterns versus anti-patterns

## AWS/Cloud Services Mentioned
AWS Kuro, AWS Q Developer

## Keywords
Kuro, steering-documents, MCP, Model-Context-Protocol, AI-agents, domain-knowledge, code-generation, Kuro-Powers

---
*Generated on 2026-01-04 03:59 UTC*
