# MidTown Dental Care

Website redesign for Dr. Laura Russell’s Wauwatosa practice. Built in Astro with static output for Cloudflare. All photos and the logo are served locally; fonts are bundled locally.

The original request was homepage-first; Bryan later requested completion of the remaining pages. His November 2 question about the initial one-page build did not establish a one-page-only engagement or waive remaining migration work. Bryan subsequently reported that the website appeared to be working after the nameserver repair; the timed diagnostic results below remain historical checks.

## Navigation

The November 2 navigation update replaces the homepage's section-only menu with shared dropdowns for Our practice, Dental services, and Patient info, plus a direct Contact link. The saved WordPress header provided the navigation reference. All 25 built services appear in four groups; practice/team profiles and patient resources are directly accessible. Footer navigation now opens the corresponding pages on the homepage too. The restored blog is available under **Patient info → Patient education & blog** and in the footer. Unmigrated legal destinations were not added to the header.

Verification: production build passed; all 25 catalog services are included and all 45 header links resolve to built pages. Browser checks covered desktop, 1051px breakpoint, 390px and 320px mobile widths, service/patient link navigation, scrollable mobile menus, and Escape closing with focus return. No horizontal overflow was found at the checked widths. Evidence is in ignored `outputs/launch-2026-11-02/navigation/`. This is a navigation improvement, not completion of the remaining migration or launch checklist.

## Development

Requires Node 22.22 or later.

```sh
npm install
npm run dev
npm run build
npm run preview
```

Use the local URL printed by Astro. The production build is written to `dist/`.

## Cloudflare

For Cloudflare Pages, set the build command to `npm run build` and the output directory to `dist`. The Node version must be 22.22 or newer. No server adapter, database, secrets, or environment variables are required.

The custom domain serves this build. Bryan authorized production indexing on November 3; preview and utility pages remain noindex. **The remaining legal, ownership, form, tracking and launch-review items are still open.** The approved homepage and 48 other core content routes are built, plus an archived COVID notice, a form completion page and real 404. The expansion includes all 25 services in the directory, four dentist bios, two staff profiles, membership, financing, the real before/after gallery, accessibility information, and patient resources. All 50 old blog sources were recovered; 49 distinct articles remain published and one mis-titled duplicate now redirects to the matching cosmetic service. The blog index, 41 category/tag archives, and seven pagination routes are built; six duplicate-only archives also redirect to cosmetic dentistry. Old advertising and confirmation URLs redirect to matching existing destinations. Four legal paths remain unresolved: Privacy, Terms of Service, Disclaimer, and EULA. The footer privacy destination currently returns 404.

On November 2, Bryan connected the apex production domain to Pages and then explicitly authorized a limited repair of the failing `www` hostname. The Pages wizard replaced four old `www` A/AAAA entries with `CNAME www → midtown-dental.pages.dev` and associated that hostname with this project. Both domain variants served this build over HTTPS after that repair. This routing repair did not complete the production migration. Production noindex was retained at that checkpoint and was released separately under Bryan’s November 3 indexing authorization. The November 2 inventory contains 156 sitemap URLs plus 218 additional discovered URLs; the remaining content, authority data, and exact migration behavior must be resolved before cutover. Private source snapshots, the URL manifest, verification, and the launch handoff are kept in the ignored `outputs/launch-2026-11-02/` directory.

A second outage on November 2 followed delegation to GoDaddy's default nameservers. With Bryan's explicit approval, GoDaddy forwarding was removed and the custom nameservers restored to `emma.ns.cloudflare.com` and `yadiel.ns.cloudflare.com`. The existing `.org` DMARC policy was preserved in Cloudflare; `.net` email settings were not changed. Cloudflare's active `MidTown apex to www` Single Redirect sends the apex hostname to HTTPS www with the original path and query string (301). Direct Cloudflare tests passed with normal TLS verification. At 23:47 UTC, the `.org` registry and public resolvers still returned GoDaddy's nameservers, and normal public HTTPS requests still failed; public recovery remains unverified pending delegation updates. Evidence and the prior zone backup are in ignored `outputs/launch-2026-11-02/nameserver-repair/`. Do not recreate GoDaddy forwarding for this domain.

The static build includes 150 HTML pages, a real `404.html`, and a 141-URL XML sitemap (form completion, 404, redirects, and archive pagination are excluded from the sitemap). `public/_redirects` contains the service/landing/confirmation repairs and exact mappings for 200 duplicated WordPress numbered article URLs. Both slash variants are handled for the new mappings (433 rules total). Real archive pagination remains intact. Authority/SEO sign-off remains separate. Astro preview does not emulate Cloudflare redirect rules, so validate redirects on Pages.

## Search Console verification

On November 3, Bryan requested HTML-tag verification for the URL-prefix property `https://www.midtowndentalcare.org/`. The supplied Google verification tag is rendered in the homepage's `<head>` by `src/layouts/SiteLayout.astro`; keep it after verification so ownership can be rechecked. This verifies only the specified URL prefix, not a DNS Domain property. Ownership was verified under `info@alphadogagency.com`. Bryan subsequently authorized production indexing and sitemap submission as described below. Client ownership/delegation and the other launch gates remain separate follow-up items.

## Appointment form

The homepage, `/contact/`, and `/appointment/` embed the real Jotform [263055223419049](https://form.jotform.com/263055223419049), created in the existing HIPAA Jotform workspace. Bryan confirmed `frontdesk@midtowndentalcare.net` as the receiving inbox on November 2. All contact fields remain PHI-protected; notification emails contain no patient answers and require authorized Jotform access to review the submission. Practice access to those submissions still needs confirmation.

The form includes required name, phone, email, contact preference, patient status, contact consent, and hCaptcha. It collects no medical free text, attachments, birth dates, or insurance identifiers. Its confirmation says the appointment is not yet booked. The branded `/thank-you/` route is for the real provider success redirect, not a simulated submission. Keep that route noindex at production launch. Update the Jotform success redirect to the production origin when launch is approved.

The embed uses Jotform's official resize helper and a direct-link fallback. The homepage appointment grid uses fixed vertical gaps so the section accounts for the full resized form height and keeps its fallback link above the footer. Camera, microphone, geolocation, and payment permissions are not granted. Required-field validation was verified without submitting. Bryan explicitly reserved the end-to-end submission/inbox test for his team; successful delivery is **not verified**. Confirm inbox receipt, authorized access to request details, acknowledgment, and success redirect before production use. Existing OperaDDS patient forms and payment links are preserved.

## Content sources and launch checks

- Client design direction: Laura’s September 28, 2026 “Comp Sites” email; a balance between Emily Stout DDS and 816 Med Spa, modern and family-friendly.
- Copy source: https://www.midtowndentalcare.org/ and its provider, office, services, and patient information pages, checked October 7, 2026.
- Photos and logo: existing Midtown website. The two homepage waiting-room photos use edited copies with the retired books and train table removed following Laura’s October 9 feedback. Originals are preserved in `public/images/`; edited sources are in `src/assets/images/` and Astro produces responsive WebP files. The image-editing tool and exact prompts are recorded in `docs/photo-edits.json`.
- Patient quote: Bonnie H., as published on the existing site, linked to the practice’s Google reviews.
- Confirm provider roster, phone numbers, hours, financing, and clinical details with the practice before launch.
- The core page source copy is in `src/data/core-pages.json`, with its source URL per route. The content comes from the current practice website, checked November 2. The later brief overrides obsolete PPO acceptance copy and online-booking CTAs. Insurance language is neutral pending the approved wording; MetLife is not named. Dr. Hoyme is identified as a general dentist, consistent with her existing bio. No unverified memberships were added. New implant testimonial blocks were withheld pending documented permission.
- Titles, descriptions, and H1s generally carry over from the existing pages. The full practice name is normalized where necessary; the payment/contact descriptions were revised to avoid obsolete insurance and form claims. The approved homepage has different metadata/H1 from the old site; this is an explicit migration-review item, not assumed SEO approval.
- Sitewide Dentist schema and footer NAP/hours use the existing website's details. The public Google Maps listing confirms 8726 W North Ave, Wauwatosa, WI 53226, (414) 258-5351, Monday–Thursday 8–5 and Friday 8–3; verified November 2. The site follows the brief's MidTown capitalization (Maps displays Midtown). Practice ownership of both phone numbers, particularly the separate new-patient number, remains open. No Gargle GTM container was copied; fresh GTM/GA4/Ads/Meta configuration and live conversion tests are still required.
- The existing logo is 318 × 111 pixels. Replace with a higher-resolution or vector original if supplied.
- The handoff WordPress backup was downloaded November 2 and selectively extracted to recover public blog images. No WordPress code was executed and a full site/database restore has not been tested. The backup and private extraction evidence are not committed.
- Team-owned final form check: submit a clearly labeled test, verify receipt at the confirmed front-desk inbox and secure access to details, and check the acknowledgment/thank-you redirect. No test request was sent by Codex.
- Update service/provider URLs to local routes as additional pages are built; preserve old URLs or add redirects at migration.
- Production `public/robots.txt` allows crawling and advertises the canonical production sitemap. `SiteLayout.astro` excludes only local development, the thank-you route and error page from indexing. Hostname-specific rules in `public/_headers` keep both `*.pages.dev` and `*.*.pages.dev` previews noindex, while allowing crawlers to read that header. Test actual production and preview responses after deployment; Astro preview does not emulate Cloudflare headers.

## Agency standards

The user-supplied ADA web checklist and design standard were received November 2. `AGENTS.md` contains Part B and the current stage/brand guardrails. The full eight-section assessment is in the private readiness report. No checklist section is treated as complete merely because the documents are now available.

The November 2 standards pass adds a persistent mobile call/request bar, Apple touch icon, Open Graph photo, two local font preloads, and responsive WebP derivatives for all displayed practice photos. The privacy footer link currently returns 404 following domain cutover. The old policy relied on Termageddon; its ownership/license and updated legal copy need review before migration, and no legacy policy script was copied.

The share-image origin in `src/layouts/SiteLayout.astro` now uses the canonical production domain; social previews no longer depend on the preview host. Astro is pinned to 7.4.1 and `.node-version` pins the tested Node 22.22.2 runtime. The standards pass dependency audit reports zero vulnerabilities; this is not proof of account ownership, 2FA, form security, or backup restoration.

## November 2 page expansion

Added 29 source-backed content routes while retaining the approved design. New metadata, clinical/service copy, membership terms, historical staff roster, and gallery permissions remain subject to practice review. Obsolete PPO claims and the old 2022 membership price graphic were not carried across; insurance wording stays neutral. The Cherry application link was verified from the old practice widget. The published accessibility statement and front-desk email were preserved.

Build-only open items: approved legal-policy content for the four unresolved legal paths, deferred author/reviewer details, final phone ownership and insurance wording, and the team's form delivery/access test. Tracking accounts/conversions, authority sign-off, and Jordan handoff remain separate launch work.

## November 2 historical blog restoration

Bryan explicitly requested restoring all historical articles now and deferring author/reviewing-doctor details. This is a scoped exception to the attribution-before-publication gate, recorded in `AGENTS.md`; it does not waive other launch gates.

- All 50 posts from the saved WordPress post sitemap were recovered. The later cleanup below consolidates one duplicate, leaving 49 in `src/data/blog-posts.json`. Their original article text, titles, dates, categories, tags, and agency/admin publishing credits are retained. No new medical advice, doctor attribution, or review claims were generated. Original in-body signatures remain intact. BlogPosting structured data records `creditText`; individual `author`/`reviewedBy` fields remain omitted until attribution is confirmed.
- The `/blog/` index and remaining category/tag archives use ten articles per page, pagination, related articles, and newer/older navigation. Every published article has archive and article links leading to it. Shared header/footer links expose the index throughout the site. The six duplicate-only category/tag addresses redirect to cosmetic dentistry.
- Fifty optimized public image files are local in `public/images/blog/`: 48 recovered from the supplied WordPress backup and two original public inline images. Every inline image was recovered. The latest clear-aligner article's unavailable cover was replaced with the existing March 2026 clear-aligner photo; its text is complete. Four other posts originally had no cover. Repeated cover/inline images are displayed once in the article.
- Removed obsolete Fusion Builder layout shortcodes from one 2018 post; retained its article text. Four broken service links inside old posts point to the corresponding existing service pages. No blanket redirects or DNS changes were made.
- The mis-titled cosmetic article duplicated the benefits article in both the saved HTML and the backup's post/revision. Its original source remains archived; its URL now redirects to the matching cosmetic service as described below. No replacement medical copy was invented.
- `scripts/import-legacy-blog.py` regenerates the public data from ignored source snapshots, the ignored asset map, and tracked `src/data/blog-migration-adjustments.json`. `scripts/verify-blog-migration.py` checks the 49 published articles and 49 archive/pagination routes for body preservation, metadata, production indexability, local links/images, and inbound links. Run `npm run build` first. Private source files and verification outputs stay under ignored `outputs/launch-2026-11-02/blog-migration/`.

This restoration completes the historical blog portion; legal content and the other recorded migration/launch items remain open.

## November 2 legacy URL and blog cleanup

Bryan authorized fixing the remaining old URLs and both blog issues while deferring privacy, author details and anything requiring client confirmation.

- The old cosmetic advertising page redirects to `/services/cosmetic-dentistry-milwaukee/`; the old implant advertising page redirects to `/services/dental-implants-milwaukee/`. Their two confirmation URLs redirect to the existing `/thank-you/` page. Ads, forms and tracking configuration were not changed and no submission was performed.
- `/covid-19-response/` preserves the original office notice with its May 2020 publication and May 2022 update dates. A prominent archive notice directs patients to contact the practice for current instructions. The historical protocol text is not presented as newly confirmed practice policy. Office and first-appointment pages link to it, and it links to those pages and contact.
- The incorrect cosmetic-blog URL redirects to the existing cosmetic service, matching the URL/title's topic. Its benefits text is still available in the original benefits post. Its six now-empty topic archives also redirect to that service. Blog lists and sitemap omit the consolidated duplicate; there are 49 distinct published articles, with all 50 original article addresses resolving through a page or matching redirect.
- The saved internal-link crawl contained 200 extra numbered article addresses (`/<article>/2/` through `/5/`). Their saved bodies were compared with the parent articles and all matched; their old canonical tags also named those parents. Exact redirects now lead directly to the canonical article (or the cosmetic service for the consolidated duplicate), without redirect chains. Four additional old service aliases now reach their matching built services. Genuine `/blog/page/…` and category pagination is preserved. A single malformed quoted Yomi URL in the old crawl is recorded as a parsing/link artifact, not a legitimate missing content page.
- The replacement cover reuses `/images/blog/uploads--2026--03--shutterstock_2684758523-3.webp`, already published on the client's clear-aligner article. It is a replacement, not a claimed recovery of the missing October image.
- Saved Terms, Disclaimer and EULA pages contain headings and third-party policy embeds, but no usable approved policy text. Those paths stay deferred with Privacy; no policy was fabricated or silently redirected to an unrelated page.
- Verification and source decisions are kept privately in ignored `outputs/launch-2026-11-02/legacy-cleanup/`. All noindex, DNS, analytics and existing form settings remain unchanged.

## November 3 production indexing

Bryan explicitly authorized enabling search indexing for the live site and submitting `https://www.midtowndentalcare.org/sitemap.xml` in the verified URL-prefix Search Console property. This is a scoped exception to the earlier production indexing hold; it is not completion of all client or launch gates.

- Production content HTML has no blocking robots meta tag; robots.txt permits crawling and references the 141-URL canonical sitemap. Existing content redirect destinations remain unchanged. Five old WordPress XML sitemap addresses redirect to `/sitemap.xml`, preserving Google’s saved sitemap locations (438 exact redirect rules total).
- The form completion and 404 documents retain noindex. Both the primary Pages preview and branch/deployment preview hosts receive `X-Robots-Tag: noindex, nofollow` via hostname-specific Cloudflare rules. Their robots.txt permits crawling so search engines can see the noindex headers.
- The Google verification tag stays in the homepage head. Social preview images use the production origin.
- Deployment checks and the Search Console submission/inspection results are recorded privately in `outputs/launch-2026-11-03/indexing/`. Sitemap submission and indexing requests are not proof that Google has indexed the new build.
## November 3 photo and technology updates

Bryan reviewed the refinement preview and explicitly authorized committing and pushing these updates to main for deployment on November 3. The homepage comfort section uses the supplied family lifestyle image, the office gallery has the salt container removed, and the technology page describes NOMAD, TRIOS, SprintRay, Pearl and CEREC while retaining existing CT/Yomi/laser topics and section anchors. See `docs/refinements-2026-11-03.md` for sources and review boundaries. These changes do not close the separate legal, clinical-review, insurance, ownership or tracking follow-ups.
