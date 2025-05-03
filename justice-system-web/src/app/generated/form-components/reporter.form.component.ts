import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-reporter',
templateUrl: './reporter.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class ReporterFormComponent{
    @Input()form!: Models.ReporterFormType;
    protected readonly PersonTitleOptions = Object.values(Models.PersonTitle);
    protected readonly GenderOptions = Object.values(Models.Gender);

}
