import type { UploadRawFile } from "element-plus";

export interface SettingsAccountForm {
  username: string|null,
  email: string|null,
  lang: string,
  timezone: string
}

export interface SettingsProfileForm {
  name: string|null,
  avatar: UploadRawFile|string|null,
  avatar_file: string|null
}