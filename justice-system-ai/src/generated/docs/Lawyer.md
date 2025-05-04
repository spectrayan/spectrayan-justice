# Lawyer


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
**type** | [**LawyerType**](LawyerType.md) |  | 
**bar_number** | **str** | Lawyer&#39;s bar association number | 
**firm** | **str** | Law firm or organization the lawyer is associated with | [optional] 
**email** | **str** | Lawyer&#39;s email address | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**years_of_experience** | **int** | Years of experience as a lawyer | [optional] 

## Example

```python
from justice_system.models.lawyer import Lawyer

# TODO update the JSON string below
json = "{}"
# create an instance of Lawyer from a JSON string
lawyer_instance = Lawyer.from_json(json)
# print the JSON string representation of the object
print(Lawyer.to_json())

# convert the object into a dict
lawyer_dict = lawyer_instance.to_dict()
# create an instance of Lawyer from a dict
lawyer_from_dict = Lawyer.from_dict(lawyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


