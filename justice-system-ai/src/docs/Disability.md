# Disability

Person's disabilities and accessibility needs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disability_type** | **List[str]** | Types of disabilities the person has. | 
**accessibility_needs** | **List[str]** | Specific accessibility requirements or accommodations needed. | [optional] 
**coping_strategies** | **List[str]** | Strategies used to cope with the disability. | [optional] 
**impact_on_daily_life** | **str** | Description of how the disability affects daily activities. | [optional] 
**assistive_technology** | **List[str]** | Assistive devices or technology used. | [optional] 
**accommodation_history** | **str** | History of accommodations provided in various settings. | [optional] 
**disability_notes** | **str** | Additional notes about the disability. | [optional] 

## Example

```python
from generated.models.disability import Disability

# TODO update the JSON string below
json = "{}"
# create an instance of Disability from a JSON string
disability_instance = Disability.from_json(json)
# print the JSON string representation of the object
print(Disability.to_json())

# convert the object into a dict
disability_dict = disability_instance.to_dict()
# create an instance of Disability from a dict
disability_from_dict = Disability.from_dict(disability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


