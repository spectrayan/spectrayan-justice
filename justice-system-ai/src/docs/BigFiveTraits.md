# BigFiveTraits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openness** | **int** | Score for openness to experience (1-100). Higher scores indicate greater openness to new experiences, creativity, and intellectual curiosity. | 
**conscientiousness** | **int** | Score for conscientiousness (1-100). Higher scores indicate greater organization, responsibility, and self-discipline. | 
**extraversion** | **int** | Score for extraversion (1-100). Higher scores indicate greater sociability, assertiveness, and energy. | 
**agreeableness** | **int** | Score for agreeableness (1-100). Higher scores indicate greater compassion, cooperation, and consideration for others. | 
**neuroticism** | **int** | Score for neuroticism (1-100). Higher scores indicate greater emotional instability and tendency toward negative emotions. | 
**assessment_date** | **date** | The date when the Big Five traits assessment was conducted. | [optional] 
**assessment_method** | **str** | The method or tool used to assess the Big Five traits. | [optional] 

## Example

```python
from generated.models.big_five_traits import BigFiveTraits

# TODO update the JSON string below
json = "{}"
# create an instance of BigFiveTraits from a JSON string
big_five_traits_instance = BigFiveTraits.from_json(json)
# print the JSON string representation of the object
print(BigFiveTraits.to_json())

# convert the object into a dict
big_five_traits_dict = big_five_traits_instance.to_dict()
# create an instance of BigFiveTraits from a dict
big_five_traits_from_dict = BigFiveTraits.from_dict(big_five_traits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


