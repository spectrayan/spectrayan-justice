import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-witness',
templateUrl: './witness.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class WitnessFormComponent{
    @Input()form!: Models.WitnessFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);
    protected readonly WitnessTypeOptions = Object.values(Models.WitnessType);
    protected readonly CredibilityLevelOptions = Object.values(Models.CredibilityLevel);

}
