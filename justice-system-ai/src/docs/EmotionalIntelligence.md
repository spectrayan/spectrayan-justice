# EmotionalIntelligence

Person's emotional intelligence assessment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_awareness** | **int** | Score for self-awareness (1-100). Measures ability to recognize and understand one&#39;s own emotions. | 
**self_regulation** | **int** | Score for self-regulation (1-100). Measures ability to control and redirect disruptive emotions. | 
**motivation** | **int** | Score for motivation (1-100). Measures passion to work for reasons beyond money or status. | 
**empathy** | **int** | Score for empathy (1-100). Measures ability to understand the emotional makeup of other people. | 
**social_skills** | **int** | Score for social skills (1-100). Measures proficiency in managing relationships and building networks. | 
**overall_eq_score** | **int** | Overall emotional intelligence quotient (EQ) score (1-100). | [optional] 
**emotional_strengths** | **List[str]** | List of emotional strengths. | [optional] 
**emotional_weaknesses** | **List[str]** | List of emotional weaknesses or areas for improvement. | [optional] 
**assessment_date** | **date** | The date when the emotional intelligence assessment was conducted. | [optional] 

## Example

```python
from generated.models.emotional_intelligence import EmotionalIntelligence

# TODO update the JSON string below
json = "{}"
# create an instance of EmotionalIntelligence from a JSON string
emotional_intelligence_instance = EmotionalIntelligence.from_json(json)
# print the JSON string representation of the object
print(EmotionalIntelligence.to_json())

# convert the object into a dict
emotional_intelligence_dict = emotional_intelligence_instance.to_dict()
# create an instance of EmotionalIntelligence from a dict
emotional_intelligence_from_dict = EmotionalIntelligence.from_dict(emotional_intelligence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


