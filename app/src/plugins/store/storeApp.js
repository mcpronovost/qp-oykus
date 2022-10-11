import { defineStore } from "pinia";
import { QpInitStore } from "./index";

const initState = {
    "isLoading": false,
    "theme": "dark",
    "isSidenavShow": true,
    "isSideviewShow": true,
    "mainviewWidth": 1200
}

export const QpStoreApp = defineStore("storeApp", {
    state: () => { return QpInitStore("app", initState) },
    actions: {
        updateIsLoading (payload) {
            this.$patch((state) => {
                state.isLoading = payload
            })
        },
        updateMainviewWidth(payload) {
            this.$patch((state) => {
                state.mainviewWidth = payload
            })
        },
        toggleSidenavShow() {
            this.$patch((state) => {
                state.isSidenavShow = !state.isSidenavShow
            })
        },
        toggleSideviewShow() {
            this.$patch((state) => {
                state.isSideviewShow = !state.isSideviewShow
            })
        }
    }
})
