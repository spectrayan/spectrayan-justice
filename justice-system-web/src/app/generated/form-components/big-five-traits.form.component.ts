import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-big-five-traits',
templateUrl: './big-five-traits.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class BigFiveTraitsFormComponent{
    @Input()form!: Models.BigFiveTraitsFormType;

}
