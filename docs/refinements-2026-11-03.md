# November 3 photo and dental-technology refinements

Status: prepared for human review before production publication. This is a scoped update to the approved site, not a new homepage approval cycle.

## Images

- The homepage comfort section uses the client-supplied `mom and young daughter with nice teeth.jpg`, stored as `src/assets/images/family-at-home.jpg`. The photo is presented as lifestyle imagery, without identifying the people as patients or testimonial subjects. Alt: “A young girl kisses a smiling woman on the cheek.” The office-photo label was removed because the replacement does not depict the practice.
- The office gallery uses `src/assets/images/office-lounge-clean.png`, edited from the previous table/books-removed photograph. Only the salt container was requested for this pass. The previous image and original photograph remain preserved.
- Displayed waiting-room images were inventoried across generated HTML. They use the already-cleaned reception image and the newly cleaned lounge image; the older supplied lobby photos are not displayed. The salt container is obscured by chairs in the wide reception photograph; the blue container visible beside the ottomans is a different object and was left unchanged.

Image edit prompt (built-in ImageGen, 2026-11-03):

> Use case: precise-object-edit. Edit the supplied existing dental-office photograph, not a new composition. Remove ONLY the white rectangular salt container/bucket standing on the tiled hearth at the lower-right corner of the fireplace (approximately x=414–522, y=719–893 in the 1536×1024 input). Reconstruct the small area of tan fireplace tile and hearth behind/under that container using the adjacent tile, matching grout lines, perspective, texture, daylight and shadows. There must be no replacement object. Preserve every other part of this photograph as closely as possible: camera angle, exact framing and landscape aspect ratio, fireplace, television and its displayed image, tan wall, framed smile poster, EMPTY wooden shelf, black ottomans, striped carpet, reception window, wood trim, logos/signage and existing text. The books and children's train/play table have already been removed; they must stay absent. Do not redesign, renovate or beautify the room, move furniture, change colors or exposure, add anything, crop the photograph, or alter the window lettering. Return one edited photograph without labels, border or before/after comparison.

## Technology copy — human review requested

The existing `/services/dental-technology/` route, metadata and five original section anchors are retained. The page now explains the five technologies named by the client: NOMAD, TRIOS, SprintRay, Pearl and CEREC. Existing cone beam CT, Yomi and laser-dentistry topics remain. Broad inherited promises of painless procedures, superior outcomes and universal faster treatment were replaced with bounded descriptions. No equipment model, procedure timing, material, exact practice printing indication or clinical-review credit was invented.

Manufacturer references checked November 3, 2026:

| Technology | Source and claim boundary |
| --- | --- |
| NOMAD | [DEXIS NOMAD](https://dexis.com/en-us/products/hardware/nomad-pro-3): handheld intraoral X-ray system/cordless chairside imaging. The practice's model is unspecified; no Pro 3 or model-specific performance claim appears in copy. |
| TRIOS | [3Shape scanner overview](https://www.3shape.com/en/scanners/trios): digital impressions, 3D models, treatment planning and lab collaboration. No specific scanner generation or diagnosis feature claimed. |
| SprintRay | [SprintRay design workflow](https://sprintray.com/dental-appliance-design-service/) and [night-guard workflow](https://sprintray.com/digital-dentistry/3d-printed-night-guards/): digital records/design to printed models or appliances, with material-dependent finishing. No assertion that MidTown offers every manufacturer indication. |
| Pearl | [Pearl's explanation of diagnostic responsibility](https://help.hellopearl.com/knowledge-base/does-second-opinion-make-diagnoses): AI highlights areas on radiographs; a licensed clinician makes diagnostic decisions. No performance statistic or automated-diagnosis promise. |
| CEREC | [Dentsply Sirona chairside workflow](https://www.dentsplysirona.com/en-hr/discover/discover-by-topic/by-category/restorative/chairside-workflow-for-in-office-milled-crowns.html): scan, design, mill and finish restorations; same-day crowns for suitable cases. No model or fixed appointment-duration claim. |
| Yomi | [Neocis provider FAQ](https://www.neocis.com/providers/providers-faqs/): planning and physical guidance for implant position, angle and depth, with a clinician performing the procedure. |

Practice use of the five requested systems comes from the client's requested additions. Existing CT/Yomi/laser topics come from the migrated practice page. Manufacturer information supports general function, not an independent audit of practice equipment or protocols.

Private email/source snapshots, downloaded alternates and verification artifacts are kept under ignored `outputs/refinements-2026-11-03/`. Form, DNS, tracking, indexing, legal pages and blog attribution are outside this update.
