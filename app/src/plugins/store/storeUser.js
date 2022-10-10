import { defineStore } from "pinia";
import { API, QpInitStore } from "@/plugins/store/index";

const initState = {
    "rat": null,
    "id": null,
    "username": null,
    "email": null,
    "name": null,
    "owned_projects": [],
    "last": new Date().getTime()
}

export const QpStoreUser = defineStore("storeUser", {
    state: () => { return QpInitStore("user", initState) },
    actions: {
        updateLast () {
            this.$patch((state) => {
                state.last = new Date().getTime()
            })
        },
        updateRat (payload) {
            this.$patch((state) => {
                state.rat = payload
            })
        },
        cleanUser () {
            this.$patch((state) => {
                Object.keys(initState).forEach((key) => {
                    state[key] = initState[key]
                })
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
                    this.$patch((state) => {
                        state.id = r.id
                        state.username = r.username
                        state.email = r.email
                        state.name = r.name
                        state.owned_projects = r.owned_projects
                    })
                    this.updateLast()
                    return r
                } else if (f.status === 401) {
                    this.cleanUser()
                }
            }
        }
    }
})
