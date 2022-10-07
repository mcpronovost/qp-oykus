import { defineStore } from "pinia";
import { QpInitStore } from "./index";

const initState = {
    "theme": "dark",
    "isSidenavShow": true,
    "isSideviewShow": true,
    "mainviewWidth": 1200
}

export const QpStoreApp = defineStore("storeApp", {
    state: () => { return QpInitStore("app", initState) },
    actions: {
        toggleTheme() {
            this.theme = (this.theme == "dark" ? "light" : "dark")
        },
        toggleSidenavShow() {
            this.isSidenavShow = !this.isSidenavShow
        },
        toggleSideviewShow() {
            this.isSideviewShow = !this.isSideviewShow
        },
        setMainviewWidth(payload) {
            this.mainviewWidth = payload
        }
    }
})
