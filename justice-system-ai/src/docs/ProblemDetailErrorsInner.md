# ProblemDetailErrorsInner

An object to provide explicit details on a problem towards an API consumer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A granular description on the specific error related to a body property, query parameter, path parameters, and/or header. | 
**pointer** | **str** | A JSON Pointer to a specific request body property that is the source of error. | [optional] 
**parameter** | **str** | The name of the query or path parameter that is the source of error. | [optional] 
**header** | **str** | The name of the header that is the source of error. | [optional] 
**code** | **str** | A string containing additional provider specific codes to identify the error context. | [optional] 

## Example

```python
from generated.models.problem_detail_errors_inner import ProblemDetailErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetailErrorsInner from a JSON string
problem_detail_errors_inner_instance = ProblemDetailErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ProblemDetailErrorsInner.to_json())

# convert the object into a dict
problem_detail_errors_inner_dict = problem_detail_errors_inner_instance.to_dict()
# create an instance of ProblemDetailErrorsInner from a dict
problem_detail_errors_inner_from_dict = ProblemDetailErrorsInner.from_dict(problem_detail_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


