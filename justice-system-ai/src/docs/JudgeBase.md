# JudgeBase


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
from generated.models.judge_base import JudgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeBase from a JSON string
judge_base_instance = JudgeBase.from_json(json)
# print the JSON string representation of the object
print(JudgeBase.to_json())

# convert the object into a dict
judge_base_dict = judge_base_instance.to_dict()
# create an instance of JudgeBase from a dict
judge_base_from_dict = JudgeBase.from_dict(judge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


