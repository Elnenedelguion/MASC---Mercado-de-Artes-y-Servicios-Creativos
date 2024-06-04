import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../model/user';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/api/usuarios/';
  private token = '123456';

  constructor(private http: HttpClient) {}
  createUser(user: User): Observable<any> {
    return this.http.post(this.apiUrl, user);
  }

  isAuth(): boolean {
    return this.token.length > 0;
  }

  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.apiUrl}`, { email, password });
  }

  logout(): Observable<any> {
    return this.http.post(`${this.apiUrl}logout/`, {});
  }

  register(user: User): Observable<any> {
    return this.http.post(`{this.apiUrl`, user);
  }
}
