export const routeRpg = [
    {
        path: "/rpg",
        name: "RpgList",
        component: () => import("@/views/RpgListView.vue"),
        meta: {
            title: "RPG"
        }
    },
    {
        path: "/rpg/:slug",
        component: () => import("@/views/RpgView.vue"),
        meta: {
            title: "RPG"
        },
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
            },
            {
                path: "/rpg/:slug/t:topic_pk-:topic_slug",
                name: "RpgForumTopic",
                component: () => import("@/views/rpg/forum/RpgForumTopic.vue")
            }
        ]
    }
  ]