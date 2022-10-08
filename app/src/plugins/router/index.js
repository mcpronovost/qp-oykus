import { createRouter, createWebHistory } from "vue-router";
//import { storeUser } from "@/plugins/store";

import HomeView from "@/views/HomeView.vue";
import ErrorView from "@/views/ErrorView.vue";

const routes = [
    {
      path: "/",
      name: "Home",
      component: HomeView
    },
    /* ===--- FALLBACK ---=== */
    {
      path: "/:catchAll(.*)",
      name: "Error",
      component: ErrorView
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

router.beforeEach(async (to, from, next) => {
    //const useStoreUser = storeUser()
    //const { updateUser } = useStoreUser
    // updateUser()
    next()
})

export default router
