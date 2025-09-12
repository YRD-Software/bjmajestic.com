import type { CollectionConfig } from 'payload'

import { anyone } from '@/access/anyone'
import { authenticated } from '@/access/authenticated'
import { savePdfPreview } from './hooks/savePdfPreview'

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
    {
      name: 'thumbnail',
      type: 'upload',
      relationTo: 'media',
      required: false,
    },
  ],
  upload: {
    staticDir: 'catalog',
    disableLocalStorage: true,
    crop: false,
    pasteURL: false,
    mimeTypes: ['application/pdf'],
  },
  hooks: {
    beforeOperation: [savePdfPreview]
  }
}
