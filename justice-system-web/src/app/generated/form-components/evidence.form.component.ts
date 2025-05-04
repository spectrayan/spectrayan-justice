import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-evidence',
templateUrl: './evidence.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class EvidenceFormComponent{
    @Input()form!: Models.EvidenceFormType;

}
