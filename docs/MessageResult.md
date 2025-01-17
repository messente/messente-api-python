# MessageResult

A message part of an omnimessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Unique identifier for the message | 
**channel** | [**Channel**](Channel.md) |  | 
**sender** | **str** | Sender that was used for the message | 

## Example

```python
from messente_api.models.message_result import MessageResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageResult from a JSON string
message_result_instance = MessageResult.from_json(json)
# print the JSON string representation of the object
print(MessageResult.to_json())

# convert the object into a dict
message_result_dict = message_result_instance.to_dict()
# create an instance of MessageResult from a dict
message_result_from_dict = MessageResult.from_dict(message_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


