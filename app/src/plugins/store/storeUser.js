import { defineStore } from "pinia";
import i18n from "@/plugins/i18n";
import { API, QpStoreHeaders, QpInitStore } from "@/plugins/store/index";

const initState = {
    "rat": null,
    "id": null,
    "username": null,
    "email": null,
    "name": null,
    "avatar": null,
    "owned_projects": [],
    "notifications": [],
    "lang": "fr",
    "last": new Date().getTime()
}

export const QpStoreUser = defineStore("storeUser", {
    state: () => { return QpInitStore("user", initState) },
    actions: {
        updateRat (payload) {
            this.$patch((state) => {
                state.rat = payload
            })
        },
        updateLang (payload) {
            this.$patch((state) => {
                state.lang = payload
                i18n.global.locale.value = payload
                document.documentElement.setAttribute("lang", payload)
            })
        },
        updateLast () {
            this.$patch((state) => {
                state.last = new Date().getTime()
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
                    headers: QpStoreHeaders(this.rat, this.lang)
                })
                if (f.status === 200) {
                    let r = await f.json()
                    this.$patch((state) => {
                        state.id = r.id
                        state.username = r.username
                        state.email = r.email
                        state.name = r.name
                        state.avatar = r.avatar
                        state.owned_projects = r.owned_projects
                        state.notifications = r.notifications
                    })
                    this.updateLang(r.lang)
                    this.updateLast()
                    return r
                } else if (f.status === 401) {
                    this.cleanUser()
                }
            }
        }
    }
})
