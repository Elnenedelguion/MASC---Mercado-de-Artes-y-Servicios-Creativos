import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {User} from '../model/user';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  url="https://regres.in/api/users/1";

  constructor(private http:HttpClient) { }

  createUser(user:User):Observable<any>
  {
    return this.http.post(this.url, user)
  }
  

}

