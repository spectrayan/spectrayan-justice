import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-bailiff',
templateUrl: './bailiff.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class BailiffFormComponent{
    @Input()form!: Models.BailiffFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
