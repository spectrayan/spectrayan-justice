import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-lawyer',
templateUrl: './lawyer.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class LawyerFormComponent{
    @Input()form!: Models.LawyerFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
