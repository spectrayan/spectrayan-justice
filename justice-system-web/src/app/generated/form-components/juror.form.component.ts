import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-juror',
templateUrl: './juror.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class JurorFormComponent{
    @Input()form!: Models.JurorFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
