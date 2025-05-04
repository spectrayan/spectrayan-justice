# SocialBehavior

Person's social behavior patterns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_style** | [**CommunicationStyle**](CommunicationStyle.md) |  | 
**social_network_size** | [**SocialNetworkSize**](SocialNetworkSize.md) |  | [optional] 
**conflict_resolution_style** | [**ConflictResolutionStyle**](ConflictResolutionStyle.md) |  | 
**leadership_style** | [**LeadershipStyle**](LeadershipStyle.md) |  | [optional] 
**teamwork_ability** | **int** | Score for ability to work in teams (1-100). | 
**social_influence** | **int** | Score for ability to influence others (1-100). | [optional] 
**trust_level** | [**TrustLevel**](TrustLevel.md) |  | [optional] 
**social_adaptability** | **int** | Score for adaptability in social situations (1-100). | [optional] 
**cultural_sensitivity** | **int** | Score for sensitivity to cultural differences (1-100). | [optional] 
**social_behavior_notes** | **str** | Additional notes about social behavior. | [optional] 

## Example

```python
from generated.models.social_behavior import SocialBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of SocialBehavior from a JSON string
social_behavior_instance = SocialBehavior.from_json(json)
# print the JSON string representation of the object
print(SocialBehavior.to_json())

# convert the object into a dict
social_behavior_dict = social_behavior_instance.to_dict()
# create an instance of SocialBehavior from a dict
social_behavior_from_dict = SocialBehavior.from_dict(social_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


