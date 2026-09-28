# Content recovery after PR #2

Date: 28 September 2026. Base: `4017489f8675514a136acf0bb9b16736e050f500`. Reference: EDIS Global `713a2cf2369196445eee8853e42c67eae2601018`. Branch: `codex/edbb-docs-content-recovery`.

Gerhard asked to fix the published rewrite, use EDIS Global's tone and voice, restore missing detail and use native Mintlify components. He also confirmed that the annual 11+1 offer uses a coupon and is excluded from refunds. This record covers the correction branch; `validation.md` is the historical record for the original rewrite.

## Approach

Keep the sound migration work and correct the content. Every existing public route and all 97 redirect definitions remain unchanged. No screenshot, bank PDF, logo or other existing asset was changed. Existing EDBB panel instructions remain the authority for menu labels and screenshots; EDIS is the shared-policy and technical-content reference. The EDIS repository and website were not edited.

The correction restores steps and explanations instead of reverting all 156 files from PR #2. It retains the 11+1 offer and makes its refund exclusion explicit. New guides fill eight useful gaps without adding an API, BYOIP, commercial /24 product, volume discounts or an unapproved reseller programme.

## Main corrections

| Area | Pages/files | Result |
| --- | --- | --- |
| Missing welcome email | `no-email-received.mdx`, `check-your-inbox.mdx` | Complete EDBB reinstall steps and retained screenshot; data-loss warning before reinstalling; separate password-reset paths for servers with data. No promise to resend the original credentials. |
| Coupon refunds | `faq/billing-lifecycle/{cancellation-and-refund-policy,can-i-get-a-refund,billing-workflow}.mdx`, `faq/{hourly-plans-available,free-trials-available}.mdx` | 11+1 remains available; purchases using the coupon are excluded from the refund policy. Cancellation remains a separate action. |
| Broken IP price tables | `faq/ip-addresses/{order-additional-ip-address,order-bespoke-ip-address}.mdx` | Removed malformed table remnants and unconfirmed prices; clear ordering steps and links to configuration. |
| Missing operating instructions | `getting-started/ssh-security-hardening.mdx`, `vps-management/{ipv6-configuration,basic-ipv6-troubleshooting,system-configuration-dialog,os-availability}.mdx`, `advanced-setup-guides/{resize-linux-disk,install-mikrotik-chr}.mdx` | Worked procedures, actual commands, OS/layout branches, verification steps and relevant precautions. |
| Traffic diagnosis | `faq/traffic-bandwidth/{investigate-network-usage,traffic-vs-bandwidth,traffic-pool}.mdx` | Restored tool installation, commands and two existing screenshots; separated plan allowance, monthly usage, port speed and shared pool. |
| Abuse handling | `misc/{reporting-abuse,responding-to-abuse-complaints}.mdx` | Restored useful report/response detail with EDBB contacts and AUP links. No reseller programme implied. |
| Voice and navigation | `docs.json`, landing/support pages and targeted wording across the guides | Direct customer language following EDIS Global; task order in the sidebar; native Steps, Tabs, Cards and Frames; less internal editorial wording. |
| Contact and technical clarity | Welcome/status pages, `faq/billing-lifecycle/vat.mdx`, IP/upgrade pages | Shared status link corrected to `status.edis.global`; clearer VAT categories and IPv6 allocation wording. |

## Eight added guides

- `faq/billing-lifecycle/reset-2fa.mdx`
- `faq/billing-lifecycle/cancel-paypal-subscription.mdx`
- `faq/ip-addresses/configure-additional-ip-linux.mdx`
- `faq/ip-addresses/network-is-down.mdx`
- `faq/ip-addresses/ports-and-firewalls.mdx`
- `getting-started/email-notifications.mdx`
- `vps-management/linux-rescue.mdx`
- `vps-management/rdp-account-locked.mdx`

## Validation

- The repository check covers **110 public pages and 97 redirects**, including metadata/inventory agreement, local links/assets, migration destinations, exclusions and duplicate explicit anchors. It now catches the orphan table separators found in PR #2 and the incorrect `status.edbb.com` destination.
- Official Mintlify `broken-links --check-anchors --telemetry false` passes. The separate redirect option reports `.md` exports as missing local files; these need hosted checks and should not be deleted to satisfy a local file check.
- The current official Mintlify strict prebuild passes. The CLI `validate`/`dev` wrapper cannot enumerate network interfaces in this execution environment, so validation used its official `prebuild(..., {strict: true})` entry point and the official downloaded preview runtime. No repository dependency or Mintlify runtime was patched to make validation pass.
- Rendered HTTP checks: **110/110 pages return 200, render one H1 and use the expected meta description**. All **328 existing explicit section aliases** and **45 heading IDs affected by rewrites** resolve in the rendered destinations. No duplicate authored content IDs remain; Mintlify's repeated desktop/mobile context-menu IDs are excluded from that count. The compact results are in `recovery-validation-summary.json`.
- The agent-browser verification tool repeatedly exits during daemon startup without an actionable browser error. **No desktop/mobile visual pass is claimed for this branch.** The previous rewrite's screenshots do not certify these changed pages.
- No authenticated EDBB workflow, payment/refund, destructive install, disk resize or network reconfiguration was executed. The technical examples need normal staff review on a disposable VPS before being treated as tested procedures.

## Live-site audit and remaining release checks

The audit of the already-published base found 102/102 pages available with one H1, metadata and canonicals; the sitemap contained 102 intended pages. The bank PDF's raw GitHub download worked and matched the supplied PDF. Sampled excluded review/careers paths were not public. These are observations of the base deployment, not proof that an unmerged correction has deployed.

1. Inspect the changed guides in a hosted preview on desktop and mobile, including screenshots, tabs, long tables and code. Spot-check EDBB panel labels with staff access.
2. Preserve and verify all 97 redirects after deployment. The base returned permanent 308 responses for 50 HTML redirects but 307 for 46 Markdown redirects. The remaining OpenAPI URL did not follow its configured redirect. No redirect definitions were removed or weakened here.
3. `/api-reference/openapi.json` still serves the **OpenAPI Plant Store** sample on the audited live deployment, despite there being no EDBB API source in this repository. Repository exclusions and the redirect are already configured. Inspect Mintlify's API/dashboard configuration and rebuild/cache behavior; verify the hosted URL and exports afterward. This branch does not claim to fix that platform state.
4. Verify new pages, canonicals, sitemap, search, `.md`, `llms.txt`, `llms-full.txt`, historical fragments and excluded content on the hosted correction. The base's successful export/canonical checks do not replace release checks for eight new pages.
5. Gerhard should pass the updated `website-change-report.md` and `website-worker-prompt.md` to the website worker. They now explicitly include the 11+1 coupon exclusion for Terms, refund FAQs, annual-offer wording and matching JSON-LD. The website must be corrected separately; this branch does not publish website policy changes.

The branch is a reviewable correction, not a claim that all hosted release checks are complete. Do not reuse the original handover's unverified release claims as approval evidence.
