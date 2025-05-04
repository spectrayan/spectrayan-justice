# Personality

Person's personality traits and characteristics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personality_type** | [**PersonalityType**](PersonalityType.md) |  | 
**big_five_traits** | [**BigFiveTraits**](BigFiveTraits.md) |  | [optional] 
**dominant_traits** | **List[str]** | List of dominant personality traits. | [optional] 
**adaptability** | **int** | Score representing adaptability to new situations (1-10). | [optional] 
**stress_response** | [**StressResponse**](StressResponse.md) |  | [optional] 
**personality_notes** | **str** | Additional notes about the person&#39;s personality. | [optional] 

## Example

```python
from generated.models.personality import Personality

# TODO update the JSON string below
json = "{}"
# create an instance of Personality from a JSON string
personality_instance = Personality.from_json(json)
# print the JSON string representation of the object
print(Personality.to_json())

# convert the object into a dict
personality_dict = personality_instance.to_dict()
# create an instance of Personality from a dict
personality_from_dict = Personality.from_dict(personality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


