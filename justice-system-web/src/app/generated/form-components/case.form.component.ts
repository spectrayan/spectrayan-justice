import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-case',
templateUrl: './case.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class CaseFormComponent{
    @Input()form!: Models.CaseFormType;
    protected readonly CaseTypeOptions = Object.values(Models.CaseType);
    protected readonly CaseStatusOptions = Object.values(Models.CaseStatus);

}
