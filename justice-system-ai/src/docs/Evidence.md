# Evidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 
**evidence_number** | **str** | Unique evidence number assigned by the system | 
**name** | **str** | Name or title of the evidence | 
**description** | **str** | Detailed description of the evidence | [optional] 
**type** | [**EvidenceType**](EvidenceType.md) |  | 
**case_id** | **str** | ID of the case this evidence is associated with | 
**collection_date** | **datetime** | Date and time the evidence was collected | 
**collection_location** | **str** | Location where the evidence was collected | [optional] 
**collected_by_id** | **str** | ID of the person who collected the evidence | 
**status** | **str** | Current status of the evidence (e.g., in custody, analyzed, released) | [optional] 
**storage_location** | **str** | Current storage location of the evidence | [optional] 
**custody_chain** | [**List[CustodyRecord]**](CustodyRecord.md) | Chain of custody records for the evidence | [optional] 
**physical_properties** | [**EvidenceAllOfPhysicalProperties**](EvidenceAllOfPhysicalProperties.md) |  | [optional] 
**digital_properties** | [**EvidenceAllOfDigitalProperties**](EvidenceAllOfDigitalProperties.md) |  | [optional] 
**documentary_properties** | [**EvidenceAllOfDocumentaryProperties**](EvidenceAllOfDocumentaryProperties.md) |  | [optional] 
**forensic_properties** | [**EvidenceAllOfForensicProperties**](EvidenceAllOfForensicProperties.md) |  | [optional] 
**notes** | **str** | Additional notes about the evidence | [optional] 
**tags** | **List[str]** | Tags or keywords associated with the evidence | [optional] 
**file_paths** | **List[str]** | Paths to files associated with the evidence (photos, documents, etc.) | [optional] 

## Example

```python
from generated.models.evidence import Evidence

# TODO update the JSON string below
json = "{}"
# create an instance of Evidence from a JSON string
evidence_instance = Evidence.from_json(json)
# print the JSON string representation of the object
print(Evidence.to_json())

# convert the object into a dict
evidence_dict = evidence_instance.to_dict()
# create an instance of Evidence from a dict
evidence_from_dict = Evidence.from_dict(evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


