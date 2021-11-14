import Axios from 'axios'
import { getFileSize } from '../helpers/file'

const instance = Axios.create({
  baseURL: '__API_BASE__',
})

export async function getCompressedImage (file, rate) {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('rate', rate)

  const response = await instance.post(
    '/compress',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: 'blob',
    }
  )

  return {
    file: response.data,
    time: response.headers['compress-time'],
  }
}
