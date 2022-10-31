export const routeRpg = [
    {
        path: "/rpg",
        component: () => import("@/views/RpgView.vue"),
        meta: {
            title: "RPG"
        },
        children: [
            {
                path: "",
                name: "RpgList",
                component: () => import("@/views/rpg/RpgList.vue")
            },
            {
                path: "/rpg/:slug",
                component: () => import("@/views/rpg/RpgForum.vue"),
                children: [
                    {
                        path: "",
                        name: "RpgForum",
                        component: () => import("@/views/rpg/forum/RpgForumIndex.vue")
                    },
                    {
                        path: "/rpg/:slug/c:category_pk-:category_slug",
                        name: "RpgForumCategory",
                        component: () => import("@/views/rpg/forum/RpgForumCategory.vue")
                    },
                    {
                        path: "/rpg/:slug/s:section_pk-:section_slug",
                        name: "RpgForumSection",
                        component: () => import("@/views/rpg/forum/RpgForumSection.vue")
                    }
                ]
            },
        ]
    }
  ]