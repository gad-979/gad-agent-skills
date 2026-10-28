# GAD agent skills

A collection of agent skills for designing agents, improving prompts and automating interfaces. Skills are instructions for an AI agent; they do not install software or guarantee a result.

## Skills

| Skill | Purpose | Requirements and example |
| --- | --- | --- |
| [agent-creator](skills/agent-creator/SKILL.md) | Plan custom agents, skills and MCP integrations. | Example: “Design an agent to review database queries.” MCP examples are illustrative and require independent implementation and verification. |
| [automatic-stateful-prompt-improver](skills/automatic-stateful-prompt-improver/SKILL.md) | Improve prompts locally; optionally use an existing compatible server for stateful feedback. | Example: “Improve this prompt for a customer support assistant.” Stateful mode requires a separately configured compatible MCP server; none is provided here. See [setup](skills/automatic-stateful-prompt-improver/SETUP.md). |
| [browser-automation](skills/browser-automation/SKILL.md) | Guide browser and Windows desktop interaction. | Example: “Inspect this webpage and summarize the form fields.” Requires a supported, authorized browser or computer-use tool in the host. |

## Installation for Codex

Clone the repository, then copy the desired skill directory into your Codex skills directory. Replace `<repo>` with the clone location. Review all instructions before use. For another agent, consult its own skill installation documentation.

PowerShell:

```powershell
git clone https://github.com/gad-979/gad-agent-skills.git
New-Item -ItemType Directory -Force "$env:USERPROFILE/.codex/skills" | Out-Null
Copy-Item -Recurse -LiteralPath "./gad-agent-skills/skills/agent-creator" -Destination "$env:USERPROFILE/.codex/skills/agent-creator"
```

macOS/Linux:

```sh
git clone https://github.com/gad-979/gad-agent-skills.git
mkdir -p ~/.codex/skills
cp -R gad-agent-skills/skills/agent-creator ~/.codex/skills/
```

Choose another folder name from the table to install a different skill. Do not overwrite an existing skill without reviewing it first; the copy examples assume the destination does not already exist. Restart the agent session if needed for skill discovery.

## Validation and status

Run `python tests/validate_skills.py` from the repository root for structural checks. This does not execute the skills or prove external integrations work. See [validation notes](docs/validation.md) for the actual checks and limitations. New skills follow the [publication standard](AGENTS.md).

## License

[MIT](LICENSE).
