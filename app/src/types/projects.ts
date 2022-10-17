import type { UploadRawFile } from "element-plus";
import type { TypeUserSimple } from "./users";

export interface TypeProject {
  name: string,
  slug: string,
  caption?: string,
  description?: string,
  initial: string,
  primary_color: string,
  icon: string|null,
  creator: string|null,
  owner: TypeUserSimple|null
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