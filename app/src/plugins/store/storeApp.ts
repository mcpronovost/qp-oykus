import type { TypeAppStore } from "./types";
import { defineStore } from "pinia";
import { QpInitStore } from "./index";

const initState = {
    "isLoading": false,
    "isSidenavShow": true,
    "isSideviewShow": true,
    "mainviewWidth": 1200
}

export const QpStoreApp = defineStore("storeApp", {
    state: () => { return QpInitStore("app", initState) as TypeAppStore },
    actions: {
        updateIsLoading (payload: boolean) {
            this.$patch((state) => {
                state.isLoading = payload
            })
        },
        updateMainviewWidth(payload: number) {
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
