from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skills = root / 'skills'
errors = []
if not skills.is_dir():
    errors.append('skills directory missing')
else:
    for folder in sorted(x for x in skills.iterdir() if x.is_dir()):
        entry = folder / 'SKILL.md'
        if not entry.is_file():
            errors.append(f'{folder.name}: SKILL.md missing')
            continue
        text = entry.read_text(encoding='utf-8-sig')
        parts = text.split('---', 2)
        if len(parts) < 3 or parts[0].strip():
            errors.append(f'{folder.name}: missing frontmatter')
            continue
        name = re.search(r'^name:\s*(.+?)\s*$', parts[1], re.M)
        desc = re.search(r'^description:\s*(?:\S|\n\s+\S)', parts[1], re.M)
        if not name or name.group(1).strip('"\'') != folder.name:
            errors.append(f'{folder.name}: name does not match folder')
        if not desc:
            errors.append(f'{folder.name}: description missing')
        refs = re.findall(r'\]\(((?:references|scripts)/[^)#]+)', text)
        refs += re.findall(r'`((?:references|scripts)/[^\`\s]+)`', text)
        for ref in sorted(set(refs)):
            if not (folder / ref).is_file():
                errors.append(f'{folder.name}: missing {ref}')
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.parts:
        continue
    try:
        text = path.read_text(encoding='utf-8-sig')
    except UnicodeError:
        continue
    if '-----BEGIN ' + 'PRIVATE KEY-----' in text:
        errors.append(f'{path.relative_to(root)}: private key marker')
    if re.search(r'gh[pousr]_[A-Za-z0-9]{30,}', text):
        errors.append(f'{path.relative_to(root)}: possible GitHub token')
if errors:
    print('FAILED')
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: skill structure, referenced local files, basic secret patterns')
