import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Angular Material Imports
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatOptionModule } from '@angular/material/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatRadioModule } from '@angular/material/radio';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTabsModule } from '@angular/material/tabs';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatChipsModule } from '@angular/material/chips';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatStepperModule } from '@angular/material/stepper';
import { MatListModule } from '@angular/material/list';
import { MatDividerModule } from '@angular/material/divider';
import { MatMenuModule } from '@angular/material/menu';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatSliderModule } from '@angular/material/slider';
import { MatBadgeModule } from '@angular/material/badge';
import { MatBottomSheetModule } from '@angular/material/bottom-sheet';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatRippleModule } from '@angular/material/core';
import { MatTreeModule } from '@angular/material/tree';

// Form Components
import { AddressFormComponent } from './form-components/address.form.component';
import { BailiffFormComponent } from './form-components/bailiff.form.component';
import { BigFiveTraitsFormComponent } from './form-components/big-five-traits.form.component';
import { CaseFormComponent } from './form-components/case.form.component';
import { ClerkFormComponent } from './form-components/clerk.form.component';
import { EvidenceFormComponent } from './form-components/evidence.form.component';
import { IdentityFormComponent } from './form-components/identity.form.component';
import { JudgeFormComponent } from './form-components/judge.form.component';
import { JurorFormComponent } from './form-components/juror.form.component';
import { JuryFormComponent } from './form-components/jury.form.component';
import { LawyerFormComponent } from './form-components/lawyer.form.component';
import { PersonalityFormComponent } from './form-components/personality.form.component';
import { PhoneFormComponent } from './form-components/phone.form.component';
import { PhysicalTraitsFormComponent } from './form-components/physical-traits.form.component';
import { PlaintiffFormComponent } from './form-components/plaintiff.form.component';
import { ReporterFormComponent } from './form-components/reporter.form.component';
import { SocialBehaviorFormComponent } from './form-components/social-behavior.form.component';
import { VictimFormComponent } from './form-components/victim.form.component';
import { WitnessFormComponent } from './form-components/witness.form.component';
import {SharedModule} from '../shared/shared.module';
import {DisabilityFormComponent} from './form-components/disability.form.component';
import {EmotionalIntelligenceFormComponent} from './form-components/emotional-intelligence.form.component';

// Array of all form components for easier management
const formComponents = [
  AddressFormComponent,
  BailiffFormComponent,
  BigFiveTraitsFormComponent,
  CaseFormComponent,
  ClerkFormComponent,
  EvidenceFormComponent,
  IdentityFormComponent,
  JudgeFormComponent,
  JurorFormComponent,
  JuryFormComponent,
  LawyerFormComponent,
  PersonalityFormComponent,
  PhoneFormComponent,
  PhysicalTraitsFormComponent,
  PlaintiffFormComponent,
  ReporterFormComponent,
  SocialBehaviorFormComponent,
  VictimFormComponent,
  WitnessFormComponent,
  DisabilityFormComponent,
  EmotionalIntelligenceFormComponent,

];

// Array of all Angular Material modules
const materialModules = [
  MatFormFieldModule,
  MatInputModule,
  MatSelectModule,
  MatOptionModule,
  MatButtonModule,
  MatCheckboxModule,
  MatRadioModule,
  MatDatepickerModule,
  MatNativeDateModule,
  MatCardModule,
  MatIconModule,
  MatTableModule,
  MatPaginatorModule,
  MatSortModule,
  MatDialogModule,
  MatSnackBarModule,
  MatTooltipModule,
  MatProgressSpinnerModule,
  MatTabsModule,
  MatExpansionModule,
  MatChipsModule,
  MatAutocompleteModule,
  MatSlideToggleModule,
  MatStepperModule,
  MatListModule,
  MatDividerModule,
  MatMenuModule,
  MatToolbarModule,
  MatSidenavModule,
  MatGridListModule,
  MatProgressBarModule,
  MatSliderModule,
  MatBadgeModule,
  MatBottomSheetModule,
  MatButtonToggleModule,
  MatRippleModule,
  MatTreeModule
];

@NgModule({
  declarations: [
    ...formComponents
  ],
  imports: [
    SharedModule,
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    ...materialModules
  ],
  exports: [
    ...formComponents
  ]
})
export class GeneratedModule { }
