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
            "APP_VERSION": JSON.stringify(process.env.npm_package_version)
        },
        resolve: {
            alias: {
                "@": path.resolve(__dirname, "./src")
            }
        }
    }
});
