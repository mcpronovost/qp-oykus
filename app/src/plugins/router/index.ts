import type { RouteRecordRaw } from "vue-router";
import type { TypeRouteMeta } from "./types";
import { createRouter, createWebHistory } from "vue-router";
import { storeApp, storeUser } from "../store";
import i18n from "../i18n";

import { routeAuth } from "./routeAuth";
import { routeProjects } from "./routeProjects";
import { routeSettings } from "./routeSettings";

const { t } = i18n.global;

const APPNAME = "Oykus"
const APPDESC = "Createandmanagerpgprojects"

const routes = [
    {
      path: "/",
      name: "Home",
      component: () => import("@/views/HomeView.vue")
    },
    ...routeAuth,
    {
      path: "/profile",
      name: "Profile",
      component: () => import("@/views/ProfileView.vue"),
      meta: {
        title: "Profile"
      }
    },
    ...routeProjects,
    {
      path: "/tasks",
      name: "Tasks",
      component: () => import("@/views/TasksView.vue"),
      meta: {
        title: "Tasks"
      }
    },
    {
      path: "/rpg",
      name: "RPG",
      component: () => import("@/views/RpgView.vue"),
      meta: {
        title: "RPG"
      }
    },
    {
      path: "/forums",
      name: "Forums",
      component: () => import("@/views/ForumsView.vue"),
      meta: {
        title: "Forums"
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
    ...routeSettings,
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
    routes: routes as RouteRecordRaw[]
})

const setMeta = (meta: TypeRouteMeta) => {
  if (meta.title) {
    document.title = `${t(meta.title)} - ${APPNAME}`
  } else  {
    document.title = APPNAME
  }
  if (meta.desc) {
    document.querySelector('meta[name="description"]')?.setAttribute("content", meta.desc)
  } else {
    document.querySelector('meta[name="description"]')?.setAttribute("content", t(APPDESC))
  }
}

router.beforeEach((to, from, next) => {
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    const useStoreUser = storeUser()
    const { updateUser } = useStoreUser
    updateIsLoading(true)
    updateUser()
    next()
})

router.afterEach((to, from, next) => {
    const useStoreApp = storeApp()
    const { updateIsLoading } = useStoreApp
    setMeta(to.meta)
    updateIsLoading(false)
})

export default router
