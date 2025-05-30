/**
 * Justice system APIs
 *
 * Contact: admin@spectrayan.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Disability } from './disability';
import { EmotionalIntelligence } from './emotional-intelligence';
import { Personality } from './personality';
import { Gender } from './gender';
import { SocialBehavior } from './social-behavior';
import { Identity } from './identity';
import { PhysicalTraits } from './physical-traits';
import { PersonTitle } from './person-title';


import * as DisabilityModule from './disability';
import * as EmotionalIntelligenceModule from './emotional-intelligence';
import * as PersonalityModule from './personality';
import * as GenderModule from './gender';
import * as SocialBehaviorModule from './social-behavior';
import * as IdentityModule from './identity';
import * as PhysicalTraitsModule from './physical-traits';
import * as PersonTitleModule from './person-title';
import {FormArray, FormControl, FormGroup, Validators} from "@angular/forms";
import {DocumentData, QueryDocumentSnapshot, SnapshotOptions, Timestamp} from "@angular/fire/firestore";

export interface Judge { 
        /**
        * Unique document id auto generated
        */
        readonly id?: string;
    
        /**
        * The principal that created the entity containing the field.
        */
        readonly createdBy?: string;
    
        /**
        * The date and time the entity containing the field was created.
        */
        readonly createdAt?: Date;
    
        /**
        * The principal that recently modified the entity containing the field.
        */
        readonly updatedBy?: string;
    
        /**
        * The date the entity containing the field was recently modified.
        */
        readonly updatedAt?: Date;
    
        title?: PersonTitle;
    
        /**
        * Person\'s first name.
        */
        firstName: string;
    
        /**
        * Person\'s middle name.
        */
        middleName?: string;
    
        /**
        * Person\'s last name.
        */
        lastName: string;
    
        gender?: Gender;
    
        identity?: Identity;
    
        personality?: Personality;
    
        emotionalIntelligence?: EmotionalIntelligence;
    
        physicalTraits?: PhysicalTraits;
    
        socialBehavior?: SocialBehavior;
    
        disability?: Disability;
    
        /**
        * A short description about judge
        */
        about?: string;
    
        /**
        * Judge\'s email address
        */
        email?: string;
    
}

export type JudgeFormType = FormGroup<{ 
    title: FormControl<PersonTitle|null>;

    firstName: FormControl<string>;

    middleName: FormControl<string|null>;

    lastName: FormControl<string>;

    gender: FormControl<Gender|null>;

    identity: IdentityModule.IdentityFormType;
    
    personality: PersonalityModule.PersonalityFormType;
    
    emotionalIntelligence: EmotionalIntelligenceModule.EmotionalIntelligenceFormType;
    
    physicalTraits: PhysicalTraitsModule.PhysicalTraitsFormType;
    
    socialBehavior: SocialBehaviorModule.SocialBehaviorFormType;
    
    disability: DisabilityModule.DisabilityFormType;
    
    email: FormControl<string|null>;
 }>

export function getJudgeForm(): JudgeFormType {
    return new FormGroup({ 





    title: new FormControl<PersonTitle>("Mr.", {  nonNullable:   false ,
    validators: [ ] } ),
    

    firstName: new FormControl<string>("", {  nonNullable:  true  ,
    validators: [  Validators.required,  Validators.minLength(1), Validators.maxLength(12),] } ),
    

    middleName: new FormControl<string>("", {  nonNullable:   false ,
    validators: [ ] } ),
    

    lastName: new FormControl<string>("", {  nonNullable:  true  ,
    validators: [  Validators.required,  Validators.minLength(1),] } ),
    

    gender: new FormControl<Gender>("Decline To Identify", {  nonNullable:   false ,
    validators: [ ] } ),
    

    identity: IdentityModule.getIdentityForm(),


    personality: PersonalityModule.getPersonalityForm(),


    emotionalIntelligence: EmotionalIntelligenceModule.getEmotionalIntelligenceForm(),


    physicalTraits: PhysicalTraitsModule.getPhysicalTraitsForm(),


    socialBehavior: SocialBehaviorModule.getSocialBehaviorForm(),


    disability: DisabilityModule.getDisabilityForm(),



    email: new FormControl<string>("", {  nonNullable:   false ,
    validators: [  Validators.email,] } ),
    
    })
}


// Firestore data converter for Judge
export const JudgeFirestoreConverter = {
toFirestore(modelObject: Judge): DocumentData {
const result: DocumentData = {};
        if (modelObject.createdBy !== undefined) {
                    result['createdBy'] = modelObject.createdBy;
        }
        if (modelObject.createdAt !== undefined) {
                    result['createdAt'] = modelObject.createdAt;
        }
        if (modelObject.updatedBy !== undefined) {
                    result['updatedBy'] = modelObject.updatedBy;
        }
        if (modelObject.updatedAt !== undefined) {
                    result['updatedAt'] = modelObject.updatedAt;
        }
        if (modelObject.title !== undefined) {
        
        result['title'] = modelObject.title;
        }
        if (modelObject.firstName !== undefined) {
                    result['firstName'] = modelObject.firstName;
        }
        if (modelObject.middleName !== undefined) {
                    result['middleName'] = modelObject.middleName;
        }
        if (modelObject.lastName !== undefined) {
                    result['lastName'] = modelObject.lastName;
        }
        if (modelObject.gender !== undefined) {
        
        result['gender'] = modelObject.gender;
        }
        if (modelObject.identity !== undefined) {
        
        result['identity'] = modelObject.identity;
        }
        if (modelObject.personality !== undefined) {
        
        result['personality'] = modelObject.personality;
        }
        if (modelObject.emotionalIntelligence !== undefined) {
        
        result['emotionalIntelligence'] = modelObject.emotionalIntelligence;
        }
        if (modelObject.physicalTraits !== undefined) {
        
        result['physicalTraits'] = modelObject.physicalTraits;
        }
        if (modelObject.socialBehavior !== undefined) {
        
        result['socialBehavior'] = modelObject.socialBehavior;
        }
        if (modelObject.disability !== undefined) {
        
        result['disability'] = modelObject.disability;
        }
        if (modelObject.about !== undefined) {
                    result['about'] = modelObject.about;
        }
        if (modelObject.email !== undefined) {
                    result['email'] = modelObject.email;
        }
return result;
},
fromFirestore(snapshot: QueryDocumentSnapshot, options: SnapshotOptions): Judge {
const data = snapshot.data(options);
return {
    id: snapshot.id,
    
                    createdBy: data['createdBy'],
    
                    createdAt: data['createdAt'] ? (data['createdAt'] as Timestamp).toDate() : undefined,
    
                    updatedBy: data['updatedBy'],
    
                    updatedAt: data['updatedAt'] ? (data['updatedAt'] as Timestamp).toDate() : undefined,
    
            
            title: data['title'],
    
                    firstName: data['firstName'],
    
                    middleName: data['middleName'],
    
                    lastName: data['lastName'],
    
            
            gender: data['gender'],
    
            
            identity: data['identity'],
    
            
            personality: data['personality'],
    
            
            emotionalIntelligence: data['emotionalIntelligence'],
    
            
            physicalTraits: data['physicalTraits'],
    
            
            socialBehavior: data['socialBehavior'],
    
            
            disability: data['disability'],
    
                    about: data['about'],
    
                    email: data['email'],
    } as Judge;
    }

};

