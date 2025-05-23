import React from 'react'

import configPromise from '@payload-config'
import { getPayload } from 'payload'
import Link from 'next/link'

export const CatalogArchiveBlock: React.FC<{ id?: string }> = async () => {
  const limit = 3 // TODO: Need something like: `const limit = limitFromProps || 3`

  const payload = await getPayload({ config: configPromise })

  const fetchedCatalogs = await payload.find({
    collection: 'catalog',
    depth: 1,
    limit,
  })

  return (
    <div className="my-16">
      <h1>Catalog Archive Block</h1>
      <ul>
        {fetchedCatalogs?.docs?.map((catalog) => {
          return (
            <div key={catalog.id} className="mb-4">
              <Link href={catalog.url || '#'} className="text-blue-500 hover:underline">
                {catalog.name}
              </Link>
            </div>
          )
        })}
      </ul>
    </div>
  )
}
