export const getFileSize = (blob) => {
  if (!blob) {
    return ''
  }

  const units = ['B', 'KB', 'MB', 'GB', 'TB']

  let size = blob.size
  let order = 0;
  while (size >= 1024 && order < units.length - 1)
  {
    order++
    size /= 1024
  }

  return `${size.toFixed(3)} ${units[order]}`
}
