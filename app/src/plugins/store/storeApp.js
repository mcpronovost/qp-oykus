import { defineStore } from "pinia";
import { QpInitStore } from "./index";

const initState = {
    "theme": "dark",
    "sideview-open": true
}

export const QpStoreApp = defineStore("storeApp", {
    state: () => { return QpInitStore("app", initState) },
    actions: {
        toggleTheme() {
            this.theme = (this.theme == "dark" ? "light" : "dark")
        }
    }
})
