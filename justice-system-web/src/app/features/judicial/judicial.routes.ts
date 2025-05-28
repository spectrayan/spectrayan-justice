import { Routes } from '@angular/router';
import { LoginComponent } from './user-management/login/login.component';
import { RegisterComponent } from './user-management/register/register.component';
import { ForgotPasswordComponent } from './user-management/forgot-password/forgot-password.component';
import { ResetPasswordComponent } from './user-management/reset-password/reset-password.component';
import { MainComponent } from './main/main.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CaseManagementComponent } from './case-management/case-management.component';
import { LexPredictComponent } from './lex-predict/lex-predict.component';

export const judicialRoutes: Routes = [
  {
    path: '',
    component: MainComponent,
    children: [
      {
        path: 'dashboard',
        component: DashboardComponent
      },
      {
        path: 'case-management',
        component: CaseManagementComponent
      },
      {
        path: 'lex-predict',
        component: LexPredictComponent
      },
      {
        path: 'user-management/login',
        component: LoginComponent
      },
      {
        path: 'user-management/register',
        component: RegisterComponent
      },
      {
        path: 'user-management/forgot-password',
        component: ForgotPasswordComponent
      },
      {
        path: 'user-management/reset-password',
        component: ResetPasswordComponent
      },
      {
        path: '',
        redirectTo: 'dashboard',
        pathMatch: 'full'
      }
    ]
  }
];
