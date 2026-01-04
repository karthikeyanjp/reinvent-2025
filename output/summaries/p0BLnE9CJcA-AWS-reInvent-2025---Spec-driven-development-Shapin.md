# AWS re:Invent 2025 - Spec-driven development: Shaping the next generation of AI software (DVT212)

**URL**: [https://www.youtube.com/watch?v=p0BLnE9CJcA](https://www.youtube.com/watch?v=p0BLnE9CJcA)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`ai-development` `developer-experience` `testing` `requirements-engineering` `code-generation`

## Key Insights

- Spec-driven development with Kira creates three artifacts (requirements, design, tasks) before writing code, reducing the 'prompt and pray' loop by establishing clear technical decisions upfront.
- Property-based testing (PBT) automatically generates comprehensive test scenarios from structured requirements, providing better coverage than manual edge case testing while tracing back to original requirements.
- Using industry-standard EARS syntax for requirements enables automated parsing and validation, helping identify conflicting or ambiguous requirements before implementation.
- The Kira team uses specs as replacements for traditional design reviews, committing them to git repos for traceability and allowing requirement changes to automatically update design and tasks.
- MCP integration allows pulling requirements from external systems (Jira, Linear) and referencing documentation, providing richer context for more accurate code generation decisions.

## Summary

## Overview
This session introduces spec-driven development using Kira, an AI coding assistant that structures the software development lifecycle by generating requirements, design, and task specifications before writing code. The approach aims to bring predictability and reproducibility to AI-assisted development.

## Technical Details
- Three-phase workflow: requirements (using EARS syntax) → design (architecture decisions) → tasks (discrete implementation units)
- Property-based testing generates comprehensive test scenarios from structured requirements, providing better coverage than manual testing
- MCP (Model Context Protocol) integration enables pulling context from external systems like Jira, documentation, and existing codebases
- Specs are committed to git repositories as markdown files for team collaboration and traceability
- Built-in steering files provide persistent project context (tech stack, structure, product flow)
- Spec MVP mode allows rapid prototyping by marking testing tasks as optional

## Architecture/Patterns
- Structured workflow replacing ad-hoc prompting with planned development phases
- Requirements traceability from acceptance criteria through to property tests
- Git-based collaboration model where specs serve as living documentation and ADRs
- Context-aware development using project steering and external knowledge sources

## Practical Takeaways
- Start with structured requirements using EARS syntax before any code implementation
- Commit specs to version control for team alignment and decision documentation
- Use property-based testing to automatically validate system invariants across multiple scenarios

## AWS/Cloud Services Mentioned
AWS Amplify, AWS Cognito

## Keywords
Kira, spec-driven-development, property-based-testing, EARS-syntax, MCP, AI-coding, requirements-traceability

---
*Generated on 2026-01-04 04:03 UTC*
