import { defineConfig } from "vite";
import path from "path";
import vue from "@vitejs/plugin-vue";

export default defineConfig(() => {
    return {
        server: {
            port: 3000
        },
        build: {
            outDir: "bundle"
        },
        css: {
            devSourcemap: true
        },
        plugins: [vue()],
        define: {
            "APP_VERSION": JSON.stringify(process.env.npm_package_version),
            "__VUE_I18N_FULL_INSTALL__": true,
            "__VUE_I18N_LEGACY_API__": false,
            "__INTLIFY_PROD_DEVTOOLS__": false
        },
        resolve: {
            alias: {
                "@": path.resolve(__dirname, "./src")
            }
        }
    }
});
