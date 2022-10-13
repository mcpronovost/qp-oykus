export interface AuthLoginForm {
  username: string,
  password: string
}

export interface AuthRegisterForm {
  username: string,
  email: string,
  name: string,
  password: string,
  password_confirm: string
}
