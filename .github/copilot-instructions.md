# Copilot Instructions for bjmajestic.com

## Project Overview
- This is a Payload CMS + Next.js website template, tailored for content-driven sites (blogs, portfolios, etc.) with a full-featured admin panel and production-ready frontend.
- The backend (Payload) and frontend (Next.js App Router) are tightly integrated and share a single codebase.
- Key features: authentication, access control, layout builder, draft/live preview, on-demand revalidation, SEO, search, redirects, scheduled publishing, and media management.

## Key Architecture & Patterns
- **Payload config:** `src/payload.config.ts` is the central config for collections, globals, plugins, DB, email, i18n, and jobs.
- **Collections:** Defined in `src/collections/` (e.g., `Posts`, `Pages`, `Media`, `Categories`, `Users`, `Catalog`). Each collection may have custom access, hooks, and plugins.
- **Blocks:** Layout-building blocks live in `src/blocks/` and are used for flexible page/post layouts.
- **Frontend:** Next.js App Router code is in `src/app/(frontend)/`. The main layout is `layout.tsx`. Pages use SSR/SSG and dynamic routing.
- **Admin:** Payload admin UI is in `src/app/(payload)/`. Custom admin components are mapped via `importMap.js`.
- **Plugins:** All Payload plugins are registered in `src/plugins/index.ts` (SEO, redirects, search, nested docs, form builder, cloud, etc.).
- **Utilities:** Shared helpers in `src/utilities/` (e.g., URL generation, meta, debounce, etc.).

## Developer Workflows
- **Local dev:**
  - `pnpm install && pnpm dev` (starts both Payload and Next.js frontend)
  - Visit `http://localhost:3000` for the site and admin panel
- **Database:**
  - Uses Postgres (Vercel adapter by default). Migrations: `pnpm payload migrate:create` (create), `pnpm payload migrate` (run)
- **Production build:**
  - `pnpm build` then `pnpm start` (serves production bundle)
- **Docker:**
  - `docker-compose up` for standardized local dev
- **Seeding:**
  - Use the admin panel's 'seed database' link (destructive, resets DB)

## Project-Specific Conventions
- **TypeScript everywhere** (including Payload config, collections, frontend)
- **Custom blocks/components:** Add new layout blocks in `src/blocks/` and register in collections as needed
- **Access control:** See `src/access/` for reusable access functions (e.g., `authenticated`, `anyone`)
- **Hooks:** Custom hooks in `src/hooks/` (e.g., for revalidation, slug formatting)
- **Plugins:** Extend via `src/plugins/index.ts`—follow existing plugin registration patterns
- **Globals:** Site-wide data (header/footer) in `src/Footer/` and `src/Header/`, registered as globals in Payload config
- **Media:** Uploads managed via Payload's media collection and Vercel Blob storage plugin
- **SEO & search:** Use official Payload plugins, configured in plugins index

## Integration Points
- **Payload plugins:** SEO, redirects, search, nested docs, form builder, cloud, Vercel Blob storage
- **Email:** Nodemailer adapter, configured via env vars in Payload config
- **i18n:** English and Simplified Chinese supported (see Payload config)
- **Analytics:** Vercel Analytics in frontend layout

## Examples
- To add a new collection: create a file in `src/collections/`, export it, and add to `collections` in `payload.config.ts`
- To add a new block: create a folder in `src/blocks/`, implement `Component.tsx` and `config.ts`, then register in relevant collections
- To add a new plugin: import and add to the `plugins` array in `src/plugins/index.ts`

## References
- Main config: `src/payload.config.ts`
- Plugins: `src/plugins/index.ts`
- Collections: `src/collections/`
- Blocks: `src/blocks/`
- Frontend: `src/app/(frontend)/`
- Admin: `src/app/(payload)/`
- Utilities: `src/utilities/`

---
For more details, see the README or ask for clarification on any unclear workflow or pattern.
