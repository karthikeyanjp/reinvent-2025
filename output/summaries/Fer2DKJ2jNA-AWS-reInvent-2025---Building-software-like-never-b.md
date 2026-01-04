# AWS re:Invent 2025 - Building software like never before with Agentic AI (DVT220)

[![Video Thumbnail](https://img.youtube.com/vi/Fer2DKJ2jNA/maxresdefault.jpg)](https://www.youtube.com/watch?v=Fer2DKJ2jNA)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`aws` `ai` `development-tools` `enterprise-rollout` `productivity`

## Key Insights

- Amazon Kira provides spec-driven development with requirements, design, and task phases to generate production-ready code rather than prototype-level outputs, addressing the problem where developers generate massive amounts of AI code with only 25% making it to production.
- Rackspace achieved 85% efficiency gains across 800+ developers using Kira through a phased rollout strategy (8 teams → 100 users → 175 users → 800 users) with mandatory communication and knowledge sharing requirements.
- Amazon Bedrock Agent Core offers modular services (runtime, memory, identity, gateway, browser tools, evaluations, policy) enabling deployment of production-scale agents with any framework (Strands, LangChain, CrewAI) and model choice.
- Agent hooks in Kira automate repetitive development tasks like updating test cases, documentation, and multi-language files whenever code changes, eliminating manual maintenance overhead that often gets deferred.
- Custom steering files in Kira allow teams to inject organizational coding standards, security guidelines, testing approaches, and deployment processes into AI-generated code, ensuring consistency with existing team practices.

## Summary

## Overview
AWS re:Invent session covering Amazon Kira (agentic development environment) and Amazon Bedrock Agent Core for building custom AI agents. Rackspace CTO shared their journey implementing Kira across 800+ developers with 85% efficiency gains.

## Technical Details
- Kira provides spec-driven development with requirements definition, design phase, and task list generation before code creation
- Agent hooks automate repetitive tasks (testing, documentation updates) triggered by file saves or other events
- Advanced context management through steering files containing coding standards, security guidelines, and organizational practices
- Amazon Bedrock Agent Core includes runtime (serverless deployment), memory (short/long-term), identity (IAM), gateway (MCP/OpenAPI), and browser tools
- Strands SDK enables agent building with just prompt and tools definition, deployable to Agent Core
- Support for 100+ models through single Bedrock API with framework flexibility (LangChain, LangGraph, Llama Index)

## Architecture/Patterns
- Multi-agent orchestration where agents feed information to each other (DUVA's Drew AI example with data/help/action agents)
- Phased enterprise rollout strategy: controlled ignition → accelerant phase → gasoline phase → enterprise scale
- Natural language as UI pattern replacing traditional form-based interactions
- Context-aware intelligence leveraging memory and reasoning capabilities for personalized experiences

## Practical Takeaways
- Start Kira evaluation at kira.dev for free to test spec-driven development approach
- Implement agent hooks to eliminate manual documentation and testing maintenance overhead
- Use Amazon Bedrock Agent Core for production agent deployment with built-in observability and security
- Consider multi-agent architectures for complex workflows where agents can collaborate and share context

## AWS/Cloud Services Mentioned
Amazon Bedrock, Amazon Kira, Bedrock Agent Core, Amazon Nova, CloudWatch

## Keywords
Amazon Kira, Bedrock Agent Core, Strands SDK, agentic AI, spec-driven development, agent hooks, steering files, MCP servers, multi-agent orchestration

---
*Generated on 2026-01-04 04:00 UTC*
