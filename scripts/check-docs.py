"""Check migration contracts that Mintlify's syntax/link checks do not cover."""
import collections
import json
import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
config = json.loads((ROOT / 'docs.json').read_text())
rows = json.loads((ROOT / '.github/review/migration-inventory.json').read_text())
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

def nav_pages(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == 'pages':
                yield from (x for x in item if isinstance(x, str))
            yield from nav_pages(item)
    elif isinstance(value, list):
        for item in value:
            yield from nav_pages(item)

nav = list(nav_pages(config['navigation']))
check(len(nav) == len(set(nav)), 'Duplicate navigation pages')
active = {r['final_path'].strip('/'): r for r in rows if r['action'] not in ('merge', 'exclude')}
check(set(nav) == set(active), 'Navigation and reviewed page inventory differ')
redirects = config['redirects']
sources = [r['source'] for r in redirects]
check(len(sources) == len(set(sources)), 'Duplicate redirect source')
redirect_map = {r['source']: r['destination'] for r in redirects}
for r in redirects:
    check(r.get('permanent') is True, f"Non-permanent redirect: {r['source']}")
    check(r['destination'] not in redirect_map, f"Redirect chain or loop: {r['source']}")
    path = urlsplit(r['destination']).path.strip('/') or 'index'
    if path.endswith('.md'):
        path = path[:-3]
    check(path in active, f"Missing redirect destination: {r['destination']}")
for r in rows:
    if r['action'] in ('rename', 'merge'):
        for suffix in ('', '.md'):
            check(redirect_map.get(r['existing_path'] + suffix) == r['final_path'] + suffix,
                  f"Missing direct migration redirect: {r['existing_path'] + suffix}")
        check(not (ROOT / (r['existing_path'].strip('/') + '.mdx')).exists(),
              f"Competing old page: {r['existing_path']}")

metadata = collections.defaultdict(list)
for route, row in active.items():
    file = ROOT / (route + '.mdx')
    check(file.exists(), f'Missing page: {route}')
    if not file.exists():
        continue
    text = file.read_text()
    header, body = text.split('---', 2)[1:]
    for key in ('title', 'sidebarTitle', 'description'):
        match = re.search(r'^' + key + r': (.+)$', header, re.M)
        check(bool(match), f'{route}: missing {key}')
        if match:
            value = json.loads(match[1])
            check(value == row[key], f'{route}: inventory differs for {key}')
            metadata[key].append(value)
    # Ignore fenced examples when checking document structure.
    prose = re.sub(r'```.*?```', '', body, flags=re.S)
    check(not re.search(r'^# ', prose, re.M), f'{route}: duplicate H1')
    check(not re.search(r'<(?:warning|info|tip|note)\b|<Callout\b[^>]*type=', prose),
          f'{route}: unsupported callout form')
    ids = re.findall(r'\bid="([^"]+)"', prose)
    check(len(ids) == len(set(ids)), f'{route}: duplicate explicit anchor')
    check('manage.edisglobal.com' not in text, f'{route}: wrong-brand customer destination')
    check('status.edbb.com' not in text, f'{route}: use the shared status.edis.global destination')
    # A leftover separator without a table header passed MDX validation in PR #2.
    lines = prose.splitlines()
    for index, line in enumerate(lines):
        if '|' in line and re.fullmatch(r'[\s|:\-]+', line):
            previous = lines[index - 1].strip() if index else ''
            check('|' in previous and not re.fullmatch(r'[\s|:\-]+', previous),
                  f'{route}: table separator has no header')
    links = re.findall(r'\]\(([^\s)]+)', prose) + re.findall(r'(?:href|src)=["\']([^"\']+)', prose)
    for link in links:
        parsed = urlsplit(link)
        if parsed.netloc or parsed.scheme or not parsed.path:
            continue
        path = unquote(parsed.path)
        if not path.startswith('/'):
            errors.append(f'{route}: use an absolute internal link: {link}')
            continue
        check(path not in redirect_map, f'{route}: internal link uses redirect: {link}')
        target = path.strip('/') or 'index'
        if target.endswith('.md'):
            target = target[:-3]
        check(target in active or (ROOT / target).is_file(), f'{route}: missing internal target: {link}')
for key in ('title', 'description'):
    check(len(metadata[key]) == len(set(metadata[key])), f'Duplicate {key} values')
ignored = (ROOT / '.mintignore').read_text().splitlines()
for excluded in ('join-our-team/', '.github/', 'scripts/', 'pages/', 'api-reference/'):
    check(excluded in ignored, f'Missing deployment exclusion: {excluded}')
check(not any('join-our-team/' in p for p in nav), 'Excluded recruitment content in navigation')
check('https://status.edis.global/' in json.dumps(config), 'Shared status link lost')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(active)} pages; unique metadata; assets/internal targets; {len(redirects)} direct permanent redirects; migration and exclusions.')
