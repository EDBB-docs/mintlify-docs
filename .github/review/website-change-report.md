# EDBB website changes for Gerhard

Review date: 28 September 2026. This is a separate proposal for **edbb.com**. No website files, CMS records or production settings were changed. The documentation proposal is in EDBB-docs/mintlify-docs, branch `codex/edbb-documentation-overhaul`.

## Evidence and scope

Reviewed the current public homepage (including its expanded payment FAQ and rendered FAQPage JSON-LD), About, Terms, Contact, Privacy, Legal Notice, and representative Graz and Tokyo location pages. This is a targeted policy/compatibility review, not a claim that all website routes, nine plan selectors, checkout accounts or CMS components were exhaustively tested. Exact component names must be established by the website worker. Shared content is identified by its visible section title below.

Authority: Gerhard's EDBB rules supplied by Mehdi; Mehdi's later confirmations of the traffic cart, paid qcow2 service, annual billing offer and use of the EDIS billing schedule; EDIS docs commit `713a2cf2369196445eee8853e42c67eae2601018`. EDBB panel instructions remain specific to EDBB.

Priority: P1 = contradicts approved policy or materially misleads a purchase decision; P2 = clarity/consistency; decision = verify before making a new commitment.

## Confirmed corrections

### W1 — P1: Refund exceptions in Terms

Page: https://www.edbb.com/terms — **Payment and Billing** and **Termination**. The current wording excludes customer refunds broadly. It conflicts with the approved conditional 24-hour policy. [Current Terms](https://www.edbb.com/terms).

Source: EDIS `faq/billing-lifecycle/cancellation-and-refund-policy.mdx`; EDBB's confirmed shared policy. Current EDBB final route remains `/faq/billing-lifecycle/cancellation-and-refund-policy`.

Replace **Payment and Billing** with:

> Services are billed in advance. Eligible VPS purchases may be refunded under our 24-hour cancellation and refund policy, subject to its conditions and exclusions. Other fees are non-refundable except where these Terms provide otherwise. We reserve the right to adjust pricing with reasonable notice. Continued use of our services after the notice period constitutes acceptance of the new rates.

Link “24-hour cancellation and refund policy” to https://docs.edbb.com/faq/billing-lifecycle/cancellation-and-refund-policy.

Replace **Termination** with:

> You may request cancellation of a service at any time. Cancellation and a refund request are separate actions. Prepaid fees are non-refundable unless the purchase qualifies under our 24-hour cancellation and refund policy or another refund provision in these Terms applies. We reserve the right to terminate your account for violations of these Terms or the AUP, or with reasonable notice if done without cause; unused fees will be refunded for termination without cause by us.

Retain the existing provider-initiated termination exception. Have Gerhard approve the final policy wording; this proposal does not determine statutory rights or alter unrelated liability clauses. Update any duplicated refund FAQ, snippets and FAQPage answers. Do not advertise an unconditional trial or refunds on every order. Coordinate this correction with the approved documentation release.

### W2 — P1: IPv6 limit and location certainty

Page: https://www.edbb.com/ — **VPS Hosting Questions → Do VPS plans include a dedicated IP address?** The visible answer and rendered FAQPage `acceptedAnswer.text` both use the older 10-address limit and overstate geolocation certainty. [Homepage](https://www.edbb.com/).

Source: shared AUP/IPv6 policy permits **20 stable addresses simultaneously**; allocation is /64-equivalent within a shared /48, not a routed customer /64. Third-party GeoIP can be inaccurate.

Replace the answer, both visibly and in JSON-LD, with:

> Every EDBB VPS includes one provider-assigned IPv4 address and an IPv6 allocation equivalent in size to a /64. You may configure up to 20 stable IPv6 addresses simultaneously under the Acceptable Use Policy. Use the prefix and gateway shown in your control panel. Third-party geolocation databases may take time to reflect the correct location.

Link to `/vps-management/ipv6-configuration` and `/acceptable-use-policy`. Find other copies of the same answer. Do not replace valid IPv4 `/24` configuration examples while removing commercial prefix offers.

### W3 — P2: Payment FAQ omits PayPal

Page: https://www.edbb.com/ — **Which payment methods are supported?** The expanded answer and FAQPage schema mention cards and crypto only. Source: approved shared payment methods; final docs `/faq/billing-lifecycle/accepted-payment-methods`.

Replacement for the visible answer and schema:

> EDBB accepts supported cards, PayPal and cryptocurrencies, with additional wallet methods where available. The options shown on your invoice depend on provider availability and eligibility. Contact EDBB support for bank-transfer arrangements and verified EDBB bank details.

Mehdi supplied and confirmed the EDBB EUR PDF on 28 September 2026. It is included unchanged in the docs review branch at `assets/edbb-eur-bank-details.pdf`. After the documentation release, link to `https://raw.githubusercontent.com/EDBB-docs/mintlify-docs/main/assets/edbb-eur-bank-details.pdf` if a website download is needed. Do not use that new production URL before it is deployed, or substitute EDIS banking details.

### W4 — P1: Traffic Pool expiry needs qualification

Page: https://www.edbb.com/vps-hosting/austria/graz — **EDBB: Fast, Simple, Reliable VPS Hosting → Traffic Pool**. It presents pool traffic as non-expiring without explaining assignment expiry. [Graz page](https://www.edbb.com/vps-hosting/austria/graz).

Source: shared traffic policy; final docs `/faq/traffic-bandwidth/traffic-pool`.

Replacement:

> Buy traffic for your shared account pool and assign it to a VPS when needed. Unassigned pool traffic does not expire. Unused traffic assigned to a VPS expires at that VPS's next monthly refill. Every new VPS adds 100 GB starter credit to the pool.

Use https://my.edbb.com/cart.php?gid=214 for an actual purchase CTA. Apply to the shared feature block and every location page using it; update any matching FAQ/schema. Keep monthly EDBB plan allowances separate. Do not copy EDIS volume discounts.

### W5 — P1: Provisioning and installer promises

Pages: https://www.edbb.com/vps-hosting/austria/graz and https://www.edbb.com/vps-hosting/japan/tokyo — shared **Instant Activation / 1-Click OS Installer** feature cards. The timing and universal “latest version” claims exceed the shared delivery policy and current selector. [Tokyo page](https://www.edbb.com/vps-hosting/japan/tokyo).

Source: shared provisioning policy; final docs `/faq/billing-lifecycle/provisioning-time` and `/vps-management/os-availability`.

Replace the activation card heading with **Automated provisioning**, and its text with:

> Provisioning begins after payment is confirmed. Operating-system installation usually takes about five minutes for Linux or 15 minutes for Windows, but payment checks and installation work can take longer.

Replace the installer card text with:

> Install an available Linux or Windows image from the EDBB control panel. Check the current release selector before choosing. Reinstallation erases existing VPS data, so keep a backup first.

Apply to every shared instance and duplicated metadata/schema. Estimates must not become a guaranteed delivery SLA.

### W6 — P2: Legal form and inconsistent location count

Page: https://www.edbb.com/about — introductory identity and **What EDBB Offers**. Its generic company description is less precise than the confirmed legal form, and its location count differs from the homepage's 48. [About page](https://www.edbb.com/about).

Replacement introduction:

> EDBB is an independent VPS hosting brand operated by ED Backbone & Co, a legal partnership in Cyprus. EDBB uses infrastructure from the EDIS Global resource pool and manages its own plans, customers and commercial operations.

Replacement offering sentence:

> EDBB provides Linux and Windows VPS in physical locations across its current location catalogue, with KVM virtualization and administrative access.

Link “current location catalogue” to `/#start-now`. If a count is needed, derive it from the actual orderable location data and reuse that count in the homepage title, description, visible copy and WebSite schema. Do not choose 48 or 50 simply to reconcile text. Keep legal address/VAT details unchanged unless the owner supplies a correction.

## Claims needing evidence or a decision

### W7 — P1 decision: Uptime commitment

Page: https://www.edbb.com/vps-hosting/japan/tokyo — **Uptime >99.9%** feature. A measurable uptime claim needs an approved SLA, measurement scope and remedy. Shared DDoS handling can include null-routing. No such commitment was supplied for this documentation task.

Until verified, replace this card with **Infrastructure status**:

> Check the shared infrastructure status page for reported incidents and maintenance affecting EDBB locations.

Link to https://status.edis.global/. Apply to shared feature instances and any Service/Product/schema promise. Owner question: is there an approved EDBB SLA supporting the percentage? Do not invent credits or availability guarantees.

### W8 — P2 decision: Immediate support / round-the-clock response

Pages: https://www.edbb.com/contact — **Fastest Response**, and location pages such as https://www.edbb.com/vps-hosting/japan/tokyo — **Always-On Support**. The contact page promises immediate access to staff; location copy claims continuous support and fast responses. [Contact](https://www.edbb.com/contact).

The approved scope covers accounts, billing, panel functions and infrastructure; guest administration remains the customer's responsibility. Confirm staffing and response commitments separately.

Safe replacement contact text:

> Contact EDBB through the website messenger or support@edbb.com for account, billing, control-panel and infrastructure questions. Include your service details and relevant error information. You remain responsible for administering your VPS operating system, applications and backups.

For a location card, use heading **Support channels** and:

> Reach EDBB through the website messenger or support@edbb.com. See our support guide for scope and the information to include in a request.

Link to https://docs.edbb.com/how-our-support-team-helps-you. Do not promise a response time without approval. Audit repeated support badges and schema.

### W9 — P2: CPU/uplink labels need a clear scope

Page: https://www.edbb.com/vps-hosting/austria/graz — plan cards and comparison table. The CPU label can imply physical-core exclusivity, while uplink figures can be mistaken for guaranteed VPS throughput. Source: KVM resource model; the approved docs distinguish virtual resources from physical hardware. Existing historical speed-test caveats should remain.

Use **vCPU** for virtual CPU allocations; retain the verified numeric allocation. Add this explanatory text beside network specifications:

> Uplink capacity describes the hosting infrastructure. It is not guaranteed throughput for an individual VPS; actual performance depends on the plan, route, destination and load.

Verify the underlying uplink value and scope before relabelling it as a host-level specification. Update every shared plan card, comparison table and structured specification. Do not alter plan quantities or prices without a verified EDBB product source.

### W10 — P2 decision: Broad network superiority claims

Page: https://www.edbb.com/vps-hosting/austria/graz — **Internet Exchanges, Peerings and Transit Providers**. Qualify global superiority/latency claims. Keep current peer/transit names only if the network owner verifies them.

Replacement introduction:

> Review the network information for this location and test routes to the destinations you depend on. Routing and performance can change with the destination, network conditions and time of day.

Related work: all location-specific network introductions; preserve the existing dated test results and their limitations. No new peering or guaranteed latency claim is authorized.

### W11 — P2 decision: Privacy retention versus VPS disk retention

Page: https://www.edbb.com/privacy — **Data Retention → Retention Periods**. It describes accounting/contract records, not the VPS termination lifecycle. [Privacy page](https://www.edbb.com/privacy).

Do not replace accounting retention periods with the six-day VPS disk period. The legal basis and existing 7/10-year figures need the owner's separate verification if revised. A useful scope clarification is:

> Retention of account, billing and contract records is separate from retention of a terminated VPS's disk data. See the VPS data-retention documentation for the service-deletion timeline.

Link to https://docs.edbb.com/faq/billing-lifecycle/data-retention-period. Do not add a new legal retention promise based on EDIS docs.

## Items checked and rules to preserve

- Homepage unmanaged-server and backup-responsibility wording agrees with the approved policy; preserve it. Paid qcow2 export is a separate service, not routine backups.
- Annual 12-for-11 billing is explicitly confirmed by Mehdi. **Keep the annual offer** on location pages. No other discounts, volume programme or decided reseller programme should be introduced.
- EDBB plan prices are globally uniform for the same plan. Sampled location entry plans are consistent; the worker must compare the complete shared plan data and checkout identifiers before making a site-wide claim of verification.
- Shared status links are intentional. Preserve https://status.edis.global/ and EDBB customer links to https://my.edbb.com/.
- Root administration, customer-hosted APIs and Cloud-Init are not an EDBB customer/order API. Do not remove legitimate application-hosting examples merely because they mention an API.
- No API/BYOIP/commercial /24/reseller promise was identified in the sampled visible pages. Search the full website/CMS/schema for these claims before declaring them absent site-wide.
- No routine-backup, SMTP or DDoS guarantee should be introduced. If these are described, use the final docs: infrastructure protection can null-route; outbound port 25 is rate-limited and abuse can lead to blocking; customers maintain backups.
- Use support@edbb.com and abuse@edbb.com. Verify rendered mailto destinations as well as visible labels; some fetched pages obscure addresses.
- The Legal Notice identifies ED BACKBONE & CO in Cyprus; no fabricated identity/address change is proposed.

## Documentation links and release order

`website-doc-link-mapping.csv` contains all changed documentation routes and final destinations for searching the website source/CMS, plus verified unchanged links observed on the homepage, Terms and Privacy pages. A mapping row marked “search source/CMS” is a migration candidate, not a claim that the old URL was found on a sampled page.

The homepage's observed panel and support links, footer docs link, and legal-page AUP links retain their routes and need no URL replacement. The worker must search the complete website, shared components, structured data, CMS rich text and links containing fragments or `.md` variants using the supplied mapping.

Release the approved documentation redirects and final destinations first (or coordinate a single release). Check hosted HTTP responses and canonicals. Only then switch website links to new paths directly. Keep documentation redirects for old bookmarks. Update visible content and JSON-LD from the same data source and validate both after deployment.

Please pass this website-change report and the accompanying worker prompt back to Gerhard so he can instruct the AI responsible for edbb.com to update the website accordingly.
