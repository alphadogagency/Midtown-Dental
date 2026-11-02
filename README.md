# MidTown Dental Care

Website redesign for Dr. Laura Russell’s Wauwatosa practice. Built in Astro with static output for Cloudflare. All photos and the logo are served locally; fonts are bundled locally.

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

This remains a **staging preview**, not a complete production migration. The approved homepage and 48 other content routes are built, plus a form completion page and real 404. The expansion includes all 25 services in the directory, four dentist bios, two staff profiles, membership, financing, the real before/after gallery, accessibility information, and patient resources. Existing paths are preserved. Historical blogs/archives and legal-policy content remain open; the footer privacy link still reaches the old site.

On November 2, Bryan connected the apex production domain to Pages and then explicitly authorized a limited repair of the failing `www` hostname. The Pages wizard replaced four old `www` A/AAAA entries with `CNAME www → midtown-dental.pages.dev` and associated that hostname with this project. Both domain variants now serve this build over HTTPS. This routing repair does not complete the production migration; noindex and all remaining launch gates remain in place. The November 2 inventory contains 156 sitemap URLs plus 218 additional discovered URLs; the remaining content, authority data, and exact migration behavior must be resolved before cutover. Private source snapshots, the URL manifest, verification, and the launch handoff are kept in the ignored `outputs/launch-2026-11-02/` directory.

The static build includes a real `404.html` and a 49-URL XML sitemap (the form completion and 404 pages are excluded). `public/_redirects` repairs three broken legacy aliases to existing core routes; it is **not** a complete migration redirect map. Astro preview does not emulate Cloudflare redirect rules, so validate redirects on Pages.

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
- The handoff WordPress backup is available in Drive; it has not been restored or extracted.
- Team-owned final form check: submit a clearly labeled test, verify receipt at the confirmed front-desk inbox and secure access to details, and check the acknowledgment/thank-you redirect. No test request was sent by Codex.
- Update service/provider URLs to local routes as additional pages are built; preserve old URLs or add redirects at migration.
- Preview index protection is configured in `public/robots.txt`, `public/_headers`, and `src/layouts/SiteLayout.astro`. Keep all three until the complete migration is ready. At the approved production launch, coordinate indexability with staging retirement, add the sitemap reference to production robots.txt, and verify the actual response headers and HTML on the production domain.

## Agency standards

The user-supplied ADA web checklist and design standard were received November 2. `AGENTS.md` contains Part B and the current stage/brand guardrails. The full eight-section assessment is in the private readiness report. No checklist section is treated as complete merely because the documents are now available.

The November 2 standards pass adds a persistent mobile call/request bar, Apple touch icon, Open Graph photo, two local font preloads, and responsive WebP derivatives for all displayed practice photos. The privacy footer link currently reaches the existing production policy. That policy is rendered by Termageddon; its ownership/license and updated legal copy need review before migration, and no legacy policy script was copied.

The share-image origin in `src/layouts/SiteLayout.astro` intentionally points to the preview while staging. Change it to the final production origin before retiring Pages staging. Astro is pinned to 7.4.1 and `.node-version` pins the tested Node 22.22.2 runtime. The standards pass dependency audit reports zero vulnerabilities; this is not proof of account ownership, 2FA, form security, or backup restoration.

## November 2 page expansion

Added 29 source-backed content routes while retaining the approved design. New metadata, clinical/service copy, membership terms, historical staff roster, and gallery permissions remain subject to practice review. Obsolete PPO claims and the old 2022 membership price graphic were not carried across; insurance wording stays neutral. The Cherry application link was verified from the old practice widget. The published accessibility statement and front-desk email were preserved.

Build-only open items: approved legal-policy content (the old privacy page currently renders no policy text), real author/reviewer attribution before historical blog migration, final phone ownership and insurance wording, and the team's form delivery/access test. Domain launch, tracking accounts/conversions, authority sign-off, and Jordan handoff remain separate launch work.
