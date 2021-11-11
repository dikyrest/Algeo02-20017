/**
 * @returns {import('vite').Plugin}
 */
export default function replace() {
  let config

  return {
    name: 'vite-replace',

    configResolved(resolvedConfig) {
      config = resolvedConfig
    },

    resolveId(id) {
      if (id.includes('api.js')) {
        return id
      }
    },

    transform(code, _) {
      if (config.command === 'serve') {
        code = code.replace('__API_BASE__', process.env.DEV_API_BASE)
      } else {
        code = code.replace('__API_BASE__', process.env.API_BASE)
      }

      return code
    }
  }
}
