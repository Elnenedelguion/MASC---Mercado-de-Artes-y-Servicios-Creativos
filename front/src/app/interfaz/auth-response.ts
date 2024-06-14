export interface AuthResponse {
  user_id?: string;
  email: string;
  name?: string;
  username: string;
  token?: string;
  is_admin?: boolean;
  }
  
  export interface singupModel {
    email: string;
    username: string;
    first_name: string;
    last_name: string;
    password: string;
  }