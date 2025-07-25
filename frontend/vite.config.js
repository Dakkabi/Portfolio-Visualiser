import tailwindcss from "@tailwindcss/vite";
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
    plugins: [tailwindcss(), sveltekit()],

    resolve: {
        alias: {
            '@api': path.resolve(__dirname, 'src/config/axios.config.js')
        }
    },

    server: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
                secure: false
            }
        }
    }
});
