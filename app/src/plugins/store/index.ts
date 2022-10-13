import { createPinia } from "pinia";
import { Buffer } from "buffer";
import { QpStoreApp } from "./storeApp";
import { QpStoreUser } from "./storeUser";

export const API: string = "http://localhost:8000/api"

export const HEADERS = (rat: string|null, lang?: string) => {
    if (rat) {
        return new Headers({
            "Authorization": `Token ${rat}`,
            "Accept-Language": `${lang||"fr"}`
        })
    } else {
        return new Headers({
            "Accept-Language": `${lang||"fr"}`
        })
    }
}

export const QpInitStore = (store: string, payload: {}) => {
    if (localStorage.getItem(`qp-oykus-${store}`)) {
        try { return QpFromStore(store) } catch (e) {
            console.error(`Error on Init State > ${store} : `, e)
        }
    } else { QpToStore(store, payload) }
    return payload
}

export const QpToStore = (store: string, payload: {}) => {
    localStorage.setItem(`qp-oykus-${store}`, new Buffer(JSON.stringify(payload)).toString("base64"))
}

export const QpFromStore = (store: string): {} => {
    const stored: string|null = localStorage.getItem(`qp-oykus-${store}`)
    if (typeof stored === "string") {
        return JSON.parse(new Buffer(stored, "base64").toString("utf8"))
    }
    return {}
}

const store = createPinia();

export const storeApp = () => {
    const qpStore = QpStoreApp();
    qpStore.$subscribe((mutation, state) => { QpToStore("app", state) });
    return qpStore;
};

export const storeUser = () => {
    const qpStore = QpStoreUser();
    qpStore.$subscribe((mutation, state) => { QpToStore("user", state) });
    return qpStore;
};

export default store;
