import type { CatalogArchiveBlock as CatalogArchiveBlockProps } from '@/payload-types'

import React from 'react'
import configPromise from '@payload-config'
import { getPayload } from 'payload'

import { Card } from '@/components/Card'

export const CatalogArchiveBlock: React.FC<CatalogArchiveBlockProps & { id?: string }> = async (
  props,
) => {
  const { limit: limitFromProps } = props
  const limit = limitFromProps || 3

  const payload = await getPayload({ config: configPromise })

  const fetchedCatalogs = await payload.find({
    collection: 'catalog',
    depth: 1,
    limit,
  })

  return (
    <div className="container">
      <div className="my-16 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {fetchedCatalogs?.docs?.map((catalog) => {
          return (
            <div key={catalog.id}>
              <Card
                title={catalog.name}
                href={catalog.url}
                mimeType={catalog.mimeType}
                thumbnail={catalog.thumbnail}
              ></Card>
            </div>
          )
        })}
      </div>
    </div>
  )
}
