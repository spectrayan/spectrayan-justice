# CustodyRecord

Record of evidence custody transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_date** | **datetime** | Date and time of custody transfer | 
**from_person_id** | **str** | ID of the person transferring custody | 
**to_person_id** | **str** | ID of the person receiving custody | 
**reason** | **str** | Reason for the custody transfer | [optional] 
**location** | **str** | Location where the transfer occurred | [optional] 
**notes** | **str** | Additional notes about the transfer | [optional] 

## Example

```python
from generated.models.custody_record import CustodyRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CustodyRecord from a JSON string
custody_record_instance = CustodyRecord.from_json(json)
# print the JSON string representation of the object
print(CustodyRecord.to_json())

# convert the object into a dict
custody_record_dict = custody_record_instance.to_dict()
# create an instance of CustodyRecord from a dict
custody_record_from_dict = CustodyRecord.from_dict(custody_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


