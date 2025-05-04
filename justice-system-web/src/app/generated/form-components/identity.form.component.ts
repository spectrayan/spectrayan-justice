import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-identity',
templateUrl: './identity.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class IdentityFormComponent{
    @Input()form!: Models.IdentityFormType;
    protected readonly RaceOptions = Object.values(Models.Race);
    protected readonly ReligionOptions = Object.values(Models.Religion);

}
