// import { Media } from '@/payload-types'
import { type CollectionBeforeOperationHook } from 'payload'
// import { fromBuffer } from 'pdf2pic'
// import { pdf } from 'pdf-to-img'

import { promises } from 'node:fs'

export const savePdfPreview: CollectionBeforeOperationHook = async ({ operation, req }) => {
  if (operation === 'create' || operation === 'update') {
    const { file } = req

    if (file && file.mimetype === 'application/pdf') {
      // Convert first page of PDF buffer to image

      // const document = await pdf(file.data, {
      //   scale: 2,
      // })

      // const preview = await document.getPage(1)

      // await promises.writeFile(`./pdfPreview-${file.name}.jpeg`, preview)
      
      // const options = {
      //   density: 100,
      //   format: 'jpeg',
      //   width: 600,
      //   height: 800,
      //   savePath: './media',
      //   saveFilename: `pdfPreview-${file.name}`,
      // }

      // const convert = fromBuffer(file.data, options)

      // convert(1, {responseType: 'image'})

      // convert(1, { responseType: 'buffer' }).then((result) => {
      //   try {
      //     if (!result.buffer) {
      //       throw new Error('Failed to generate image buffer from PDF.')
      //     }

      //     const imageFile: File = {
      //       name: `pdfPreview-${file.name}.jpeg`,
      //       data: result.buffer,
      //       mimetype: 'image/jpeg',
      //       size: result.buffer.length,
      //     }

      //     const imageFileMedia: Media = {
      //       id: new Date().getTime(),
      //       createdAt: new Date().toString(),
      //       updatedAt: new Date().toString(),
      //       filename: imageFile.name,
      //       alt: `Preview of ${file.name}`,
      //       mimeType: imageFile.mimetype,
      //     }

      //     req.payload.create({
      //       collection: 'media',
      //       data: imageFileMedia,
      //       file: imageFile,
      //     })
      //   } catch (err) {
      //     console.error('Error generating PDF preview image:', err)
      //   }
      // })
    }
  }
}
