import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-personality',
templateUrl: './personality.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class PersonalityFormComponent{
    @Input()form!: Models.PersonalityFormType;
    protected readonly PersonalityTypeOptions = Object.values(Models.PersonalityType);
    protected readonly StressResponseOptions = Object.values(Models.StressResponse);

}
