import { defineStore } from "pinia";
import { QpInitStore } from "./index";

const initState = {
    "playername": "Unknown",
    "last": new Date().getTime()
}

export const QpStorePlayer = defineStore("storePlayer", {
    state: () => { return QpInitStore("player", initState) },
    actions: {
        updateLast() {
            this.last = new Date().getTime()
        }
    }
})
