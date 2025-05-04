# BaseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 

## Example

```python
from justice_system.models.base_model import BaseModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseModel from a JSON string
base_model_instance = BaseModel.from_json(json)
# print the JSON string representation of the object
print(BaseModel.to_json())

# convert the object into a dict
base_model_dict = base_model_instance.to_dict()
# create an instance of BaseModel from a dict
base_model_from_dict = BaseModel.from_dict(base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


