import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss'],
  standalone: false
})
export class ForgotPasswordComponent implements OnInit {
  forgotPasswordForm: FormGroup;
  isLoading = false;
  isSubmitted = false;

  constructor(
    private fb: FormBuilder,
    private router: Router
  ) {
    this.forgotPasswordForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.forgotPasswordForm.valid) {
      this.isLoading = true;
      // Here you would typically call a password reset service
      // For now, we'll just simulate a delay and show success message
      setTimeout(() => {
        this.isLoading = false;
        this.isSubmitted = true;
      }, 1500);
    } else {
      this.forgotPasswordForm.markAllAsTouched();
    }
  }

  navigateToLogin(): void {
    this.router.navigate(['/judicial/login']);
  }

  resetForm(): void {
    this.isSubmitted = false;
    this.forgotPasswordForm.reset();
  }
}
