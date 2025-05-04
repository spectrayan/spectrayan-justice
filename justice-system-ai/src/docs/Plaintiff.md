# Plaintiff


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
**type** | [**PlaintiffType**](PlaintiffType.md) |  | [default to PlaintiffType.INDIVIDUAL]
**address** | [**Address**](Address.md) |  | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**email** | **str** | Plaintiff&#39;s email address | [optional] 
**claim_description** | **str** | Description of the plaintiff&#39;s claim | [optional] 
**damages_requested** | **float** | Amount of damages requested | [optional] 
**lawyer_id** | **str** | ID of the lawyer representing the plaintiff | [optional] 

## Example

```python
from generated.models.plaintiff import Plaintiff

# TODO update the JSON string below
json = "{}"
# create an instance of Plaintiff from a JSON string
plaintiff_instance = Plaintiff.from_json(json)
# print the JSON string representation of the object
print(Plaintiff.to_json())

# convert the object into a dict
plaintiff_dict = plaintiff_instance.to_dict()
# create an instance of Plaintiff from a dict
plaintiff_from_dict = Plaintiff.from_dict(plaintiff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


