import pages from '../data/core-pages.json';
import { practice } from '../data/practice';

export function GET() {
  const urls = ['/', ...pages.map(page => `/${page.path}/`)];
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(path => `  <url><loc>${practice.site}${path}</loc></url>`).join('\n')}\n</urlset>`,
    { headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
  );
}
