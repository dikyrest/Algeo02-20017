import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import dotenv from 'dotenv'
import replace from './scripts/vite/replace'

dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    replace(),
    vue(),
  ]
})
