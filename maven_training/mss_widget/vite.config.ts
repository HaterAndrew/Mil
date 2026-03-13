import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    // Single-file output for Workshop widget embedding
    rollupOptions: {
      output: {
        manualChunks: undefined,
      },
    },
  },
})
