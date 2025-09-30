import { MigrateUpArgs, MigrateDownArgs, sql } from '@payloadcms/db-vercel-postgres'

export async function up({ db, payload, req }: MigrateUpArgs): Promise<void> {
  await db.execute(sql`
   ALTER TABLE "pages_blocks_catalog_archive" DROP COLUMN IF EXISTS "title";
  ALTER TABLE "_pages_v_blocks_catalog_archive" DROP COLUMN IF EXISTS "title";`)
}

export async function down({ db, payload, req }: MigrateDownArgs): Promise<void> {
  await db.execute(sql`
   ALTER TABLE "pages_blocks_catalog_archive" ADD COLUMN "title" varchar;
  ALTER TABLE "_pages_v_blocks_catalog_archive" ADD COLUMN "title" varchar;`)
}
