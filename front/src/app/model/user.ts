export class User{
    /*nombre:string="";
    apellido:string="";
    
    password:string="";
    email:string="";
    id:number=0;*/
      constructor(
        public id?: string,
        public email?: string,
        public username?: string,
        public name?: string,
        public token?: string,
        public is_admin?: boolean
      ) {}
  }
  