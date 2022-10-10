import { createRouter, createWebHistory } from "vue-router";
import { storeUser } from "@/plugins/store";

const routes = [
    {
      path: "/",
      name: "Home",
      component: () => import("@/views/HomeView.vue")
    },
    {
      path: "/register",
      name: "AuthRegister",
      component: () => import("@/views/AuthView.vue")
    },
    {
      path: "/login",
      name: "AuthLogin",
      component: () => import("@/views/AuthView.vue")
    },
    {
      path: "/logout",
      name: "AuthLogout",
      component: () => import("@/views/AuthView.vue")
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import("@/views/ProfileView.vue")
    },
    {
      path: "/projects",
      name: "Projects",
      component: () => import("@/views/ProjectsView.vue")
    },
    {
      path: "/tasks",
      name: "Tasks",
      component: () => import("@/views/TasksView.vue")
    },
    {
      path: "/settings",
      name: "Settings",
      component: () => import("@/views/SettingsView.vue")
    },
    /* ===--- FALLBACK ---=== */
    {
      path: "/:catchAll(.*)",
      name: "Error",
      component: () => import("@/views/ErrorView.vue")
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

router.beforeEach(async (to, from, next) => {
    const useStoreUser = storeUser()
    const { updateUser } = useStoreUser
    updateUser()
    next()
})

export default router
