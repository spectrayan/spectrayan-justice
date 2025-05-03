import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-jury',
templateUrl: './jury.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class JuryFormComponent{
    @Input()form!: Models.JuryFormType;
    protected readonly JuryStatusOptions = Object.values(Models.JuryStatus);

}
