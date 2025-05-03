import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-victim',
templateUrl: './victim.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class VictimFormComponent{
    @Input()form!: Models.VictimFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
