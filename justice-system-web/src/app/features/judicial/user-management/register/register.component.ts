import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  standalone: false
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  isLoading = false;
  hidePassword = true;
  hideConfirmPassword = true;

  constructor(
    private fb: FormBuilder,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', [Validators.required]]
    }, { validator: this.checkPasswords });
  }

  ngOnInit(): void {
  }

  // Custom validator to check if passwords match
  checkPasswords(group: FormGroup) {
    const password = group.get('password')?.value;
    const confirmPassword = group.get('confirmPassword')?.value;
    return password === confirmPassword ? null : { notMatching: true };
  }

  onSubmit(): void {
    if (this.registerForm.valid) {
      this.isLoading = true;
      // Here you would typically call a registration service
      // For now, we'll just simulate a delay and redirect
      setTimeout(() => {
        this.isLoading = false;
        // Navigate to login page after successful registration
        this.router.navigate(['/judicial/login']);
      }, 1500);
    } else {
      this.registerForm.markAllAsTouched();
    }
  }

  navigateToLogin(): void {
    this.router.navigate(['/judicial/login']);
  }
}
