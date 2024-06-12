import { AuthService } from '../../../services/auth.service';
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AbstractControl, ValidatorFn } from '@angular/forms';
import { AuthResData } from '../../../model/auth.model';


@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
})




export class RegisterComponent implements OnInit {
  signupForm!: FormGroup;
  error: string = '';
  success: string = '';

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    this.signupForm = this.formBuilder.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      passwords: this.formBuilder.group(
        {
          password: ['', [Validators.required, Validators.minLength(8)]],
          confirmPassword: ['', Validators.required],
        },
        { validators: this.passwordCheck }
      ),
    });
  }

  onSignup() {
    console.log(this.signupForm);
    this.authService
      .signup({
        email: this.signupForm.value.email,
        username: this.signupForm.value.username,
        first_name: this.signupForm.value.firstName,
        last_name: this.signupForm.value.lastName,
        password: this.signupForm.value.passwords.password,
      })
      .subscribe({
        next: (data: AuthResData) => {
          this.success = 'Signup was successful';
          this.error = '';
          this.router.navigate(['/login']);
        },
        error: (errorRes) => {
          this.error = errorRes;
          alert(errorRes);
        },
      });
  }

  passwordCheck(control: AbstractControl): { [s: string]: boolean } | null {
    const password = control.get('password')?.value;
    const confirmPassword = control.get('confirmPassword')?.value;
    if (password !== confirmPassword) {
      return { notsame: true };
    }
    return null;
  }
}
