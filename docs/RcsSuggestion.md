# RcsSuggestion

Exactly one of reply or action must be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply** | [**RcsSuggestedReply**](RcsSuggestedReply.md) |  | [optional] 
**action** | [**RcsSuggestedAction**](RcsSuggestedAction.md) |  | [optional] 

## Example

```python
from messente_api.models.rcs_suggestion import RcsSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of RcsSuggestion from a JSON string
rcs_suggestion_instance = RcsSuggestion.from_json(json)
# print the JSON string representation of the object
print(RcsSuggestion.to_json())

# convert the object into a dict
rcs_suggestion_dict = rcs_suggestion_instance.to_dict()
# create an instance of RcsSuggestion from a dict
rcs_suggestion_from_dict = RcsSuggestion.from_dict(rcs_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


