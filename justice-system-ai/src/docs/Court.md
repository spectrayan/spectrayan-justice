# Court


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 
**name** | **str** | Name of the court | 
**type** | [**CourtType**](CourtType.md) |  | 
**jurisdiction** | **str** | Jurisdiction of the court | 
**address** | [**Address**](Address.md) |  | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**email** | **str** | Court&#39;s email address | [optional] 

## Example

```python
from generated.models.court import Court

# TODO update the JSON string below
json = "{}"
# create an instance of Court from a JSON string
court_instance = Court.from_json(json)
# print the JSON string representation of the object
print(Court.to_json())

# convert the object into a dict
court_dict = court_instance.to_dict()
# create an instance of Court from a dict
court_from_dict = Court.from_dict(court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


