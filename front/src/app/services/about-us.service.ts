import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AboutUsService {
  url: string="http://localhost:3000/";
  //'http://127.0.0.1'

  constructor(private http:HttpClient) { }
 private handleError(error: HttpErrorResponse){
  if (error.status ===0){
    console.error('An error ocurred:', error.error);
  } else {
    //Backend rechazó la petición y devuelve una respuesta con un código de estado.
    console.error(
      'Backend returned code ${error.status}, body was:', error.error);
  }
    //Observable falla, retorna un mensaje de error genérico para el usuario.
   return throwError(() => new Error('Something bad happened; please try again later'));
 
  }
  
  

  obtenerProfesionales(): Observable<any>
  {
    return this.http.get(this.url+"profesional").pipe(
      catchError(this.handleError)
    );
  }
}