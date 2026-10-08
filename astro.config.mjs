import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://www.midtowndentalcare.org',
  output: 'static',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
