import { type CollectionBeforeOperationHook } from 'payload'
import { pdf } from 'pdf-to-img'

export const savePdfPreview: CollectionBeforeOperationHook = async ({ operation, req }) => {
  if (operation === 'create' || operation === 'update') {
    const { file, data } = req

    // NOTE: Things `file` has
    // file?: {
    //     /**
    //      * Context of the file when it was uploaded via client side.
    //      */
    //     clientUploadContext?: unknown;
    //     data: Buffer;
    //     mimetype: string;
    //     name: string;
    //     size: number;
    //     tempFilePath?: string;
    // };

    // TODO: I need to replace the `data` with the image's buffer
    // and mimetype to jpeg
    // and name to something like `pdf-preview-{timestamp}.jpeg`
    // and size to the image buffer's length
    // and empty tempFilePath

    // Early return if no file or not a PDF
    if (!file || file.mimetype !== 'application/pdf') {
      console.log('No file or not a PDF')
      console.log('No PDF file uploaded, skipping PDF preview generation.')
      return
    }

    try {
      console.log('Starting PDF preview generation for:', file.name)

      // Convert first page of PDF buffer to image
      const document = await pdf(file.data, {
        scale: 2, // Higher scale for better quality
      })

      // Get the first page as an image
      const image = document.getPage(1)


      // const thumbnailFile = {
      //   name: `pdf-preview-${Date.now()}.jpeg`,
      //   data: imageBuffer as Buffer,
      //   mimetype: 'image/jpeg',
      //   size: imageBuffer.length,
      // }

      // console.log('Uploading thumbnail to media collection...')

      // // Upload the thumbnail to media collection
      // const thumbnail = await req.payload.create({
      //   collection: 'media',
      //   data: thumbnailData,
      //   file: thumbnailFile,
      // })

      // console.log('Thumbnail uploaded successfully, ID:', thumbnail.id)

      // // Update the catalog data to include the thumbnail
      // if (data) {
      //   data.thumbnail = thumbnail.id
      // }
    } catch (err) {
      console.error('Error generating PDF preview image:', err)
      // Continue without thumbnail - will use default image
    }
  }
}
