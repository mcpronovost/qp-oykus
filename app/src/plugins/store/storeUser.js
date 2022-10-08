import { defineStore } from "pinia";
import { API, QpInitStore } from "@/plugins/store/index";

const initState = {
    "id": null,
    "username": null,
    "email": null,
    "rat": null,
    "last": new Date().getTime()
}

export const QpStoreUser = defineStore("storeUser", {
    state: () => { return QpInitStore("user", initState) },
    actions: {
        updateLast() {
            this.last = new Date().getTime()
        },
        async updateUser () {
            let f = await fetch(`${API}/`, {
                method: "GET"
            })
            if (f.status === 200) {
                let r = await f.json()
                console.log(r)
                this.updateLast()
                return r
            }
        },
        async doRegister (username, name, email, password) {
            let data = new FormData()
            if (username) data.append("username", username)
            if (name) data.append("name", name)
            if (email) data.append("email", email)
            if (password) data.append("password", password)
            let f = await fetch(`${API}/register/`, {
                method: "POST",
                body: data
            })
            if (f.status === 200) {
                let r = await f.json()
                console.log(r)
            }
        }
    }
})
