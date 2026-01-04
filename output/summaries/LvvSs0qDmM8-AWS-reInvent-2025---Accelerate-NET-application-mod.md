# AWS re:Invent 2025 - Accelerate .NET application modernization with generative AI (DVT211)

[![Video Thumbnail](https://img.youtube.com/vi/LvvSs0qDmM8/maxresdefault.jpg)](https://www.youtube.com/watch?v=LvvSs0qDmM8)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `modernization` `dotnet` `generative-ai` `migration` `cost-optimization`

## Key Insights

- AWS Transform for .NET automates 40-70% of .NET Framework to .NET Core modernization tasks asynchronously in the cloud, eliminating the need to tie up senior engineering resources during lengthy transformations.
- Modernization projects are frequently stuck due to resource constraints - senior engineers with legacy knowledge are needed but are typically assigned to feature development rather than modernization work.
- The asynchronous nature of AWS Transform allows transformations of massive codebases (1-10 million lines) to run for days in the cloud without blocking developer machines or IDEs.
- Combining AWS Transform with AI coding assistants like Amazon Q Developer or Kirao creates an effective workflow where automated transformation is followed by AI-assisted completion and validation.
- Thompson Reuters scaled modernization by establishing a central team to operate AWS Transform, allowing product teams to focus on features while modernization happens in parallel.

## Summary

## Overview
AWS re:Invent session on using generative AI to accelerate .NET application modernization from Windows/.NET Framework to Linux/.NET Core. Covers AWS Transform for .NET service and real-world implementation patterns from Thompson Reuters.

## Technical Details
- AWS Transform for .NET combines rules engine (10 years of modernization knowledge) with generative AI via Amazon Bedrock
- Supports both IDE integration (Visual Studio 2022/2026) and web-based bulk transformations via code connections or S3
- Asynchronous processing handles massive codebases (1M-10M+ lines of code) without tying up developer resources
- Automated testing validation runs transformed code and identifies failures for manual remediation
- Creates separate transformation branches to maintain human-in-the-loop approval workflows
- Integrates with AI coding assistants for completing remaining 30-60% of transformation work

## Architecture/Patterns
- Central modernization team pattern: Dedicated team operates transformation tools while product teams focus on features
- Hybrid automation approach: Rules engine for deterministic transforms + LLMs for complex scenarios
- Iterative transformation workflow: Assess → Transform → Validate → Complete with AI assistance
- Cost-driven business case: 40% cost reduction, 1.5-2x performance improvement, 50% better scalability on Linux

## Practical Takeaways
- Start small with modernization programs to work through tooling, permissions, and process issues before scaling
- Build mature CI/CD pipelines before attempting large-scale modernization to handle safe deployment of transformed code
- Establish central teams with .NET expertise to handle bulk transformations, freeing product teams for feature work

## AWS/Cloud Services Mentioned
AWS Transform for .NET, Amazon Bedrock, Amazon Q Developer, Kirao, S3, Code Connections

## Keywords
AWS Transform for .NET, Kirao, Amazon Q Developer, NET Framework, NET Core, Linux migration, Thompson Reuters, asynchronous transformation, Amazon Bedrock

---
*Generated on 2026-01-04 04:02 UTC*
