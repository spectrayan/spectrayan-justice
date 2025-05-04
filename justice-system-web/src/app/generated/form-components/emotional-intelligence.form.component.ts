import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-emotional-intelligence',
templateUrl: './emotional-intelligence.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class EmotionalIntelligenceFormComponent{
    @Input()form!: Models.EmotionalIntelligenceFormType;

}
