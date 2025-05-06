import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss'],
  standalone: false
})
export class ResetPasswordComponent implements OnInit {
  resetPasswordForm: FormGroup;
  isLoading = false;
  isSubmitted = false;
  hidePassword = true;
  hideConfirmPassword = true;

  constructor(
    private fb: FormBuilder,
    private router: Router
  ) {
    this.resetPasswordForm = this.fb.group({
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', [Validators.required]]
    }, { validator: this.checkPasswords });
  }

  ngOnInit(): void {
    // In a real application, you would typically get a token from the URL
    // and validate it before allowing the user to reset their password
  }

  // Custom validator to check if passwords match
  checkPasswords(group: FormGroup) {
    const password = group.get('password')?.value;
    const confirmPassword = group.get('confirmPassword')?.value;
    return password === confirmPassword ? null : { notMatching: true };
  }

  onSubmit(): void {
    if (this.resetPasswordForm.valid) {
      this.isLoading = true;
      // Here you would typically call a password reset service with the token
      // For now, we'll just simulate a delay and show success message
      setTimeout(() => {
        this.isLoading = false;
        this.isSubmitted = true;
      }, 1500);
    } else {
      this.resetPasswordForm.markAllAsTouched();
    }
  }

  navigateToLogin(): void {
    this.router.navigate(['/judicial/login']);
  }
}
