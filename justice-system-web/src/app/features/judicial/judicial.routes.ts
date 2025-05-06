import { Routes } from '@angular/router';
import { LoginComponent } from './user-management/login/login.component';
import { RegisterComponent } from './user-management/register/register.component';
import { ForgotPasswordComponent } from './user-management/forgot-password/forgot-password.component';
import { ResetPasswordComponent } from './user-management/reset-password/reset-password.component';

export const judicialRoutes: Routes = [
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'forgot-password',
    component: ForgotPasswordComponent
  },
  {
    path: 'reset-password',
    component: ResetPasswordComponent
  },
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  }
];
