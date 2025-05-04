# Case


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document id auto generated | [optional] [readonly] 
**created_by** | **str** | The principal that created the entity containing the field. | [optional] [readonly] 
**created_at** | **datetime** | The date and time the entity containing the field was created. | [optional] [readonly] 
**updated_by** | **str** | The principal that recently modified the entity containing the field. | [optional] [readonly] 
**updated_at** | **datetime** | The date the entity containing the field was recently modified. | [optional] [readonly] 
**case_number** | **str** | Unique case number assigned by the court | 
**title** | **str** | Title or name of the case | 
**description** | **str** | Brief description of the case | [optional] 
**type** | [**CaseType**](CaseType.md) |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | [optional] [default to CaseStatus.PENDING]
**filing_date** | **date** | Date the case was filed | 
**court_id** | **str** | ID of the court handling the case | 
**judge_id** | **str** | ID of the judge presiding over the case | [optional] 
**prosecutor_ids** | **List[str]** | IDs of prosecutors assigned to the case | [optional] 
**defense_attorney_ids** | **List[str]** | IDs of defense attorneys assigned to the case | [optional] 
**defendant_ids** | **List[str]** | IDs of defendants in the case | [optional] 
**plaintiff_ids** | **List[str]** | IDs of plaintiffs in the case | [optional] 
**victim_ids** | **List[str]** | IDs of victims in the case | [optional] 
**witness_ids** | **List[str]** | IDs of witnesses in the case | [optional] 
**jury_id** | **str** | ID of the jury assigned to the case | [optional] 
**clerk_id** | **str** | ID of the clerk assigned to the case | [optional] 
**bailiff_id** | **str** | ID of the bailiff assigned to the case | [optional] 
**reporter_id** | **str** | ID of the court reporter assigned to the case | [optional] 
**evidence_ids** | **List[str]** | IDs of evidence associated with the case | [optional] 
**hearing_dates** | **List[datetime]** | Dates of scheduled hearings | [optional] 
**verdict** | **str** | Verdict of the case if concluded | [optional] 
**sentence_details** | **str** | Details of the sentence if applicable | [optional] 

## Example

```python
from generated.models.case import Case

# TODO update the JSON string below
json = "{}"
# create an instance of Case from a JSON string
case_instance = Case.from_json(json)
# print the JSON string representation of the object
print(Case.to_json())

# convert the object into a dict
case_dict = case_instance.to_dict()
# create an instance of Case from a dict
case_from_dict = Case.from_dict(case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


