import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { User } from '../model/user';
import { BehaviorSubject, throwError } from 'rxjs';
import { AuthResponse } from '../interfaz/auth-response'; 
import { AuthResData } from '../model/auth.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/api/auth/';
  user = new BehaviorSubject<User | null>(null);


  constructor(private http: HttpClient) {}

  signup(account: AuthResData) {
    return this.http
      .post<AuthResData>(`${this.apiUrl}registro/`, account)
      .pipe(
        catchError((error: HttpErrorResponse) => this.handleError(error)),
        tap((res) => {
          console.log(res);
        })
      );
  }

  
  private handleError(error: HttpErrorResponse) {
    console.log(error);
    let errorMessage = 'An unknown error occurred';
    if (!error.error) {
      return throwError(() => errorMessage);
    }
    if (error.error.non_field_errors) {
      errorMessage = error.error.non_field_errors[0];
    }
    if (error.error.email) {
      errorMessage = error.error.email[0];
    }
    if (error.error.username) {
      errorMessage = error.error.username[0];
    }
    return throwError(() => errorMessage);
  }

 
/*
  createUser(user: User): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}registro/`, user).pipe(
      tap(response => {
        if (response.token) {
          localStorage.setItem('token',response.token)
          //this.setToken(response.token);
        }
      })
    );
  }*/

  login(email: string, password: string): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.apiUrl}login/`, { email, password }).pipe(
      tap(response => {
        if (response.token) {
          this.setToken(response.token);
          console.log('Token set:', response.token); // Logging for debugging
        }
      }),
      catchError(this.handleError)
    );
  }

  logout(): Observable<any> {
    this.removeToken();
    return this.http.post(`${this.apiUrl}logout/`, {});
  }

  private setToken(token: string): void {
    localStorage.setItem('token', token);
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  removeToken(): void {
    localStorage.removeItem('token');
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }
}
