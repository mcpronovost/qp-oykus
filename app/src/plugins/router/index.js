import { createRouter, createWebHistory } from "vue-router";
import { storeApp, storeUser } from "@/plugins/store";
import i18n from "@/plugins/i18n";

const { t } = i18n.global;

const APPNAME = "Oykus"
const APPDESC = "Createandmanagerpgprojects"

const routes = [
    {
      path: "/",
      name: "Home",
      component: () => import("@/views/HomeView.vue")
    },
    {
      path: "/register",
      name: "AuthRegister",
      component: () => import("@/views/AuthView.vue"),
      meta: {
        title: "Register"
      }
    },
    {
      path: "/login",
      name: "AuthLogin",
      component: () => import("@/views/AuthView.vue"),
      meta: {
        title: "Login"
      }
    },
    {
      path: "/logout",
      name: "AuthLogout",
      component: () => import("@/views/AuthView.vue"),
      meta: {
        title: "Logout"
      }
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import("@/views/ProfileView.vue"),
      meta: {
        title: "Profile"
      }
    },
    {
      path: "/projects",
      name: "Projects",
      component: () => import("@/views/ProjectsView.vue"),
      meta: {
        title: "Projects"
      }
    },
    {
      path: "/tasks",
      name: "Tasks",
      component: () => import("@/views/TasksView.vue"),
      meta: {
        title: "Tasks"
      }
    },
    {
      path: "/leaderboard",
      name: "Leaderboard",
      component: () => import("@/views/LeaderboardView.vue"),
      meta: {
        title: "Leaderboard"
      }
    },
    {
      path: "/settings",
      name: "Settings",
      component: () => import("@/views/SettingsView.vue"),
      meta: {
        title: "Settings"
      }
    },
    /* ===--- FALLBACK ---=== */
    {
      path: "/:catchAll(.*)",
      name: "Error",
      component: () => import("@/views/ErrorView.vue"),
      meta: {
        title: "Error"
      }
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

const setMeta = (meta) => {
  if (meta.title) {
    document.title = `${t(meta.title)} - ${APPNAME}`
  } else  {
    document.title = APPNAME
  }
  if (meta.desc) {
    document.querySelector('meta[name="description"]').setAttribute("content", meta.desc)
  } else {
    document.querySelector('meta[name="description"]').setAttribute("content", t(APPDESC))
  }
}

router.beforeEach(async (to, from, next) => {
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    const useStoreUser = storeUser()
    const { updateUser } = useStoreUser
    updateIsLoading(true)
    setMeta(to.meta)
    updateUser()
    next()
})

router.afterEach(async (to, from, next) => {
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    updateIsLoading(false)
})

export default router
