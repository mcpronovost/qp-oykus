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
  "avatar": string|null,
  "owned_projects": [],
  "notifications": [],
  "lang": string,
  "last": number
}
