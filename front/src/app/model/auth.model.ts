export interface singupModel {
    email: string;
    username: string;
    first_name: string;
    last_name: string;
    password: string;
  }
  
  export interface AuthResData {
    user_id?: string;
    email: string;
    first_name?: string;
    last_name?: string;
    username: string;
    token?: string;
    is_admin?: boolean;
    password: string;
  }
  
  export interface loginModel {
    email: string;
    password: string;
  }
  
  export class User {
    constructor(
      public id?: string,
      public email?: string,
      public username?: string,
      public name?: string,
      public token?: string,
      public is_admin?: boolean
    ) {}
  }
  