# Identity

Person's demographic information including race, ethnicity, religion, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**race** | [**Race**](Race.md) |  | 
**ethnicity** | **str** | The person&#39;s ethnic background. | 
**religion** | [**Religion**](Religion.md) |  | [optional] 
**creed** | **str** | The person&#39;s system of beliefs or principles. | [optional] 
**culture** | **str** | The person&#39;s cultural background or identity. | [optional] 
**caste** | **str** | The person&#39;s caste identification, if applicable. | [optional] 
**language** | **str** | The person&#39;s primary language. | [optional] 
**color** | **str** | The person&#39;s skin color. | [optional] 
**nationality** | **str** | The person&#39;s nationality. | [optional] 

## Example

```python
from generated.models.identity import Identity

# TODO update the JSON string below
json = "{}"
# create an instance of Identity from a JSON string
identity_instance = Identity.from_json(json)
# print the JSON string representation of the object
print(Identity.to_json())

# convert the object into a dict
identity_dict = identity_instance.to_dict()
# create an instance of Identity from a dict
identity_from_dict = Identity.from_dict(identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


