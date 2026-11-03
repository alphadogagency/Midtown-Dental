# MidTown Dental Care project rules

## Current scope and fixed guardrails

- November 2 blog exception: Bryan explicitly authorized recreating all 50 historical articles now and deferring individual author/reviewing-doctor details. Preserve original publishing credits (Brew City Marketing / Gargle Admin); do not invent doctor authorship, review, or bios. This overrides the attribution-before-publication gate for this historical restoration only. Other migration, indexing, legal, tracking and form gates remain unchanged.

- The original request was homepage-first, followed by Bryan's request to finish the remaining pages. His November 2 question about whether the site began as one page was a question, not a new scope restriction. Do not treat it as authorization to omit migration work or as confirmation of a one-page-only engagement.
- Existing Astro/Cloudflare project for Dr. Laura Russell in Wauwatosa, WI. Preserve the approved October homepage, green/cream palette, Instrument Serif/DM Sans, real logo/photos, and edited waiting-room images.
- This is a staged core-page build, not a completed production migration. Do not change DNS, remove noindex, retire staging, enable ads, or declare launch complete while the migration, ownership, form and tracking gates remain open.
- The selected design direction has already been approved. Routine readiness fixes operate in Deliver; do not restart Discover/Define or introduce alternate homepage designs unless Bryan explicitly asks.
- Source facts only. No invented credentials, memberships, reviews, insurance acceptance, office locations, phone ownership, successful form submissions, or analytics results.
- Preserve old paths and protected content. Complete the URL/authority manifest and required sign-off before cutover. Do not replace unbuilt pages with blanket homepage redirects.
- Phone ownership and final insurance wording are explicitly left open by Bryan. No online scheduling at launch. Use the real Jotform only after its recipient and protections are established; never an imitation form.
- Read README.md for current implementation details. The private readiness report and manifests are in ignored outputs/launch-2026-11-02/. Never commit those private source snapshots or handoffs.
- Build with npm run build; inspect changed desktop/mobile routes and affected flows. Cloudflare redirect/header behavior must be tested on Pages. Do not treat browser viewport checks as physical iPhone/Android tests.
- No external stakeholder messages or ads actions are authorized by these files. Preserve any shared browser/account-control reservation from the coordinator.

## ADA design standard, version 1.1 (October 2026)

The following Part B is reproduced from the user-supplied ADA design standard. Its fixed-constraint rule applies to the approved design and current delivery stage above. Receipt of this file does not retroactively certify a critic score or human sign-off.

# PART B: Agent instructions (paste into CLAUDE.md / AGENTS.md)

You are building a visual deliverable for an Alpha Dog Agency client. Follow this standard.

## Operating principle

Your defaults produce generic output. Do not trust your first instinct on palette, layout, type or copy. Work in three stages in order: Discover, Define, Deliver. Do not polish before there is a distinct direction.

## Fixed constraints always win

Anything listed under "Brand guardrails" in the brief (logo, required colors, required copy, legal or compliance items, native platform conventions) is non-negotiable. Every technique below operates inside those guardrails, never against them.

## Stage 1: Discover

### Technique 1: Seed strings

You cannot generate randomness internally. When told to "be unique" you produce the same three ideas every time. Get variety from outside.

1. Generate a long random alphanumeric string with a shell command. Do not invent one.
2. Mine the string for inspiration: repeated characters, digit runs, letter clusters, anything that suggests a mood, era, material, palette or layout logic.
3. Write a short creative direction from that inspiration (palette, typography, layout, texture, motion).
4. Build from that direction and make it look good.
5. Never surface the string anywhere in the output.

When exploring, run 3 to 4 instances in parallel. If two results look alike, the seed was ignored. Redo.

### Technique 2: Ambitious, specific briefs

A brief that names an outside reference and says how it should bend the design gives you something to commit to. A brief that says "modern and clean" gives you nothing.

Brief structure:
- Deliverable
- Brand guardrails (fixed)
- Reference: a game genre, art movement, architectural style, physical object or era
- Constraint: how that reference must shape the functional layout, not just decorate it
- Permission to break rules, with the requirement that it still works and still looks good

When asked to help find a direction:
1. List many candidate design languages with one-line descriptions. Breadth, not depth.
2. Wait for the human to pick favorites and react in their own words. Sharpen from their reaction, not your defaults.
3. Repeat until they are satisfied, then write a tight build prompt for a proof-of-concept.

Attempt ideas that sound like they will fail. Discard freely. Log prompts that did not work (see prompt log) so they can be retried on newer models.

## Stage 2: Define

### Technique 3: Critic loop

You cannot judge your own work objectively. You remember the code and the effort. Hand evaluation to a separate critic.

Per iteration:
1. Screenshot the current state.
2. Invoke the critic (a stronger model) in a fresh context with the screenshot only. No code, no notes, no prior critiques.
3. The critic identifies the aesthetic being attempted, imagines how a top studio would execute that aesthetic, lists the biggest gaps and returns a score out of 10.
4. Address the gaps. Repeat.

Critic prompt requirements (use the identical prompt every iteration):
- Evaluate composition and structure first, then fine detail.
- Hunt for overdone, excessive or obviously AI-generated patterns and penalize them.
- Feedback must be specific and actionable.
- Be opinionated. Safe is not the goal.
- When reference images are supplied, treat them as a baseline for quality, never as something to copy.

Stopping rule: done when the critic independently scores 9/10 or higher. Do not tell the critic the threshold. Cap at two iterations first, check for convergence, then extend if warranted. Never run an uncapped loop.

Best-case critic setup: four professional examples plus our screenshot, ranked by polish and taste. Use this whenever the team can supply references.

### Technique 4: Real imagery instead of drawn decoration

Code-drawn gradients, blobs and geometric patterns are a loud AI tell. Use image generation whenever a design feels flat. Combine with shaders or 3D effects where appropriate. Verify the result in the browser.

Access (in order of preference for ADA):
1. Built-in image generation if your agent has it. Use it without being told twice.
2. Codex CLI billed to a ChatGPT subscription.
3. A dedicated OpenAI or Gemini API key.

Key hygiene, no exceptions:
- Keys live in a gitignored `.env.agents` file, referenced from `CLAUDE.md` with a note that they are for development only.
- Dedicated key per project or per agent, tight spend cap, revocable without collateral damage.
- Never write a key into source. Never ship one with the product.

### Technique 5: Video for motion

Use an aggregator (fal.ai or similar) so one key covers many models and you can pick the current best.

Looping graphics:
1. Generate a short loop on a solid-color background.
2. Remove the background (chroma key, or a video matting model for complex subjects).
3. Layer it into the UI so it reads as a living element, not an embedded video.
4. For glass, refraction or light effects, render over the page's real background colors first so the optics are baked in, then matte.

State transitions:
1. Generate a still for state A.
2. Generate a clip from that still to state B.
3. Seed the next clip from the final frame so the chain is seamless.
4. Play on user action, or scrub frame by frame on scroll or swipe.
5. Prefer a video model known for physical consistency.

Use motion only where it serves the page. A dental practice homepage does not need a splintering crystal.

## Stage 3: Deliver

### Technique 6: Subtract

You add. You almost never remove. Overdecorated, overexplained screens are a primary AI tell. Restraint reads as premium.

Apply on every polish pass:
- Remove background glows, halos and decorative gradients
- Remove color or highlights on text that serve no function
- Remove labels and captions that repeat what an image or layout already says
- Remove empty containers, cards and wrappers that group nothing
- Replace custom buttons and inputs that look worse than native components
- Remove anything a user would not miss

Then tighten type (smaller, simpler, fewer weights), lean on native components and let the visuals carry the message.

You will not do this unprompted because deleting work feels risky. Treat this as a standing instruction and expect the human to push further.

### Technique 7: Remove AI tells (ADA-authored)

After subtraction, sweep for the patterns that mark a page as machine-made. Fix every one you find.

Layout tells
- Hero with headline left, graphic right, two buttons below
- Three equal feature cards in a row, each with an icon, a bold label and two lines of copy
- Every section the same height with the same centered heading
- Symmetric everything, no intentional tension anywhere
- Testimonials in a three-card carousel with star ratings

Visual tells
- Purple, indigo or teal gradient backgrounds
- Glassmorphism cards (frosted blur with a thin white border)
- Uniform large border radius on every element
- Soft drop shadows on everything
- Lucide or Heroicons line icons in colored circles
- Abstract blob or wave SVG dividers between sections
- Placeholder-style illustration of "diverse people at laptops"

Typography tells
- Inter or a system sans for everything, no contrast
- Headline sizes that step down in perfect proportion with no surprise
- Gradient text on the hero headline
- Tracking-tight headings paired with tracking-wide uppercase eyebrows on every section

Copy tells
- "Unlock", "Elevate", "Seamless", "Effortless", "Supercharge", "Transform", "Journey"
- Headline pattern of "Verb your noun" ("Grow your practice", "Simplify your workflow")
- Emoji as bullet points
- Every sentence the same length and rhythm
- Feature lists that describe the feature and never the outcome for the client's customer
- A closing CTA section titled "Ready to get started?"

Structural tells
- A FAQ section with five questions nobody asked
- Trust badges or logo rows for brands the client has no relationship with
- Stats with round numbers and no source ("10,000+ happy customers")
- Placeholder copy or lorem-adjacent phrasing that survived to production
- An About page or team section with history, credentials or stats the client never supplied
- A "best" list or comparison where the client ranks itself first
- Location pages that differ only by town name

Fix approach: do not replace one tell with a different tell. Reach back to the direction from Stage 1 and ask what that aesthetic would do here instead.

## Content and SEO rules

These apply to every page you create or edit, including edits to live sites long after launch.

- Never invent facts about the client. That covers history, founding dates, team members, credentials, awards, patient counts, reviews and stats. If you need a fact you don't have, stop and ask. An About page with invented history is worse than none.
- Every blog post or article shows an author box with the author or reviewing doctor, a one-line bio and a link to their bio page. Article markup names the same person.
- Business schema (Dentist or the most specific LocalBusiness type) lives sitewide and matches the Google Business Profile exactly. All structured data must match what's visible on the page. Don't add schema to chase AI answers, Google says no special markup is needed for AI features.
- Link every new page to at least three existing pages on related topics with descriptive anchor text, and add links to it from at least two pages that already get traffic.
- Never rank the client first in any "best" list, comparison or alternatives page on its own site. Order by the criteria stated on the page and place the client where it honestly lands.
- Never build location pages that swap the town name into the same template. Only build a location page when the brief confirms a real office or real patient base there, and write content specific to that place.
- Never generate a separate page for each wording of the same question. One strong page per real patient question.
- Use the exact words patients search for the service in the title, H1 and headings (for example "same-day crowns", not "crowns completed in one visit"). Keep those phrases intact and use them naturally, never stuffed.
- Write each section so it answers its heading in the first sentence and makes sense quoted on its own. AI answer engines cite passages, not whole pages.
- Write from what only this client knows (their approach, real cases, real pricing, office specifics). Generic advice any competitor could publish adds nothing.
- Treat AI-written titles, meta descriptions, alt text and schema like body copy. Flag them for human review before publish.
- No llms.txt or other AI-only files.

## Standing rules

- Never expose seed strings or API keys in output or source.
- Verify visual work in the browser before calling it done. Motion is verified frame by frame.
- Write every prompt that failed to the prompt log with the model name and date.
- Brand guardrails from the brief override everything in this standard.

---
