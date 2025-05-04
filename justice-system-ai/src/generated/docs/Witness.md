# Witness


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
**type** | [**WitnessType**](WitnessType.md) |  | 
**testimony** | **str** | Summary of witness testimony | [optional] 
**credibility** | [**CredibilityLevel**](CredibilityLevel.md) |  | [optional] [default to CredibilityLevel.UNKNOWN]
**address** | [**Address**](Address.md) |  | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**email** | **str** | Witness&#39;s email address | [optional] 
**relationship** | **str** | Relationship to the case or parties involved | [optional] 

## Example

```python
from justice_system.models.witness import Witness

# TODO update the JSON string below
json = "{}"
# create an instance of Witness from a JSON string
witness_instance = Witness.from_json(json)
# print the JSON string representation of the object
print(Witness.to_json())

# convert the object into a dict
witness_dict = witness_instance.to_dict()
# create an instance of Witness from a dict
witness_from_dict = Witness.from_dict(witness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


