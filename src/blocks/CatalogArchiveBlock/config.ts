import type { Block } from 'payload'

export const CatalogArchive: Block = {
  slug: 'catalogArchive',
  interfaceName: 'CatalogArchiveBlock',
  fields: [
    {
      name: 'title',
      type: 'text',
      label: 'Title',
    },
    {
      name: 'limit',
      type: 'number',
      label: 'Number of Catalogs to Show',
      defaultValue: 3,
    },
  ]
}
