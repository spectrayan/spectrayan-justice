import {Component, Input} from '@angular/core';
import * as Models from "../model/models";
@Component({
selector: 'app-form-social-behavior',
templateUrl: './social-behavior.form.component.html',
styleUrls: ['../scss/common.scss'],
standalone: false,
})
export class SocialBehaviorFormComponent{
    @Input()form!: Models.SocialBehaviorFormType;
    protected readonly CommunicationStyleOptions = Object.values(Models.CommunicationStyle);
    protected readonly SocialNetworkSizeOptions = Object.values(Models.SocialNetworkSize);
    protected readonly ConflictResolutionStyleOptions = Object.values(Models.ConflictResolutionStyle);
    protected readonly LeadershipStyleOptions = Object.values(Models.LeadershipStyle);
    protected readonly TrustLevelOptions = Object.values(Models.TrustLevel);

}
