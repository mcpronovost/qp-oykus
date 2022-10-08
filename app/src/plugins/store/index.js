import { createPinia } from "pinia ";
import { Buffer } from "buffer";
import { QpStoreApp } from "./storeApp";
import { QpStoreUser } from "./storeUser";

export const API = "http://localhost:8000/api"

export const QpInitStore = (store, payload) => {
    if (localStorage.getItem(`qp-oykus-${store}`)) {
        try { return QpFromStore(store) } catch (e) {
            console.log(`Error on Init State > ${state} : `, e)
        }
    } else { QpToStore(store, payload) }
    return payload
}

export const QpToStore = (store, payload) => {
    localStorage.setItem(`qp-oykus-${store}`, Buffer.from(JSON.stringify(payload)).toString("base64"))
}

export const QpFromStore = (store) => {
    return JSON.parse(Buffer.from(localStorage.getItem(`qp-oykus-${store}`), "base64").toString("utf8"))
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
