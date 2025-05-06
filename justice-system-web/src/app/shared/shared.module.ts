import {NgModule} from "@angular/core";
import {FieldValidationErrorComponent} from "./error/field.validation.error.component";
import {MatError} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {CommonModule} from "@angular/common";
import {MatCardModule} from "@angular/material/card";
import {MatDatepickerInput, MatDatepickerModule} from "@angular/material/datepicker";
import {MatIconModule} from "@angular/material/icon";
import {MatSelectModule} from "@angular/material/select";
import {ReactiveFormsModule} from "@angular/forms";
import {MatChipsModule} from "@angular/material/chips";
import {MatProgressSpinner} from "@angular/material/progress-spinner";
import {MatRadioButton, MatRadioGroup, MatRadioModule} from "@angular/material/radio";
import {RouterModule} from "@angular/router";
import {MatButtonModule} from "@angular/material/button";

@NgModule(
    {
        imports: [
            CommonModule,
            MatError,
            MatInputModule,
            MatCardModule,
            MatDatepickerInput,
            MatIconModule,
            MatSelectModule,
            MatDatepickerModule,
            ReactiveFormsModule,
            MatChipsModule,
            MatProgressSpinner,
            MatRadioGroup,
            MatRadioButton,
            MatRadioModule,
            RouterModule,
            MatButtonModule,
        ],
        exports: [
            FieldValidationErrorComponent,
        ],
        declarations: [
            FieldValidationErrorComponent,
        ],
        providers: []
    }
)
export class SharedModule {

}
