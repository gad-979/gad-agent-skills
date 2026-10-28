---
name: browser-automation
description: Automate browser interactions and Windows desktop workflows using available, authorized tools; use for navigation, forms, screenshots, and UI inspection.
---

# Browser and desktop automation

Use an available browser or computer-use integration supported by the current host. Check the host's instructions and tool availability first. This skill is guidance; it does not install a browser, grant access, or supply a desktop automation runtime.

1. Identify the target and the user's desired result. Prefer an existing authorized session and inspect the current UI before interacting.
2. Use the host's supported browser or desktop tools. Ground interactions in the current page or UI state; re-check after actions and verify the result.
3. Follow the host's approval requirements for sign-in, uploads, access changes and external actions. Never bypass security checks.
4. If a required tool is absent, state the missing capability and suggest an installation only when appropriate. Do not automatically install or alter the user's environment.
5. Report what was done, what was verified, and any limitations. Avoid closing or changing unrelated user tabs.

The optional [Playwright reference](references/playwright-cheatsheet.md) is illustrative, not a guarantee that its tools are installed. On Windows, `scripts/setup.ps1` performs a read-only availability check. Run it from PowerShell; it does not install anything.
