import type { UploadRawFile } from "element-plus";

export interface TypeProjectSimple {
  name: string,
  caption?: string,
  description?: string,
  initial: string,
  primary_color: string,
  icon: string|null
}

export interface ProjectsCreateForm {
  name: string,
  caption: string,
  description: string,
  primary_color: string,
  secondary_color: string,
  icon: UploadRawFile|string|null,
  icon_file: string|null
}