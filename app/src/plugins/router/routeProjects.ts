export const routeProjects = [
  {
    path: "/projects",
    name: "Projects",
    component: () => import("@/views/ProjectsView.vue"),
    meta: {
      title: "Projects"
    }
  },
  {
    path: "/projects/:slug",
    name: "ProjectsDetail",
    component: () => import("@/views/projects/DetailView.vue")
  }
]