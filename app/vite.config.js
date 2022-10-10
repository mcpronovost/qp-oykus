import { defineConfig } from "vite";
import path from "path";
import vue from "@vitejs/plugin-vue";

export default defineConfig(() => {
    return {
        server: {
            port: 3000
        },
        build: {
            outDir: "../static",
            rollupOptions: {
                output: {
                    chunkFileNames: "static/assets/js/[name]-[hash].js",
                    entryFileNames: "static/assets/js/[name]-[hash].js",
                    assetFileNames: ({name}) => {
                      if (/\.(gif|jpe?g|png|svg)$/.test(name ?? "")){
                          return "static/assets/img/[name]-[hash][extname]";
                      }
                      if (/\.(woff|woff2|eot|ttf)$/.test(name ?? "")){
                          return "static/assets/font/[name]-[hash][extname]";
                      }
                      if (/\.css$/.test(name ?? "")) {
                          return "static/assets/css/[name]-[hash][extname]";   
                      }
                      return "static/assets/[name]-[hash][extname]";
                    }
                }
            }
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
