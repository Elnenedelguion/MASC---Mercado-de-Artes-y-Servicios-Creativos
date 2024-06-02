import { AuthService } from '../../../services/auth.service';
import {User} from '../../../model/user'
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AbstractControl, ValidatorFn } from '@angular/forms';

// Función de validación personalizada para comparar contraseñas
export const checkPasswords: ValidatorFn = (control: AbstractControl): {[key: string]: boolean} | null => {
  const password = control.get('password');
  const repeatPassword = control.get('repeatPassword');

  if (password && repeatPassword && password.value !== repeatPassword.value) {
    return { 'passwordMismatch': true };
  }

  return null;
};



@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
})




export class RegisterComponent implements OnInit {
  signupForm = this.formBuilder.nonNullable.group({
    name: ['', [Validators.required, Validators.minLength(3)]],
    surname: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(5)]],
    repeatPassword: ['', [Validators.required, Validators.minLength(5), checkPasswords]],
  })
  ;

  constructor(private formBuilder: FormBuilder, private authService: AuthService, private router: Router) {}

  ngOnInit(): void {}

  get name() {
    return this.signupForm.controls.name;
  }

  get surname() {
    return this.signupForm.controls.surname;
  }

  get email() {
    return this.signupForm.controls.email;
  }

  get password() {
    return this.signupForm.controls.password;
  }

  get repeatPassword() {
    return this.signupForm.controls.repeatPassword;
  }

  signup() {
    if (this.signupForm.valid) {
      console.log('Iniciar Sesión');
      this.router.navigateByUrl('/');
      this.signupForm.reset();
    } else {
      this.signupForm.markAllAsTouched();
      alert('Para registrarse debe completar todos los campos');
    }
  }

  navigateToTyC() {
    this.router.navigate(['/terms-and-conditions']);
  }

  onEnviar(event: Event): void {
    event.preventDefault();
    if (this.signupForm.valid) {
      console.log('Enviando al servidor...');
      this.authService.createUser(this.signupForm.value as User).subscribe((data) => {
        if (data.id > 0) {
          alert('El registro ha sido creado satisfactoriamente. A continuación, por favor Inicie Sesión.');
          this.router.navigate(['/login']);
        }
      });
    } else {
      this.signupForm.markAllAsTouched();
    }
  }
}
