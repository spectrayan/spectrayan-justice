import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { SharedModule } from '../../shared/shared.module';

// Material Imports
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSelectModule } from '@angular/material/select';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatStepperModule } from '@angular/material/stepper';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatTabsModule } from '@angular/material/tabs';
import { MatCheckboxModule } from '@angular/material/checkbox';

// Components
import { LoginComponent } from './user-management/login/login.component';
import { RegisterComponent } from './user-management/register/register.component';
import { ForgotPasswordComponent } from './user-management/forgot-password/forgot-password.component';
import { ResetPasswordComponent } from './user-management/reset-password/reset-password.component';
import { MainComponent } from './main/main.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CaseManagementComponent } from './case-management/case-management.component';

// LexPredict Components
import { LexPredictComponent } from './lex-predict/lex-predict.component';
import { CaseInfoComponent } from './lex-predict/steps/case-info/case-info.component';
import { LawyerSelectionComponent } from './lex-predict/steps/lawyer-selection/lawyer-selection.component';
import { JurySelectionComponent } from './lex-predict/steps/jury-selection/jury-selection.component';
import { EvidenceComponent } from './lex-predict/steps/evidence/evidence.component';
import { ReviewComponent } from './lex-predict/steps/review/review.component';

// Routes
import { judicialRoutes } from './judicial.routes';
import {GeneratedModule} from '../../generated';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatListModule, MatNavList} from '@angular/material/list';
import {MatToolbarModule} from '@angular/material/toolbar';

@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    ForgotPasswordComponent,
    ResetPasswordComponent,
    MainComponent,
    DashboardComponent,
    CaseManagementComponent,
    LexPredictComponent,
    CaseInfoComponent,
    LawyerSelectionComponent,
    JurySelectionComponent,
    EvidenceComponent,
    ReviewComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(judicialRoutes),
    ReactiveFormsModule,
    SharedModule,
    GeneratedModule,
    // Material Modules
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatDividerModule,
    MatProgressSpinnerModule,
    MatTableModule,
    MatPaginatorModule,
    MatSelectModule,
    MatTooltipModule,
    MatSidenavModule,
    MatNavList,
    MatToolbarModule,
    MatListModule,
    MatStepperModule,
    MatExpansionModule,
    MatTabsModule,
    MatCheckboxModule
  ],
  exports: [
  ]
})
export class JudicialModule { }
