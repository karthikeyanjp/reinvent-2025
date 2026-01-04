# AWS re:Invent 2025 - Scaling Globally: Priority Pass's Journey with AWS Amplify (DVT319)

**URL**: [https://www.youtube.com/watch?v=50hKzkjRErE](https://www.youtube.com/watch?v=50hKzkjRErE)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 7/10

## Tags
`aws` `frontend` `cicd` `cost-optimization` `migration`

## Key Insights

- AWS Amplify reduced Priority Pass hosting costs by 90% (from $180k to $20k annually) while supporting 100M+ annual visitors through automated CDN-first architecture.
- Ephemeral environments are generated automatically per git branch in 6 minutes with isolated URLs, dramatically improving developer testing workflows without infrastructure overhead.
- Direct AWS partnership provides free consultancy access to product teams, significantly reducing time-to-market for complex implementations and custom feature requests.
- Monorepo architecture with NX tooling allows individual Amplify app deployments without full rebuild, enabling independent service releases while maintaining shared libraries.
- Migration from legacy CMS to headless architecture with Next.js increased deployment frequency from 1-2x weekly to hundreds monthly while eliminating manual scaling operations.

## Summary

## Overview
Priority Pass migrated their high-traffic web platform (100M+ annual visitors) from legacy Sitecore CMS on EC2 to AWS Amplify with Next.js, achieving 90% cost reduction and zero manual scaling requirements. The talk demonstrates practical patterns for global CDN-first architecture supporting bursty traffic across multiple time zones.

## Technical Details
- Monorepo architecture using NX tooling with separate Amplify apps per subdirectory
- Infrastructure managed entirely through Terraform including branches and environment variables
- GitHub Actions for CI/CD with automated quality gates before Amplify deployment
- CloudFront CDN with optional Lambda@Edge for server-side rendering abstracted away
- Contentful headless CMS integration replacing legacy Sitecore
- DataDog monitoring integration for observability

## Architecture/Patterns
- CDN-first architecture optimized for global traffic distribution across time zones
- Branch-based ephemeral environments with production mirroring in 6 minutes
- Separation of frontend (Amplify) and backend infrastructure for independent scaling
- Framework-agnostic approach avoiding vendor lock-in to Amplify-specific tooling

## Practical Takeaways
- Engage AWS solution architects for free consultancy to accelerate complex migrations and resolve technical blockers
- Consider Amplify for 90% cost savings over traditional EC2-based hosting for web applications
- Implement ephemeral environments per branch for safer testing without infrastructure complexity

## AWS/Cloud Services Mentioned
AWS Amplify, CloudFront, Lambda@Edge, EC2, GitHub Actions

## Keywords
AWS Amplify, Next.js, CloudFront, ephemeral environments, NX monorepo, Terraform, headless CMS, GitHub Actions

---
*Generated on 2026-01-04 04:04 UTC*
