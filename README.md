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

This remains a **staging preview**, not a complete production migration. The approved homepage and 19 core routes are built: four doctor bios, seven service pages (including single-tooth implants, no-prep veneers, and pediatric dentistry), two service directories, the team directory, practice, office, first-visit, payment, and contact pages. The existing paths are preserved. Routes not yet rebuilt still link to the current client website.

No production domain or DNS changes have been made. Do not point the production domain here yet. The November 2 inventory contains 156 sitemap URLs plus 218 additional discovered URLs; the remaining content, authority data, and exact migration behavior must be resolved before cutover. Private source snapshots, the URL manifest, verification, and the launch handoff are kept in the ignored `outputs/launch-2026-11-02/` directory.

The static build includes a real `404.html` and a 20-URL XML sitemap. `public/_redirects` repairs three broken legacy aliases to existing core routes; it is **not** a complete migration redirect map. Astro preview does not emulate Cloudflare redirect rules, so validate redirects on Pages.

## Appointment form

The appointment section (`#appointment`) and `/contact/` currently offer click-to-call links. The signed-in Jotform workspace and Shared with Me search did not contain a MidTown form on November 2. The real form, recipient, spam protection, submission delivery, and conversion thank-you route remain open. Existing OperaDDS patient forms and payment links are preserved. Do not claim a request has been sent without a real successful submission.

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
- Add the supplied Jotform and verify submission delivery before enabling online appointment requests.
- Update service/provider URLs to local routes as additional pages are built; preserve old URLs or add redirects at migration.
- Preview index protection is configured in `public/robots.txt`, `public/_headers`, and `src/layouts/SiteLayout.astro`. Keep all three until the complete migration is ready. At the approved production launch, coordinate indexability with staging retirement, add the sitemap reference to production robots.txt, and verify the actual response headers and HTML on the production domain.

## Agency standards

The user-supplied ADA web checklist and design standard were received November 2. `AGENTS.md` contains Part B and the current stage/brand guardrails. The full eight-section assessment is in the private readiness report. No checklist section is treated as complete merely because the documents are now available.

The November 2 standards pass adds a persistent mobile call/request bar, Apple touch icon, Open Graph photo, two local font preloads, and responsive WebP derivatives for all displayed practice photos. The privacy footer link currently reaches the existing production policy. That policy is rendered by Termageddon; its ownership/license and updated legal copy need review before migration, and no legacy policy script was copied.

The share-image origin in `src/layouts/SiteLayout.astro` intentionally points to the preview while staging. Change it to the final production origin before retiring Pages staging. Astro is pinned to 7.4.1 and `.node-version` pins the tested Node 22.22.2 runtime. The standards pass dependency audit reports zero vulnerabilities; this is not proof of account ownership, 2FA, form security, or backup restoration.
