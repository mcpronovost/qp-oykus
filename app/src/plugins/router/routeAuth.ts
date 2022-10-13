export const routeAuth = [
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
  }
]