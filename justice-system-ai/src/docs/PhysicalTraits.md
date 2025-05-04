# PhysicalTraits

Person's physical characteristics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height in centimeters. | 
**weight** | **float** | Weight in kilograms. | 
**eye_color** | [**EyeColor**](EyeColor.md) |  | 
**hair_color** | [**HairColor**](HairColor.md) |  | 
**blood_type** | [**BloodType**](BloodType.md) |  | [optional] 
**distinguishing_features** | **List[str]** | List of distinguishing physical features. | [optional] 
**physical_condition** | [**PhysicalCondition**](PhysicalCondition.md) |  | [optional] 
**disabilities** | **List[str]** | List of physical disabilities, if any. | [optional] 
**medical_conditions** | **List[str]** | List of medical conditions, if any. | [optional] 

## Example

```python
from generated.models.physical_traits import PhysicalTraits

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalTraits from a JSON string
physical_traits_instance = PhysicalTraits.from_json(json)
# print the JSON string representation of the object
print(PhysicalTraits.to_json())

# convert the object into a dict
physical_traits_dict = physical_traits_instance.to_dict()
# create an instance of PhysicalTraits from a dict
physical_traits_from_dict = PhysicalTraits.from_dict(physical_traits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


