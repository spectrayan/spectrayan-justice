import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-physical-traits',
templateUrl: './physical-traits.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class PhysicalTraitsFormComponent{
    @Input()form!: Models.PhysicalTraitsFormType;
    protected readonly EyeColorOptions = Object.values(Models.EyeColor);
    protected readonly HairColorOptions = Object.values(Models.HairColor);
    protected readonly BloodTypeOptions = Object.values(Models.BloodType);
    protected readonly PhysicalConditionOptions = Object.values(Models.PhysicalCondition);

}
