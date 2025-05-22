import type { CollectionConfig } from 'payload'

export const Catalog: CollectionConfig = {
  slug: 'catalog',
  fields: [
    {
      name: 'title',
      type: 'text',
      required: true,
    },
  ]
}
