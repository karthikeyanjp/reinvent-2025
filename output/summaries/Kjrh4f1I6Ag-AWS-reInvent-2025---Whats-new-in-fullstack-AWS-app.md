# AWS re:Invent 2025 - What’s new in fullstack AWS app development (DVT204)

**URL**: [https://www.youtube.com/watch?v=Kjrh4f1I6Ag](https://www.youtube.com/watch?v=Kjrh4f1I6Ag)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`aws` `ai-development` `fullstack` `infrastructure-as-code` `security`

## Key Insights

- AWS Amplify Gen 2 integrates deeply with CDK, providing L2/L3 constructs that reduce boilerplate while maintaining AWS best practices for authentication, storage, and hosting infrastructure.
- AWS MCP (Model Context Protocol) server bridges the gap between AI coding tools and AWS services by providing 30+ standard operating procedures (SOPs) that guide AI toward production-ready, secure configurations.
- Amplify's battle-tested components (authentication with passkey support, storage browser, WAF integration) eliminate the need for custom implementations of complex features like token rotation and MFA.
- The framework's approach to AI-assisted development focuses on constraining AI choices to proven patterns rather than generating everything from scratch, improving from 10% to 90% production-ready code success rate.
- New security features in 2024 include WAF integration, refresh token rotation automation, email MFA, and SCIM support, addressing common production security requirements out-of-the-box.

## Summary

## Overview
This session demonstrates AWS Amplify's 2024 enhancements for fullstack development, focusing on how AI coding tools can leverage pre-built, production-ready components. The presenters show live coding with AI assistance using the new AWS MCP server to build applications with authentication, storage, and deployment pipelines.

## Technical Details
- AWS MCP server provides 30+ SOPs for guiding AI tools toward AWS best practices
- CDK integration offers L2/L3 constructs with escape hatches for custom infrastructure
- Storage Browser component provides S3 management UI with permissions, thumbnails, and multi-file uploads
- Authentication supports passkey/biometric login, email MFA, and automatic refresh token rotation
- Amplify Hosting includes one-click WAF integration and automatic CI/CD pipelines
- Svelte framework support added through community contributions

## Architecture/Patterns
- Framework-first approach constrains AI code generation to proven, secure patterns
- Infrastructure as Code integration allows mixing Amplify components with custom CDK constructs
- Component-based architecture reduces complex features to single-line implementations
- MCP servers act as knowledge bridges between AI tools and AWS service documentation

## Practical Takeaways
- Use AWS MCP server with Cursor or similar AI IDEs to generate production-ready AWS infrastructure code
- Leverage Amplify's pre-built components for authentication and storage rather than building custom implementations
- Implement WAF protection for frontend applications with single-click integration in Amplify Hosting

## AWS/Cloud Services Mentioned
AWS Amplify, AWS CDK, Amazon Cognito, Amazon S3, AWS WAF, Amazon DynamoDB, AWS Lambda, CloudFront

## Keywords
AWS Amplify, CDK, Model Context Protocol, MCP, Cursor IDE, passkey authentication, storage browser, WAF integration, Cognito, S3, DynamoDB

---
*Generated on 2026-01-04 04:05 UTC*
