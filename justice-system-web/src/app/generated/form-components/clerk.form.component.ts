import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-clerk',
templateUrl: './clerk.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class ClerkFormComponent{
    @Input()form!: Models.ClerkFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
