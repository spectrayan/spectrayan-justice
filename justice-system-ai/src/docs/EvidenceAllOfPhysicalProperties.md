# EvidenceAllOfPhysicalProperties

Physical properties of the evidence (for PHYSICAL type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **str** | Dimensions of the physical evidence | [optional] 
**weight** | **str** | Weight of the physical evidence | [optional] 
**condition** | **str** | Condition of the physical evidence | [optional] 

## Example

```python
from generated.models.evidence_all_of_physical_properties import EvidenceAllOfPhysicalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceAllOfPhysicalProperties from a JSON string
evidence_all_of_physical_properties_instance = EvidenceAllOfPhysicalProperties.from_json(json)
# print the JSON string representation of the object
print(EvidenceAllOfPhysicalProperties.to_json())

# convert the object into a dict
evidence_all_of_physical_properties_dict = evidence_all_of_physical_properties_instance.to_dict()
# create an instance of EvidenceAllOfPhysicalProperties from a dict
evidence_all_of_physical_properties_from_dict = EvidenceAllOfPhysicalProperties.from_dict(evidence_all_of_physical_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


