/**
 * Justice system APIs
 *
 * Contact: admin@spectrayan.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { EvidenceType } from './evidence-type';
import { EvidenceAllOfForensicProperties } from './evidence-all-of-forensic-properties';
import { EvidenceAllOfDocumentaryProperties } from './evidence-all-of-documentary-properties';
import { EvidenceAllOfDigitalProperties } from './evidence-all-of-digital-properties';
import { EvidenceAllOfPhysicalProperties } from './evidence-all-of-physical-properties';
import { CustodyRecord } from './custody-record';


import * as EvidenceTypeModule from './evidence-type';
import * as EvidenceAllOfForensicPropertiesModule from './evidence-all-of-forensic-properties';
import * as EvidenceAllOfDocumentaryPropertiesModule from './evidence-all-of-documentary-properties';
import * as EvidenceAllOfDigitalPropertiesModule from './evidence-all-of-digital-properties';
import * as EvidenceAllOfPhysicalPropertiesModule from './evidence-all-of-physical-properties';
import * as CustodyRecordModule from './custody-record';
import {FormArray, FormControl, FormGroup, Validators} from "@angular/forms";
import {DocumentData, QueryDocumentSnapshot, SnapshotOptions, Timestamp} from "@angular/fire/firestore";

export interface Evidence {
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

        /**
        * Unique evidence number assigned by the system
        */
        evidenceNumber: string;

        /**
        * Name or title of the evidence
        */
        name: string;

        /**
        * Detailed description of the evidence
        */
        description?: string;

        type: EvidenceType;

        /**
        * ID of the case this evidence is associated with
        */
        caseId: string;

        /**
        * Date and time the evidence was collected
        */
        collectionDate: Date;

        /**
        * Location where the evidence was collected
        */
        collectionLocation?: string;

        /**
        * ID of the person who collected the evidence
        */
        collectedById: string;

        /**
        * Current status of the evidence (e.g., in custody, analyzed, released)
        */
        status?: string;

        /**
        * Current storage location of the evidence
        */
        storageLocation?: string;

        /**
        * Chain of custody records for the evidence
        */
        custodyChain?: Array<CustodyRecord>;

        physicalProperties?: EvidenceAllOfPhysicalProperties;

        digitalProperties?: EvidenceAllOfDigitalProperties;

        documentaryProperties?: EvidenceAllOfDocumentaryProperties;

        forensicProperties?: EvidenceAllOfForensicProperties;

        /**
        * Additional notes about the evidence
        */
        notes?: string;

        /**
        * Tags or keywords associated with the evidence
        */
        tags?: Array<string>;

        /**
        * Paths to files associated with the evidence (photos, documents, etc.)
        */
        filePaths?: Array<string>;

}

export type EvidenceFormType = FormGroup<{
    evidenceNumber: FormControl<string>;

    name: FormControl<string>;

    description: FormControl<string|null>;

    type: FormControl<EvidenceType>;

    caseId: FormControl<string>;

    collectionDate: FormControl<Date>;

    collectionLocation: FormControl<string|null>;

    collectedById: FormControl<string>;

    status: FormControl<string|null>;

    storageLocation: FormControl<string|null>;

    custodyChain: FormControl<Array<CustodyRecord>|null>;

    physicalProperties: FormControl<EvidenceAllOfPhysicalProperties|null>;

    digitalProperties: FormControl<EvidenceAllOfDigitalProperties|null>;

    documentaryProperties: FormControl<EvidenceAllOfDocumentaryProperties|null>;

    forensicProperties: FormControl<EvidenceAllOfForensicProperties|null>;

    notes: FormControl<string|null>;

    tags: FormControl<Array<string>|null>;

    filePaths: FormControl<Array<string>|null>;
 }>


// Firestore data converter for Evidence
export const EvidenceFirestoreConverter = {
toFirestore(modelObject: Evidence): DocumentData {
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
        if (modelObject.evidenceNumber !== undefined) {
                    result['evidenceNumber'] = modelObject.evidenceNumber;
        }
        if (modelObject.name !== undefined) {
                    result['name'] = modelObject.name;
        }
        if (modelObject.description !== undefined) {
                    result['description'] = modelObject.description;
        }
        if (modelObject.type !== undefined) {

        result['type'] = modelObject.type;
        }
        if (modelObject.caseId !== undefined) {
                    result['caseId'] = modelObject.caseId;
        }
        if (modelObject.collectionDate !== undefined) {
                    result['collectionDate'] = modelObject.collectionDate;
        }
        if (modelObject.collectionLocation !== undefined) {
                    result['collectionLocation'] = modelObject.collectionLocation;
        }
        if (modelObject.collectedById !== undefined) {
                    result['collectedById'] = modelObject.collectedById;
        }
        if (modelObject.status !== undefined) {
                    result['status'] = modelObject.status;
        }
        if (modelObject.storageLocation !== undefined) {
                    result['storageLocation'] = modelObject.storageLocation;
        }
        if (modelObject.custodyChain !== undefined) {


            if (Array.isArray(modelObject.custodyChain)) {
            result['custodyChain'] = modelObject.custodyChain.map(item => {
            return CustodyRecordModule.CustodyRecordFirestoreConverter.toFirestore(item);
            });
            } else {
            result['custodyChain'] = [];
            }

        }
        if (modelObject.physicalProperties !== undefined) {

        result['physicalProperties'] = modelObject.physicalProperties;
        }
        if (modelObject.digitalProperties !== undefined) {

        result['digitalProperties'] = modelObject.digitalProperties;
        }
        if (modelObject.documentaryProperties !== undefined) {

        result['documentaryProperties'] = modelObject.documentaryProperties;
        }
        if (modelObject.forensicProperties !== undefined) {

        result['forensicProperties'] = modelObject.forensicProperties;
        }
        if (modelObject.notes !== undefined) {
                    result['notes'] = modelObject.notes;
        }
        if (modelObject.tags !== undefined) {
                    result['tags'] = modelObject.tags;
        }
        if (modelObject.filePaths !== undefined) {
                    result['filePaths'] = modelObject.filePaths;
        }
return result;
},
fromFirestore(snapshot: QueryDocumentSnapshot, options: SnapshotOptions): Evidence {
const data = snapshot.data(options);
return {
    id: snapshot.id,

                    createdBy: data['createdBy'],

                    createdAt: data['createdAt'] ? (data['createdAt'] as Timestamp).toDate() : undefined,

                    updatedBy: data['updatedBy'],

                    updatedAt: data['updatedAt'] ? (data['updatedAt'] as Timestamp).toDate() : undefined,

                    evidenceNumber: data['evidenceNumber'],

                    name: data['name'],

                    description: data['description'],


            type: data['type'],

                    caseId: data['caseId'],

                    collectionDate: data['collectionDate'] ? (data['collectionDate'] as Timestamp).toDate() : undefined,

                    collectionLocation: data['collectionLocation'],

                    collectedById: data['collectedById'],

                    status: data['status'],

                    storageLocation: data['storageLocation'],

            custodyChain: data['custodyChain'] ? (data['custodyChain'] as Array<any>).map(item => {
                return CustodyRecordModule.CustodyRecordFirestoreConverter.fromFirestore(item, options);
                }) : [],



            physicalProperties: data['physicalProperties'],


            digitalProperties: data['digitalProperties'],


            documentaryProperties: data['documentaryProperties'],


            forensicProperties: data['forensicProperties'],

                    notes: data['notes'],

                    tags: data['tags'],

                    filePaths: data['filePaths'],
    } as Evidence;
    }

};

