import { type CollectionBeforeOperationHook } from 'payload'
import { pdf } from 'pdf-to-img'

export const savePdfPreview: CollectionBeforeOperationHook = async ({ operation, req }) => {
  if (operation === 'create' || operation === 'update') {
    const { file, data } = req

    if (file && file.mimetype === 'application/pdf') {
      try {
        console.log('Starting PDF preview generation for:', file.name)

        // Convert first page of PDF buffer to image
        const document = await pdf(file.data, {
          scale: 2, // Higher scale for better quality
        })

        // Get the first page using async iterator
        const pages = []
        for await (const page of document) {
          pages.push(page)
          if (pages.length >= 1) break // Only need first page
        }

        if (pages.length === 0) {
          throw new Error('PDF has no pages')
        }

        const imageBuffer = pages[0]

        if (!imageBuffer) {
          throw new Error('Failed to get image buffer from PDF page')
        }

        console.log('PDF conversion successful, buffer size:', imageBuffer.length)

        // Validate buffer has content
        if (imageBuffer.length === 0) {
          throw new Error('Generated image buffer is empty')
        }

        // Check for JPEG header (should start with 0xFF 0xD8)
        if (imageBuffer.length < 2 || imageBuffer[0] !== 0xff || imageBuffer[1] !== 0xd8) {
          console.warn('Generated buffer does not appear to be a valid JPEG')
          throw new Error('Generated image does not appear to be a valid JPEG file')
        }

        // Create media item for the thumbnail
        const thumbnailData = {
          alt: `Preview of ${file.name}`,
        }

        const thumbnailFile = {
          name: `pdf-preview-${Date.now()}.jpeg`,
          data: imageBuffer as Buffer,
          mimetype: 'image/jpeg',
          size: imageBuffer.length,
        }

        console.log('Uploading thumbnail to media collection...')

        // Upload the thumbnail to media collection
        const thumbnail = await req.payload.create({
          collection: 'media',
          data: thumbnailData,
          file: thumbnailFile,
        })

        console.log('Thumbnail uploaded successfully, ID:', thumbnail.id)

        // Update the catalog data to include the thumbnail
        if (data) {
          data.thumbnail = thumbnail.id
        }
      } catch (err) {
        console.error('Error generating PDF preview image:', err)
        // Continue without thumbnail - will use default image
      }
    }
  }
}
