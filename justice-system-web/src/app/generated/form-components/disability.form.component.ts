import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-disability',
templateUrl: './disability.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class DisabilityFormComponent{
    @Input()form!: Models.DisabilityFormType;

}
