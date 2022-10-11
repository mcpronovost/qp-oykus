import { createRouter, createWebHistory } from "vue-router";
import { storeApp, storeUser } from "@/plugins/store";

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
      path: "/leaderboard",
      name: "Leaderboard",
      component: () => import("@/views/LeaderboardView.vue")
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
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    const useStoreUser = storeUser()
    const { updateUser } = useStoreUser
    updateIsLoading(true)
    updateUser()
    next()
})

router.afterEach(async (to, from, next) => {
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    updateIsLoading(false)
})

export default router
