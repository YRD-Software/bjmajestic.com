import type { CollectionConfig } from 'payload'

import { anyone } from '@/access/anyone'
import { authenticated } from '@/access/authenticated'

export const Catalog: CollectionConfig = {
  slug: 'catalog',
  access: {
    create: authenticated,
    delete: authenticated,
    read: anyone,
    update: authenticated,
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
    },
  ],
  upload: {
    staticDir: 'catalog',
    disableLocalStorage: true,
    crop: false,
    pasteURL: false,
    mimeTypes: ['application/pdf'],
  },
}
