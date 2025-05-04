# Clerk


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
**position** | **str** | Position or title of the clerk | 
**department** | **str** | Department the clerk works in | [optional] 
**email** | **str** | Clerk&#39;s email address | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**court_id** | **str** | ID of the court the clerk is associated with | 
**years_of_service** | **int** | Number of years the clerk has been in service | [optional] 

## Example

```python
from generated.models.clerk import Clerk

# TODO update the JSON string below
json = "{}"
# create an instance of Clerk from a JSON string
clerk_instance = Clerk.from_json(json)
# print the JSON string representation of the object
print(Clerk.to_json())

# convert the object into a dict
clerk_dict = clerk_instance.to_dict()
# create an instance of Clerk from a dict
clerk_from_dict = Clerk.from_dict(clerk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


