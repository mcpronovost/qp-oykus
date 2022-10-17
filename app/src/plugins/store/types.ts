export interface TypeAppStore {
  "isLoading": boolean,
  "isSidenavShow": boolean,
  "isSideviewShow": boolean,
  "mainviewWidth": number
}

export interface TypeUserStore {
  "rat": string|null,
  "id": number|null,
  "username": string|null,
  "email": string|null,
  "name": string|null,
  "initial": string|null,
  "avatar": string|null,
  "owned_projects": Array<TypeUserProjects>,
  "staff_projects": Array<TypeUserProjects>,
  "notifications": Array<TypeUserNotification>,
  "lang": string,
  "last": number
}

export interface TypeUserProjects {
    "id": number,
    "name": string,
    "slug": string,
    "initial": string,
    "primary_color": string,
    "icon": string|null
}

export interface TypeUserNotification {
    id: number,
    user_from: number|null,
    project_from: number|null,
    initial: string|null,
    icon: string|null,
    content: string|null,
    has_type: string|null
}
