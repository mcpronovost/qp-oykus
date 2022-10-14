export const routeProjects = [
  {
    path: "/projects",
    component: () => import("@/views/ProjectsView.vue"),
    meta: {
      title: "Projects"
    },
    children: [
        {
            path: "",
            name: "Projects",
            component: () => import("@/views/projects/ProjectsList.vue")
        },
        {
            path: "/projects/:slug",
            name: "ProjectsDetail",
            component: () => import("@/views/projects/ProjectsDetail.vue")
        }
    ]
  }
]