import { defineConfig } from 'vite'
import { resolve, dirname } from 'path'
import { fileURLToPath } from 'url'
import tailwindcss from '@tailwindcss/vite'
import { viteStaticCopy } from 'vite-plugin-static-copy'

const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineConfig({
  build: {
    outDir: '../backend/app/static',
    emptyOutDir: true,
    cssCodeSplit: false,
    rollupOptions: {
      input: resolve(__dirname, 'src/main.ts'),
      output: {
        entryFileNames: 'main.js',
        assetFileNames: 'css/app.css',
        format: 'iife',
      },
    },
  },
  plugins: [
    tailwindcss(),
    viteStaticCopy({
      targets: [
        {
          src: 'node_modules/htmx.org/dist/htmx.min.js',
          dest: 'js',
        },
        {
          src: 'node_modules/htmx.org/dist/ext/json-enc.js',
          dest: 'js/ext',
        },
        {
          src: 'node_modules/htmx.org/dist/ext/alpine-morph.js',
          dest: 'js/ext',
        },
      ],
    }),
  ],
})
