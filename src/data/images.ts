import treatment from '../assets/images/office-treatment.jpg';
import laura from '../assets/images/laura-russell.jpg';
import annmarie from '../assets/images/annmarie-hoyme.jpg';
import karla from '../assets/images/karla-schmidt.jpg';
import mark from '../assets/images/mark-crego.jpg';
import larita from '../assets/images/larita.jpg';
import cathy from '../assets/images/cathy-harmatys.jpg';
import type { ImageMetadata } from 'astro';

export const practiceImages: Record<string, ImageMetadata> = {
  'office-treatment.jpg': treatment,
  'laura-russell.jpg': laura,
  'annmarie-hoyme.jpg': annmarie,
  'karla-schmidt.jpg': karla,
  'mark-crego.jpg': mark,
  'larita.jpg': larita,
  'cathy-harmatys.jpg': cathy,
};
