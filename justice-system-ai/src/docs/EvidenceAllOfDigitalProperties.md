# EvidenceAllOfDigitalProperties

Digital properties of the evidence (for DIGITAL type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | **str** | File type of the digital evidence | [optional] 
**file_size** | **str** | Size of the digital evidence file | [optional] 
**hash** | **str** | Hash value of the digital evidence for integrity verification | [optional] 

## Example

```python
from generated.models.evidence_all_of_digital_properties import EvidenceAllOfDigitalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceAllOfDigitalProperties from a JSON string
evidence_all_of_digital_properties_instance = EvidenceAllOfDigitalProperties.from_json(json)
# print the JSON string representation of the object
print(EvidenceAllOfDigitalProperties.to_json())

# convert the object into a dict
evidence_all_of_digital_properties_dict = evidence_all_of_digital_properties_instance.to_dict()
# create an instance of EvidenceAllOfDigitalProperties from a dict
evidence_all_of_digital_properties_from_dict = EvidenceAllOfDigitalProperties.from_dict(evidence_all_of_digital_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


