import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-judge',
templateUrl: './judge.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class JudgeFormComponent{
    @Input()form!: Models.JudgeFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
