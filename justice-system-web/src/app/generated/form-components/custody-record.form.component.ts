import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-custody-record',
templateUrl: './custody-record.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class CustodyRecordFormComponent{
    @Input()form!: Models.CustodyRecordFormType;

}
