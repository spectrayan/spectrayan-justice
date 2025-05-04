# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**PersonTitle**](PersonTitle.md) |  | [optional] 
**first_name** | **str** | Person&#39;s first name. | 
**middle_name** | **str** | Person&#39;s middle name. | [optional] 
**last_name** | **str** | Person&#39;s last name. | 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**identity** | [**Identity**](Identity.md) |  | [optional] 
**personality** | [**Personality**](Personality.md) |  | [optional] 
**emotional_intelligence** | [**EmotionalIntelligence**](EmotionalIntelligence.md) |  | [optional] 
**physical_traits** | [**PhysicalTraits**](PhysicalTraits.md) |  | [optional] 
**social_behavior** | [**SocialBehavior**](SocialBehavior.md) |  | [optional] 
**disability** | [**Disability**](Disability.md) |  | [optional] 
**about** | **str** | General information or biography about the person. | [optional] 

## Example

```python
from generated.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


