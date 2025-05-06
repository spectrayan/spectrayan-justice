import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  standalone: false
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  isLoading = false;
  hidePassword = true;

  constructor(
    private fb: FormBuilder,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.isLoading = true;
      // Here you would typically call an authentication service
      // For now, we'll just simulate a delay and redirect
      setTimeout(() => {
        this.isLoading = false;
        // Navigate to dashboard or home page after successful login
        // this.router.navigate(['/dashboard']);
      }, 1500);
    } else {
      this.loginForm.markAllAsTouched();
    }
  }

  navigateToRegister(): void {
    this.router.navigate(['/judicial/register']);
  }

  navigateToForgotPassword(): void {
    this.router.navigate(['/judicial/forgot-password']);
  }
}
