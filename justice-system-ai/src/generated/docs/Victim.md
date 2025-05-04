# Victim


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
**date_of_birth** | **date** | Victim&#39;s date of birth | 
**address** | [**Address**](Address.md) |  | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**email** | **str** | Victim&#39;s email address | [optional] 
**injury_description** | **str** | Description of injuries or damages suffered | [optional] 
**impact_statement** | **str** | Victim impact statement | [optional] 
**relationship_to_defendant** | **str** | Relationship between victim and defendant | [optional] 

## Example

```python
from justice_system.models.victim import Victim

# TODO update the JSON string below
json = "{}"
# create an instance of Victim from a JSON string
victim_instance = Victim.from_json(json)
# print the JSON string representation of the object
print(Victim.to_json())

# convert the object into a dict
victim_dict = victim_instance.to_dict()
# create an instance of Victim from a dict
victim_from_dict = Victim.from_dict(victim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


