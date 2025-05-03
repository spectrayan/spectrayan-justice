import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-defendant',
templateUrl: './defendant.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class DefendantFormComponent{
    @Input()form!: Models.DefendantFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);
    protected readonly CustodyStatusOptions = Object.values(Models.CustodyStatus);

}
