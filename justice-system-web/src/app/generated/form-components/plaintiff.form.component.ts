import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-plaintiff',
templateUrl: './plaintiff.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class PlaintiffFormComponent{
    @Input()form!: Models.PlaintiffFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);
    protected readonly PlaintiffTypeOptions = Object.values(Models.PlaintiffType);

}
