import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-court',
templateUrl: './court.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class CourtFormComponent{
    @Input()form!: Models.CourtFormType;
    protected readonly CourtTypeOptions = Object.values(Models.CourtType);

}
