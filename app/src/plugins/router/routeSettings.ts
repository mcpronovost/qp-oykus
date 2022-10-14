export const routeSettings = [
  {
    path: "/settings",
    component: () => import("@/views/SettingsView.vue"),
    meta: {
      title: "Settings"
    },
    children: [
      {
        path: "",
        name: "Settings",
        component: () => import("@/views/settings/SettingsAccount.vue")
      },
      {
        path: "/settings/profile",
        name: "SettingsProfile",
        component: () => import("@/views/settings/SettingsProfile.vue")
      },
      {
        path: "/settings/notifications",
        name: "SettingsNotifications",
        component: () => import("@/views/settings/SettingsNotifications.vue")
      }
    ]
  }
]