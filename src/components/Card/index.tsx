'use client'
import { cn } from '@/utilities/ui'
import useClickableCard from '@/utilities/useClickableCard'
import Link from 'next/link'
import React, { Fragment } from 'react'
import dynamic from 'next/dynamic'

import type { Post, Media as MediaType } from '@/payload-types'

import { Media } from '@/components/Media'

// Dynamically import react-pdf to prevent SSR issues
const Document = dynamic(() => import('react-pdf').then((mod) => ({ default: mod.Document })), {
  ssr: false,
  loading: () => <div className="animate-pulse bg-gray-200 h-48 w-full rounded"></div>,
})
const Page = dynamic(() => import('react-pdf').then((mod) => ({ default: mod.Page })), {
  ssr: false,
})

export type CardPostData = Pick<Post, 'slug' | 'categories' | 'meta' | 'title'>

// Setup PDF.js worker - this will only run on client side
if (typeof window !== 'undefined') {
  import('react-pdf').then(({ pdfjs }) => {
    pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.js'
  })
}

const options = {
  cMapUrl: '/cmaps/',
  standardFontDataUrl: '/standard_fonts/',
}

export const Card: React.FC<{
  alignItems?: 'center'
  className?: string
  doc?: CardPostData
  relationTo?: 'posts'
  showCategories?: boolean
  title?: string
  href?: string | null
  mimeType?: string | null
  thumbnail?: MediaType | number | null
}> = (props) => {
  const { card, link } = useClickableCard({})
  const {
    className,
    doc,
    relationTo,
    showCategories,
    title: titleFromProps,
    href,
    mimeType,
    thumbnail,
  } = props

  const { slug, categories, meta, title } = doc || {}
  const { description, image: metaImage } = meta || {}

  const hasCategories = categories && Array.isArray(categories) && categories.length > 0
  const titleToUse = titleFromProps || title
  const sanitizedDescription = description?.replace(/\s/g, ' ') // replace non-breaking space with white space

  // Use href from props if provided, otherwise fallback
  const hrefToUse = href || `/${relationTo}/${slug}`

  return (
    <article
      className={cn(
        'border border-border rounded-lg overflow-hidden bg-card hover:cursor-pointer',
        className,
      )}
      ref={card.ref}
    >
      <div className="relative">
        {!metaImage && !thumbnail && !mimeType && <div className="">No image</div>}
        {mimeType !== 'application/pdf' && metaImage && typeof metaImage !== 'string' && (
          <Media resource={metaImage} size="33vw" />
        )}
        {mimeType === 'application/pdf' && (
            <Document file={hrefToUse} options={options}>
            <Page
              pageNumber={1}
              height={350}
              renderTextLayer={false}
              renderAnnotationLayer={false}
              className="w-full h-full flex items-center justify-center overflow-hidden"
            />
          </Document>
        )}
      </div>
      <div className="p-4">
        {showCategories && hasCategories && (
          <div className="uppercase text-sm mb-4">
            {showCategories && hasCategories && (
              <div>
                {categories?.map((category, index) => {
                  if (typeof category === 'object') {
                    const { title: titleFromCategory } = category

                    const categoryTitle = titleFromCategory || 'Untitled category'

                    const isLast = index === categories.length - 1

                    return (
                      <Fragment key={index}>
                        {categoryTitle}
                        {!isLast && <Fragment>, &nbsp;</Fragment>}
                      </Fragment>
                    )
                  }

                  return null
                })}
              </div>
            )}
          </div>
        )}
        {titleToUse && (
          <div className="prose">
            <h3>
              <Link className="not-prose" href={hrefToUse} ref={link.ref}>
                {titleToUse}
              </Link>
            </h3>
          </div>
        )}
        {description && <div className="mt-2">{description && <p>{sanitizedDescription}</p>}</div>}
      </div>
    </article>
  )
}
