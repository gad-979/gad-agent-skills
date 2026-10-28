# Validation notes

The repository's structural validator checks that each skill has a `SKILL.md` with a matching name and nonempty description, checks Markdown relative links in skill entrypoints, checks referenced `references/` and `scripts/` files, and detects common private-key and credential patterns. It requires only Python's standard library. It is not a complete secret scanner or security audit.

The browser-automation PowerShell script is a read-only tool availability check. It does not install or connect any tool. Full browser and desktop interactions depend on the agent host and have not been tested in a clean independent host.

The prompt improver can be used as local writing guidance. The optional MCP server and persistent feedback are not supplied or verified. Conceptual references and sample code must not be assumed runnable.

The agent-creator examples are design guidance, not a tested implementation of a generated MCP server. Generated projects need their own tests.

Installation was checked by copying the three folders to an isolated temporary skills directory and verifying their entrypoints. Agent discovery, a live MCP server, and a fresh third-party desktop setup were not tested.

On the preparation machine, running the PowerShell availability script was blocked by the machine execution policy. No execution-policy changes were made; the script has not been runtime-verified.
