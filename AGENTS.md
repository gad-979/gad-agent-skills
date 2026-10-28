# GAD skills publication standard

For every skill added or materially changed in this repository:

- Preserve the creator's name, ownership and existing license obligations. Never claim unverified third-party content as original.
- Review the complete package for secrets, private paths, missing files, unsafe instructions, unsupported claims and external dependencies.
- Provide a clear description, appropriate installation guidance, an example request, and explicit setup requirements and limitations.
- Check the skill frontmatter and referenced local files, exercise runnable scripts in a safe isolated environment, and perform a meaningful use-case test where possible.
- Record actual test results and clearly label anything untested or unavailable. Do not describe conceptual examples as working implementations.
- Review the final changes before publishing and follow the user's instructions about approval, visibility and permissions.
- Run `python tests/validate_skills.py` and fix failures before publishing. The validator is a structural check and does not replace behavioral testing.
