# AWS re:Invent 2025 - Secure Amazon ECS observability with CDK and Grafana (DEV338)

**URL**: [https://www.youtube.com/watch?v=bATt9ZtXSNw](https://www.youtube.com/watch?v=bATt9ZtXSNw)
**Channel**: AWS Events
**Difficulty**: intermediate
**Platform Eng Relevance**: 9/10

## Tags
`observability` `aws` `ecs` `security` `cdk` `opentelemetry`

## Key Insights

- AWS OpenTelemetry Distro (ADOT) runs as sidecars in ECS and automatically instruments applications with minimal code changes, reducing observability setup complexity for platform teams.
- AWS announced deprecation of X-Ray daemon in favor of OpenTelemetry, making OTEL the strategic choice for vendor-independent observability across multi-cloud environments.
- Combining AWS ClientVPN with private subnets enables secure access to internal observability tools like Grafana while maintaining network isolation for sensitive workloads.
- CDK dependency sharing patterns and access points for EFS volumes provide reusable infrastructure components that prevent circular dependencies in multi-stack deployments.
- GitHub OIDC integration eliminates need for long-lived AWS access keys in CI/CD pipelines, improving security posture through temporary, role-based authentication.

## Summary

## Overview
This talk demonstrates building secure observability for ECS applications using AWS CDK, combining AWS native services (X-Ray, Prometheus, Application Signals) with open-source tools (Grafana, Loki) to create dashboards accessible to non-technical users. The solution addresses real-world healthcare startup needs for real-time application monitoring.

## Technical Details
- ADOT collector runs as ECS sidecar, auto-instrumenting applications and sending telemetry to AWS X-Ray and Amazon Managed Prometheus
- Fluent Bit sidecar forwards logs to Loki running in private subnets for centralized log aggregation
- Application Signals plugin in Grafana provides unified view of traces, metrics, and logs with AWS service integration
- EFS with access points provides persistent storage for Grafana configurations and Loki data
- Custom OpenTelemetry metrics complement auto-instrumentation for business-specific monitoring requirements
- Route53 private hosted zones enable secure internal service discovery

## Architecture/Patterns
- Multi-layer security: AWS ClientVPN for secure access, private/public subnet segmentation, least-privilege IAM roles, and localhost-only sidecar communication
- Infrastructure as Code with CDK: Dependency sharing patterns, access point abstractions, and automated security scanning on deployment
- Observability consolidation: Single pane of glass combining AWS native services with open-source tools for comprehensive monitoring

## Practical Takeaways
- Implement OpenTelemetry now as AWS transitions away from X-Ray daemon to ADOT for future-proofing observability stack
- Use GitHub OIDC instead of access keys for secure CI/CD integration with AWS services
- Design security-first architectures with network segmentation and encrypted tunnels for internal tool access

## AWS/Cloud Services Mentioned
ECS, X-Ray, CloudWatch, Prometheus, DynamoDB, SQS, EFS, S3, Route53, ClientVPN, CDK

## Keywords
ADOT, OpenTelemetry, ECS, Grafana, Loki, X-Ray, Application Signals, ClientVPN, CDK, GitHub OIDC, Prometheus, sidecars

---
*Generated on 2026-01-04 04:04 UTC*
