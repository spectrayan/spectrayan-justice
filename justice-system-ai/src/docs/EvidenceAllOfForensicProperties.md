# EvidenceAllOfForensicProperties

Forensic properties of the evidence (for FORENSIC type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_type** | **str** | Type of forensic test performed | [optional] 
**test_results** | **str** | Results of the forensic test | [optional] 
**test_date** | **datetime** | Date the forensic test was performed | [optional] 

## Example

```python
from generated.models.evidence_all_of_forensic_properties import EvidenceAllOfForensicProperties

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceAllOfForensicProperties from a JSON string
evidence_all_of_forensic_properties_instance = EvidenceAllOfForensicProperties.from_json(json)
# print the JSON string representation of the object
print(EvidenceAllOfForensicProperties.to_json())

# convert the object into a dict
evidence_all_of_forensic_properties_dict = evidence_all_of_forensic_properties_instance.to_dict()
# create an instance of EvidenceAllOfForensicProperties from a dict
evidence_all_of_forensic_properties_from_dict = EvidenceAllOfForensicProperties.from_dict(evidence_all_of_forensic_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


