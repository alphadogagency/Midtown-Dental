# MidTown Dental Care

Homepage redesign for Dr. Laura Russell’s Wauwatosa practice. Built in Astro with static output for Cloudflare. All photos and the logo are served locally; fonts are bundled locally.

## Development

Requires Node 22.12 or later.

```sh
npm install
npm run dev
npm run build
npm run preview
```

Use the local URL printed by Astro. The production build is written to `dist/`.

## Cloudflare

For Cloudflare Pages, set the build command to `npm run build` and the output directory to `dist`. The Node version must be 22.12 or newer. No server adapter, database, secrets, or environment variables are required.

This is a homepage preview. Existing service and provider links lead to the current Midtown website until the inner pages are rebuilt. No production domain or DNS changes have been made.

## Appointment form

The appointment section (`#appointment`) currently offers working click-to-call links. When Bryan supplies the Jotform, embed that exact form here and update the section layout as needed. Do not create an imitation form or claim submissions have been sent.

## Content sources and launch checks

- Client design direction: Laura’s September 28, 2026 “Comp Sites” email; a balance between Emily Stout DDS and 816 Med Spa, modern and family-friendly.
- Copy source: https://www.midtowndentalcare.org/ and its provider, office, services, and patient information pages, checked October 7, 2026.
- Photos and logo: existing Midtown website; no generated people, office scenes, or new branding.
- Patient quote: Bonnie H., as published on the existing site, linked to the practice’s Google reviews.
- Confirm provider roster, phone numbers, hours, financing, and clinical details with the practice before launch.
- The existing logo is 318 × 111 pixels. Replace with a higher-resolution or vector original if supplied.
- The handoff WordPress backup is available in Drive; it has not been restored or extracted.
- Add the supplied Jotform and verify submission delivery before enabling online appointment requests.
- Update service/provider URLs to local routes as additional pages are built; preserve old URLs or add redirects at migration.
- Preview index protection is configured in `public/robots.txt` and `public/_headers`; remove noindex rules for the approved production launch.
