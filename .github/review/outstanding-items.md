# Remaining decisions and release requirements

## Owner input still needed

**EDBB bank-details PDF:** please supply the correct PDF or an existing verified EDBB URL. No PDF was found in the source and none was supplied in the follow-up answer. The payment page safely directs customers to support for ED Backbone & Co bank details; it contains no invented account, EDIS PDF or placeholder download. Add the real document only after its beneficiary and details are verified.

No fixed EDBB price was copied for bespoke IPs, resource additions, traffic quantities or Drive Boost. The pages direct customers to EDBB's current quote/order summary. These are not publication blockers unless the owner wants fixed commercial tables in the docs.

The website report separately lists decisions about uptime, support availability, uplink scope and legal record-retention claims. Those decisions are not silently imported into the docs.

## Confirmed during this work

- Traffic purchase: https://my.edbb.com/cart.php?gid=214, confirmed by Mehdi.
- Paid qcow2 exports: same price and download process as EDIS — EUR 25, password-protected download for 30 days.
- Annual billing: 12 months for the price of 11; preserve this exception to the earlier “no discounts” instruction.
- Billing window: Mehdi's final direction was to use the EDIS pattern. The page follows the published 00:00–05:15 CET schedule and the EDIS table's UTC equivalents. No invented daylight-saving rule was added. If the shared backend schedule later changes, update the shared-source page and EDBB together.

## Before approval/publication

1. Review the draft PR, especially billing/refunds/traffic, technical recovery guides and retained EDBB UI labels. An actual EDBB account was not used to execute workflows.
2. Supply the bank PDF if it is required for this release; otherwise explicitly accept the support-only bank-detail path as an interim solution.
3. Review the coordinated website Terms correction. The existing website still contradicts the approved conditional refund policy until the website owner releases its separate change.
4. In a hosted Mintlify preview, verify canonical URLs, permanent redirect status, sitemap, robots, `.md`, `llms.txt`, `llms-full.txt` and search. Local preview does not implement all hosted endpoints. Check that the starter OpenAPI entry disappears from exports and its historical URL resolves to the no-API page. If it persists, inspect the Mintlify dashboard's API configuration/build cache; do not claim the repository redirect alone removed hosted template metadata.
5. Verify excluded careers/review paths and reseller non-exposure. Careers and review files are excluded by `.mintignore`; the reseller draft is outside the public repository entirely.
6. Obtain Mehdi's approval before merge/publication. After deployment, repeat hosted migration checks, then release website links to new destinations. Keep redirects for old bookmarks.

No merge, production publication, website edit, EDIS repository edit or automatic message to Gerhard was performed.
