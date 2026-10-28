---
name: automatic-stateful-prompt-improver
description: Improve a prompt when requested and optionally use a compatible prompt-learning MCP server for retrieval and feedback.
---

# Prompt improvement with optional state

Use when the user requests prompt improvement or when improving a prompt is part of their requested workflow. Preserve the original goal and constraints.

1. Identify the intended task, audience, inputs, output and success criteria; ask only for essential missing information.
2. Draft a clearer prompt and identify assumptions. Avoid inventing facts or adding requirements the user did not request.
3. When useful, compare variants against a small set of representative cases and report what was actually tested.
4. Optional stateful mode: use a compatible, already configured prompt-learning MCP server only after checking its actual available tools and schemas. Do not assume the server exists or that it exposes any particular operation.
5. Before sending a prompt or feedback to an external service, follow the host's data-sharing and approval rules. Do not record feedback automatically without appropriate authorization.
6. If the server is unavailable, improve the prompt locally and state that retrieval and stateful learning were not verified.

See [setup and limitations](SETUP.md) and the optional conceptual references under `references/`. These references are design examples, not a runnable server or verified performance claims.
