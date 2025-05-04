# Bailiff


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
**badge_number** | **str** | Bailiff&#39;s badge or identification number | 
**rank** | **str** | Bailiff&#39;s rank or position | [optional] 
**email** | **str** | Bailiff&#39;s email address | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**court_id** | **str** | ID of the court the bailiff is assigned to | 
**years_of_service** | **int** | Number of years the bailiff has been in service | [optional] 
**certifications** | **List[str]** | List of certifications held by the bailiff | [optional] 

## Example

```python
from justice_system.models.bailiff import Bailiff

# TODO update the JSON string below
json = "{}"
# create an instance of Bailiff from a JSON string
bailiff_instance = Bailiff.from_json(json)
# print the JSON string representation of the object
print(Bailiff.to_json())

# convert the object into a dict
bailiff_dict = bailiff_instance.to_dict()
# create an instance of Bailiff from a dict
bailiff_from_dict = Bailiff.from_dict(bailiff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


