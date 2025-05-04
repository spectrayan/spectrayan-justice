# Defendant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 
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
**date_of_birth** | **date** | Defendant&#39;s date of birth | 
**address** | [**Address**](Address.md) |  | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**email** | **str** | Defendant&#39;s email address | [optional] 
**criminal_history** | **str** | Summary of defendant&#39;s criminal history | [optional] 
**custody_status** | [**CustodyStatus**](CustodyStatus.md) |  | [optional] 

## Example

```python
from generated.models.defendant import Defendant

# TODO update the JSON string below
json = "{}"
# create an instance of Defendant from a JSON string
defendant_instance = Defendant.from_json(json)
# print the JSON string representation of the object
print(Defendant.to_json())

# convert the object into a dict
defendant_dict = defendant_instance.to_dict()
# create an instance of Defendant from a dict
defendant_from_dict = Defendant.from_dict(defendant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


