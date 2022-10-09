import { defineStore } from "pinia";
import { API, QpInitStore } from "@/plugins/store/index";

const initState = {
    "rat": null,
    "id": null,
    "username": null,
    "email": null,
    "last": new Date().getTime()
}

export const QpStoreUser = defineStore("storeUser", {
    state: () => { return QpInitStore("user", initState) },
    actions: {
        updateLast () {
            this.last = new Date().getTime()
        },
        updateRat (payload) {
            this.rat = payload
        },
        cleanUser () {
            Object.keys(initState).forEach((key) => {
                this[key] = initState[key]
            })
            this.updateUser()
        },
        async updateUser () {
            if (this.rat) {
                let f = await fetch(`${API}/me/`, {
                    method: "GET",
                    headers: new Headers({"Authorization": `Token ${this.rat}`})
                })
                if (f.status === 200) {
                    let r = await f.json()
                    console.log(r)
                    this.updateLast()
                    return r
                } else if (f.status === 401) {
                    this.cleanUser()
                }
            }
        }
    }
})
