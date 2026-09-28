# Page actions

Original page outcomes and additions: retain: 56, rename: 42, merge: 3, exclude: 3, add: 4.

## Merge

- `/faq/ip-addresses/understanding-dns-systems` → `/faq/ip-addresses/anycast-and-dns-location`: Duplicate intent consolidated into the maintained page.
- `/faq/is-port-25-open` → `/faq/port-25-smtp-rate-limit-policy`: Duplicate intent consolidated into the maintained page.
- `/getting-started/QQQQ_check-your-inbox` → `/check-your-inbox`: Duplicate intent consolidated into the maintained page.

## Exclude

- `/join-our-team/jobs-edisglobal-support-agent-non-voice` → ``: Unverified recruitment content excluded from deployment; no unrelated redirect.
- `/join-our-team/senior-linux-systems-engineer-kvm-and-hosting-expert` → ``: Unverified recruitment content excluded from deployment; no unrelated redirect.
- `/join-our-team/technical-procurement-and-server-operations-coordinator` → ``: Unverified recruitment content excluded from deployment; no unrelated redirect.

## Add

- `(new)` → `/getting-started/ssh-security-hardening`: Relevant missing customer guidance; no EDIS-only panel or API workflow.
- `(new)` → `/misc/responding-to-abuse-complaints`: Relevant missing customer guidance; no EDIS-only panel or API workflow.
- `(new)` → `/faq/service-api`: Relevant missing customer guidance; no EDIS-only panel or API workflow.
- `(new)` → `/getting-started/infrastructure-status`: Relevant missing customer guidance; no EDIS-only panel or API workflow.

## Removed implementation files

Unused `snippets/cta-button.mdx` and starter `snippets/snippet-intro.mdx` were removed. Renamed/merged source files were removed at their old paths and redirected. Recruitment files remain in Git but are excluded by `.mintignore`. No image asset was deleted. The unused `pages/` directory is excluded. The historical starter OpenAPI URL is redirected to an honest no-API explanation; hosted export cleanup must be verified.
