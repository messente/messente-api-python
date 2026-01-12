# RcsSuggestedReply

RCS suggested reply.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text of the suggested reply. | 
**postback_data** | **str** | The postback data associated with the suggested reply. This is sent back to the sender when the user selects the suggested reply. | 

## Example

```python
from messente_api.models.rcs_suggested_reply import RcsSuggestedReply

# TODO update the JSON string below
json = "{}"
# create an instance of RcsSuggestedReply from a JSON string
rcs_suggested_reply_instance = RcsSuggestedReply.from_json(json)
# print the JSON string representation of the object
print(RcsSuggestedReply.to_json())

# convert the object into a dict
rcs_suggested_reply_dict = rcs_suggested_reply_instance.to_dict()
# create an instance of RcsSuggestedReply from a dict
rcs_suggested_reply_from_dict = RcsSuggestedReply.from_dict(rcs_suggested_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


