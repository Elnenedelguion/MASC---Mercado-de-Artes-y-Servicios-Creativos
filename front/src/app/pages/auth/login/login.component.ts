import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loginForm = this.formBuilder.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(5)]],
  });

  constructor(private formBuilder: FormBuilder, private router: Router, private authService: AuthService) {}

  ngOnInit(): void {}

  get email() {
    return this.loginForm.controls.email;
  }

  get password() {
    return this.loginForm.controls.password;
  }

  login() {
    if (this.loginForm.valid) {
      const emailValue = this.email.value;
      const passwordValue = this.password.value;
      
      if (emailValue && passwordValue) {
        this.authService.login(emailValue, passwordValue).subscribe({
          next: (response) => {
            if (response.token) {
              this.setToken(response.token);
            }
            console.log('Iniciar Sesión');
            console.log('Token set:', response.token);
            // Redirigir al dashboard después de una autenticación exitosa
            this.router.navigateByUrl('/dashboard');
            this.loginForm.reset();
          },
          error: (err) => {
            console.error('Error al iniciar sesión', err);
            alert('Error al iniciar sesión');
          }
        });}
    } else {
      this.loginForm.markAllAsTouched();
      alert('Para iniciar sesión debe completar todos los campos');
    }
  }


private setToken(token: string): void {
  localStorage.setItem('token', token);
}
}