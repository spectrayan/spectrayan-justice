# Jury


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 
**name** | **str** | Name or identifier for the jury | 
**juror_ids** | **List[str]** | List of juror IDs that make up this jury | 
**foreman_id** | **str** | ID of the juror who is the foreman | [optional] 
**size** | **int** | Number of jurors in the jury | [optional] 
**status** | [**JuryStatus**](JuryStatus.md) |  | [optional] [default to JuryStatus.SELECTION]

## Example

```python
from justice_system.models.jury import Jury

# TODO update the JSON string below
json = "{}"
# create an instance of Jury from a JSON string
jury_instance = Jury.from_json(json)
# print the JSON string representation of the object
print(Jury.to_json())

# convert the object into a dict
jury_dict = jury_instance.to_dict()
# create an instance of Jury from a dict
jury_from_dict = Jury.from_dict(jury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


