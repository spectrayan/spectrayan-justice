# EvidenceAllOfDocumentaryProperties

Documentary properties of the evidence (for DOCUMENTARY type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Type of document | [optional] 
**page_count** | **int** | Number of pages in the document | [optional] 
**author** | **str** | Author of the document | [optional] 

## Example

```python
from generated.models.evidence_all_of_documentary_properties import EvidenceAllOfDocumentaryProperties

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceAllOfDocumentaryProperties from a JSON string
evidence_all_of_documentary_properties_instance = EvidenceAllOfDocumentaryProperties.from_json(json)
# print the JSON string representation of the object
print(EvidenceAllOfDocumentaryProperties.to_json())

# convert the object into a dict
evidence_all_of_documentary_properties_dict = evidence_all_of_documentary_properties_instance.to_dict()
# create an instance of EvidenceAllOfDocumentaryProperties from a dict
evidence_all_of_documentary_properties_from_dict = EvidenceAllOfDocumentaryProperties.from_dict(evidence_all_of_documentary_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


