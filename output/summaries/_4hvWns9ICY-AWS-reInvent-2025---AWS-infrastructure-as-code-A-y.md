# AWS re:Invent 2025 - AWS infrastructure as code: A year in review (DVT203)

[![Video Thumbnail](https://img.youtube.com/vi/_4hvWns9ICY/maxresdefault.jpg)](https://www.youtube.com/watch?v=_4hvWns9ICY)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `infrastructure-as-code` `cloudformation` `cdk` `governance` `security` `developer-experience`

## Key Insights

- AWS CloudFormation now offers pre-deployment validation that catches resource naming conflicts, invalid property values, and deletion errors during changeset creation, reducing the feedback loop from hours to minutes.
- CloudFormation launched drift-aware changesets that provide three-way comparisons between actual resource state, new template, and previous template, enabling safe reconciliation of out-of-band changes without losing data.
- CDK refactor command allows infrastructure refactoring (construct renaming, moving resources between stacks, upgrading L1s to L2s) without resource deletion or data loss, treating infrastructure code more like application code.
- CDK mixins library decouples cross-cutting concerns like encryption, logging, and tagging from L2 constructs, making them composable building blocks that can be applied to any construct level including custom ones.
- CloudFormation Hooks integrated with AWS Controls Catalog enables platform teams to enforce security best practices proactively at deployment time with just three clicks, shifting security left in the deployment pipeline.

## Summary

## Overview
AWS presented their 2025 Infrastructure as Code (IaC) innovations focused on three pillars: faster development, safer evolution, and better governance. The session covered major improvements to CloudFormation, CDK, and related tooling that address common pain points in enterprise IaC workflows.

## Technical Details
- Pre-deployment validation in CloudFormation catches errors during changeset creation rather than deployment execution
- Drift-aware changesets provide three-way diffs to safely reconcile out-of-band changes with desired template state
- CDK refactor command maps logical IDs between deployed and local constructs to enable safe infrastructure refactoring
- AWS Toolkit IDE plugins provide autocomplete, linting, and security validation for CloudFormation templates
- CDK mixins library extracts cross-cutting concerns from L2 constructs into composable, reusable abstractions
- CloudFormation Stack Sets now supports dependencies for ordered deployment across multiple accounts

## Architecture/Patterns
- Defense-in-depth strategy combining proactive controls (Hooks) with automated account baselining (Stack Sets)
- Composable construct patterns using mixins instead of inheritance-heavy L2 constructs
- Multi-account governance with dependent stack sets for proper resource ordering
- AI-assisted IaC development using MCP servers for better context and validation

## Practical Takeaways
- Implement pre-deployment validation to catch configuration errors before resource provisioning begins
- Use drift-aware changesets to safely manage infrastructure that has accumulated out-of-band changes
- Leverage CDK mixins for cross-cutting concerns like encryption and logging across multiple services and construct levels

## AWS/Cloud Services Mentioned
AWS CloudFormation, AWS CDK, AWS Lambda, Amazon S3, AWS KMS, CloudWatch, AWS Organizations, AWS Controls Catalog

## Keywords
CloudFormation, CDK, drift-aware-changesets, pre-deployment-validation, CDK-refactor, mixins, hooks, stack-sets, MCP-server, constructs

---
*Generated on 2026-01-04 04:06 UTC*
