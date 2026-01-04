# AWS re:Invent 2025 Cheatsheet

> Bite-sized knowledge for everyday conversations

## Stats That Impress

- **90% cost reduction from $180k to $20k annually**: Priority Pass achieved this migrating to AWS Amplify
  - *Use when: When discussing frontend hosting costs*

- **85% efficiency gains across 800+ developers**: Rackspace's results using Amazon Kiro
  - *Use when: When talking about AI development tools*

- **948% growth in Q Developer adoption in 6 months**: Delta Airlines using dev champions model
  - *Use when: When discussing AI tool rollout strategies*

- **60% faster Java upgrades across 40+ services**: ADP achieved this using AWS Transform Custom
  - *Use when: When discussing legacy modernization*

- **90% time savings in Terraform provider development**: HashiCorp reduced 40-hour tasks to 4 hours with AI agents
  - *Use when: When talking about infrastructure automation*

- **15.9% business value improvement year-over-year**: Amazon's Cost to Serve Software framework results
  - *Use when: When measuring developer experience ROI*

## Concepts to Know

- **MCP (Model Context Protocol)**: USB standard for AI tool integration - lets AI agents talk to any tool
  - *Why it matters: Becoming industry standard, backed by Anthropic*

- **Spec-driven development**: AI creates requirements, design, and tasks before coding
  - *Why it matters: Eliminates 'prompt and pray' - structures AI development*

- **AI-DLC (AI-Driven Development Lifecycle)**: Collaborative mob programming with AI throughout SDLC
  - *Why it matters: Achieves 5-10x productivity gains vs sequential handoffs*

- **Steering files**: Version-controlled context files that teach AI your team's standards
  - *Why it matters: Transforms AI output from inconsistent to enterprise-grade*

- **Kiro Powers**: Pre-packaged AI agent capabilities for specific tech stacks
  - *Why it matters: Solves context overload - agents get expertise when needed*

- **Cost to Serve Software**: Total dev costs divided by delivery units (deployments/PRs)
  - *Why it matters: Amazon's framework for measuring developer experience ROI*

## Hot Takes

- Traditional SDLC metrics like lines of code are dead
  - *Evidence: Amazon measures team-level delivery units, not individual productivity*

- RAG is fundamentally limited for AI agents
  - *Evidence: Can't request different info or follow dependencies - MCP solves this*

- X-Ray daemon is deprecated in favor of OpenTelemetry
  - *Evidence: AWS officially announced OTEL as strategic choice*

- Context engineering beats prompt engineering
  - *Evidence: Less context is more effective than throwing raw data at LLMs*

- Individual developer metrics are meaningless
  - *Evidence: Velocity returns to team mean - focus on team-level improvements*

## Products to Name-Drop

- **Kiro**: AWS's new agentic IDE with spec-driven development
  - *Notable: First IDE built for AI-first development workflow*

- **AWS Transform Custom**: CLI-based autonomous agent for custom code transformations
  - *Notable: Released this week - handles any language/framework*

- **Bedrock Agent Core**: Modular services for building production AI agents
  - *Notable: Serverless agent runtime with built-in security*

- **AWS MCP Server**: 30+ SOPs for guiding AI toward AWS best practices
  - *Notable: Bridges gap between AI tools and cloud services*

- **Amplify Gen 2**: CDK-integrated fullstack framework with battle-tested components
  - *Notable: Reduces complex features to single-line implementations*

## Surprising Facts

- Mob programming with AI is replacing code reviews
  - *Called 'mob elaboration' - whole team + AI designs together*

- Only 25% of AI-generated code makes it to production
  - *Most developers generate massive amounts but ship very little*

- Agent hooks automate documentation updates on file saves
  - *Eliminates manual maintenance that typically gets deferred*

- AI agents need sandbox environments to safely run thousands concurrently
  - *Code execution infrastructure becomes critical bottleneck*

- Fixed workflows with 4 LLM calls beat complex agent architectures
  - *10x performance improvement over basic retrieval approaches*

- Feature flags can auto-toggle logging levels based on CloudWatch alarms
  - *Operational flags respond to production anomalies in seconds*

- Ephemeral environments generate automatically per git branch in 6 minutes
  - *Amplify creates isolated URLs for every branch*
