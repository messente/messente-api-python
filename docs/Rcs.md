# Rcs

RCS message object. Exactly one of 'text', 'content_info' or 'rich_card' must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'rcs']
**sender** | **str** | Phone number or alphanumeric sender name | 
**validity** | **int** | After how many minutes this channel is considered as failed and the next channel is attempted.Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted. Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**text** | **str** | Text content of the RCS message | [optional] 
**suggestions** | [**List[RcsSuggestion]**](RcsSuggestion.md) | List of suggestions to include with the message | [optional] 
**rich_card** | [**RcsRichCard**](RcsRichCard.md) |  | [optional] 
**content_info** | [**RcsContentInfo**](RcsContentInfo.md) |  | [optional] 

## Example

```python
from messente_api.models.rcs import Rcs

# TODO update the JSON string below
json = "{}"
# create an instance of Rcs from a JSON string
rcs_instance = Rcs.from_json(json)
# print the JSON string representation of the object
print(Rcs.to_json())

# convert the object into a dict
rcs_dict = rcs_instance.to_dict()
# create an instance of Rcs from a dict
rcs_from_dict = Rcs.from_dict(rcs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


