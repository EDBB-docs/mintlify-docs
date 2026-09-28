# Validation evidence and limits

> Historical record for the original rewrite and bank-PDF follow-up. For the subsequent content corrections, use [recovery-validation.md](recovery-validation.md). The checks below do not certify changes made after that original review.

Date: 28 September 2026. Source base: EDBB `2e975ea120a5c43ecf73ff3a0165a721ec59191c`; shared reference: EDIS `713a2cf2369196445eee8853e42c67eae2601018`. EDBB main was rechecked before preparing the PR and had not advanced. The live docs' edit destination identifies EDBB-docs/mintlify-docs; the separate starter repository was not edited. No repository-specific AGENTS instructions were present in either checkout.

## Passed

- Official Mintlify build validation: `mint validate --telemetry false`.
- Official internal-link check: `mint broken-links --telemetry false` reported no broken links.
- Additional migration check: `python3 scripts/check-docs.py` validates all **102** navigable pages, title/sidebarTitle/description agreement with the inventory, unique titles/descriptions, local asset targets, direct internal paths, missing pages, duplicate redirect sources, redirect chains/loops, renamed/merged URL coverage (including configured `.md` variants), unsupported callout forms, duplicate explicit aliases and deployment exclusions.
- Local HTTP check: **102/102 pages returned 200**, **102/102 descriptions matched**, and every page rendered **one H1**. No duplicate content IDs remained after removing redundant aliases. Mintlify's own repeated desktop/mobile `page-context-menu` IDs were recorded separately and not treated as authored content defects.
- Historical fragments: **465 original in-page fragment references** from retained/renamed/merged pages resolve to IDs present in the final rendered destination. This includes merged DNS/SMTP/welcome-page anchors. Empty `#` is not counted.
- **97/97 redirect locations matched** the configured direct final destination. No chains or loops in the source mapping.
- All three exact excluded recruitment URLs returned 404 locally. The review inventory URL under `.github/review/` also returned 404 locally.
- Assets: all **82 original raster files** remain in Git without image changes. All **72** originally referenced local asset paths match base bytes. **58** are still referenced by the revised public pages; 14 obsolete illustrations are retained as files. See the screenshot inventory and replacement notes.
- Public external requests: 19 of 20 real linked URLs returned HTTP 200 at the initial pass; the App Store returned 429 to the direct checker, then the web tool verified its redirect to the official Windows App listing. The link was updated to that destination. A documentation-only `cdn.example.com` ISO URL was identified as an example rather than a failed real resource and explicitly labelled for replacement. The final App Store destination was verified via the official listing, not assumed from its name.
- The EDIS reference checkout has no modifications. No website repository was modified.

## Visual inspection

Inspected the local Mintlify preview in desktop light/dark modes and a 390 × 844 narrow viewport. Representative pages: landing page, Traffic Pool, billing workflow, reinstall and Cloud-Init. Verified readable headings, typed callouts, steps, syntax highlighting, loaded retained screenshots and native scrollable tables. Narrow pages inspected had document width equal to viewport width (390 px); tables/code can scroll within their native containers. Desktop examples used a 1280 px viewport. Preview screenshots are in the separately delivered `previews/` folder.

The color configuration now provides a lighter accent on dark backgrounds. Native Mintlify cards/frames/callouts replace custom SVGs, invalid generic callout types, lowercase component names and fragile sidebar CSS. One image path containing a space was encoded, and nested frames were removed after preview inspection.

These are documentation-rendering checks. VPS installations, destructive recovery, networking commands, payment processing and authenticated EDBB panel actions were not executed. Existing EDBB screenshots provide historical UI evidence; current panel verification remains an owner/staff review item.

## Hosted behavior still requiring verification

1. **Redirect status:** configuration uses `permanent: true`, supported by current [Mintlify redirects documentation](https://www.mintlify.com/docs/create/redirects). The local runtime returned **307**, not the documented hosted permanent **308**. Location targets passed, but a permanent production response is not yet proven. Verify hosted preview/deployment before release acceptance.
2. **Canonical URLs:** local HTML omitted canonicals. Verify each hosted final route uses the production canonical without the old slug, localhost or an unintended duplicate `/index` path. Page titles rendered as the page title followed by “EDBB Docs”; descriptions matched frontmatter.
3. **Exports and indexing:** local `/sitemap.xml`, `/robots.txt`, `/llms.txt`, `/llms-full.txt`, `/index.md` and sampled final `.md` routes returned 404. This limits local verification; do not interpret it as proof that hosted exports are absent or broken. Verify the hosted sitemap has only intended routes, `.md` redirects reach working exports, navigation search contains current pages, and stale/merged/career content is removed.
4. **Starter OpenAPI exposure:** no real EDBB OpenAPI source exists. The historical `/api-reference/openapi.json` URL now redirects to `/faq/service-api` and API/template directories are excluded. The existing live `llms.txt` advertised starter API material before this branch. After an approved deployment, verify the export no longer advertises it. Persistent entries may require Mintlify dashboard/API-source cleanup or cache rebuild; no dashboard mutation was performed here.
5. **Exclusion:** `.mintignore` excludes careers, review files, scripts, unused `pages/` and API-template paths, following [Mintlify's exclusion documentation](https://www.mintlify.com/docs/organize/mintignore). Local exact-route tests passed. Recheck hosted behavior and search removal. GitHub visibility is separate: the unpublished reseller proposal is outside the repository entirely.
6. **Search:** local Mintlify search requires authentication; no login was performed. Hosted search indexing remains unverified.
7. **Fragments:** old IDs are preserved, but some obsolete sections now land at the article start (204 aliases) because the old section was removed or merged into a short answer. `anchor-inventory.json` records the destination behavior. Important billing/traffic/IPv6/OS and support anchors were moved beside related current text where feasible. These are not promises of pixel-identical old scroll positions.

## Reproducibility

Node.js 23.11.0; `mint` 4.2.942 with `@mintlify/cli` 4.0.1545. See the repository README for pinned commands. Raw local observations are delivered in `rendered-pages.json`, `rendered-redirects.json`, `excluded-route-checks.json`, `local-exports.json` and `external-link-checks.json`; the compact `validation-summary.json` is also included in the PR.

Final approval should consider the hosted bank-PDF link, actual EDBB UI spot-check, hosted migration/indexing checks and coordinated website Terms update. The PR is a review proposal, not permission to publish.

## Confirmed bank PDF follow-up

Mehdi supplied and confirmed the original one-page EUR iBanFirst document on 28 September 2026. It is copied unchanged into `assets/edbb-eur-bank-details.pdf`; source/destination SHA-256 hashes match. Text and visual inspection confirm the named beneficiary, currency and bank, and the IBAN checksum passes. These checks do not independently authenticate the bank account; owner confirmation is the authority. The payment page and metadata now link the PDF, and the missing-bank-PDF blocker has been removed.

The local PDF download matched the supplied original byte for byte. Mintlify build validation and broken-link checks passed after adding the download link.

## Publication verification

PR #2 merged with owner approval; Mintlify deployment succeeded. The live payment guide rendered, but direct PDF serving returned 404. Mintlify documents PDF hosting as Enterprise-only. The guide now links to the original PDF in the public EDBB GitHub repository; its downloaded SHA-256 matches the owner-supplied file.
