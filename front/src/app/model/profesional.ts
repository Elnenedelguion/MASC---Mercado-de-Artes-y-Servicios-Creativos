export class Profesional
{
    id!:Number;
    nombre!: String;
    puesto!:String; 
    avatar!:String;

    constructor(id:number, nombre:string, puesto:string, avatar:string)
    {
        this.id=id;
        this.nombre=nombre;
        this.puesto=puesto;
        this.avatar=avatar;
    }
}