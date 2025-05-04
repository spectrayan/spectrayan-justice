# Reporter


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
**certification_number** | **str** | Court reporter&#39;s certification number | 
**email** | **str** | Reporter&#39;s email address | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**court_id** | **str** | ID of the court the reporter is associated with | [optional] 
**years_of_experience** | **int** | Number of years of experience as a court reporter | [optional] 
**specializations** | **List[str]** | Areas of specialization or expertise | [optional] 
**transcription_rate** | **float** | Rate charged per page for transcription services | [optional] 

## Example

```python
from justice_system.models.reporter import Reporter

# TODO update the JSON string below
json = "{}"
# create an instance of Reporter from a JSON string
reporter_instance = Reporter.from_json(json)
# print the JSON string representation of the object
print(Reporter.to_json())

# convert the object into a dict
reporter_dict = reporter_instance.to_dict()
# create an instance of Reporter from a dict
reporter_from_dict = Reporter.from_dict(reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


