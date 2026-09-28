# Remaining decisions and release requirements

> This is the original rewrite handover. PR #2 and the bank-PDF follow-up have since merged. See [recovery-validation.md](recovery-validation.md) for the current correction branch, completed hosted audit and remaining release checks.

## Bank details resolved

**EDBB bank-details PDF:** supplied and explicitly confirmed by Mehdi on 28 September 2026. The original, unchanged PDF is included as `assets/edbb-eur-bank-details.pdf` and linked from Payment methods. The one-page document identifies ED BACKBONE & CO, EUR and iBanFirst; visual/text checks and the IBAN checksum pass. Ownership/current payment suitability is based on the owner confirmation, not independent bank authentication.

No fixed EDBB price was copied for bespoke IPs, resource additions, traffic quantities or Drive Boost. The pages direct customers to EDBB's current quote/order summary. These are not publication blockers unless the owner wants fixed commercial tables in the docs.

The website report separately lists decisions about uptime, support availability, uplink scope and legal record-retention claims. Those decisions are not silently imported into the docs.

## Confirmed during this work

- Traffic purchase: https://my.edbb.com/cart.php?gid=214, confirmed by Mehdi.
- Paid qcow2 exports: same price and download process as EDIS — EUR 25, password-protected download for 30 days.
- Annual billing: 12 months for the price of 11; preserve this exception to the earlier “no discounts” instruction. Gerhard subsequently confirmed that the 11+1 offer uses a coupon and is excluded from refunds. The recovery branch applies that rule across the refund and annual-offer pages.
- Billing window: Mehdi's final direction was to use the EDIS pattern. The page follows the published 00:00–05:15 CET schedule and the EDIS table's UTC equivalents. No invented daylight-saving rule was added. If the shared backend schedule later changes, update the shared-source page and EDBB together.

## Before approval/publication

1. Review the draft PR, especially billing/refunds/traffic, technical recovery guides and retained EDBB UI labels. An actual EDBB account was not used to execute workflows.
2. Confirm the bank-details PDF link works in the hosted preview before publishing; the missing-file requirement is resolved.
3. Review the coordinated website Terms correction. The existing website still contradicts the approved conditional refund policy until the website owner releases its separate change.
4. In a hosted Mintlify preview, verify canonical URLs, permanent redirect status, sitemap, robots, `.md`, `llms.txt`, `llms-full.txt` and search. Local preview does not implement all hosted endpoints. Check that the starter OpenAPI entry disappears from exports and its historical URL resolves to the no-API page. If it persists, inspect the Mintlify dashboard's API configuration/build cache; do not claim the repository redirect alone removed hosted template metadata.
5. Verify excluded careers/review paths and reseller non-exposure. Careers and review files are excluded by `.mintignore`; the reseller draft is outside the public repository entirely.
6. Obtain Mehdi's approval before merge/publication. After deployment, repeat hosted migration checks, then release website links to new destinations. Keep redirects for old bookmarks.

No merge, production publication, website edit, EDIS repository edit or automatic message to Gerhard was performed.
