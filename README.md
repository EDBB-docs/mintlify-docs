# EDBB documentation

Mintlify source for https://docs.edbb.com, operated by ED Backbone & Co.

## Review and preview

Use Python 3 and Node.js 18 or newer. This overhaul was checked with `mint` 4.2.942 (underlying `@mintlify/cli` 4.0.1545).

```sh
python3 scripts/check-docs.py
npx --yes mint@4.2.942 validate --telemetry false
npx --yes mint@4.2.942 broken-links --telemetry false
npx --yes mint@4.2.942 dev --no-open --telemetry false
```

Mintlify keeps its preview cache in the current user's home directory. Local search requires a Mintlify login; do not treat an unauthenticated local preview as a search-index test. Local exports, canonicals and redirect status codes can differ from hosted deployment. See `.github/review/validation.md` for the actual evidence and release checks.

## Content rules

- EDBB's panel, plans, checkout, screenshots, contacts and bank details are EDBB-specific. Shared backend policy comes from the owner-approved EDIS reference; see `.github/review/source-matrix.csv`.
- EDBB has no customer/order API, BYOIP, commercial /24-prefix offering or volume programme. Annual billing provides 12 months for the price of 11; do not introduce other discounts.
- No routine backups are supplied. A separately requested EUR 25 qcow2 export has a protected download available for 30 days.
- Preserve the intentional shared status link, https://status.edis.global/. Customer actions use https://my.edbb.com/.
- Keep the refund, cancellation, billing, retention and traffic pages consistent. Unassigned traffic does not expire; unused assigned traffic expires at the VPS's monthly refill.
- Use native Mintlify components. Every navigable page needs a unique title/description and a concise sidebarTitle. Preserve EDBB UI labels; confirm uncertain controls with current panel evidence.
- For URL changes, update the migration inventory, internal links, navigation, redirects and important heading anchors together. Redirect to final destinations directly.
- `.mintignore` excludes review files, scripts and dormant recruitment material from publication. Exclusion does not make GitHub files private. Keep undecided reseller proposals outside this public repository.

## Publishing

This branch is a proposal. Do not merge or publish without Mehdi's approval. Review the handover and release checklist first, particularly bank details, hosted exports/indexing and the coordinated edbb.com policy corrections.
