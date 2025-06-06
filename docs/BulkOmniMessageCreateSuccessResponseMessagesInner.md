# BulkOmniMessageCreateSuccessResponseMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[MessageResult]**](MessageResult.md) | List of messages that compose the omnimessage | 
**to** | **str** | Phone number in e.164 format | 
**omnimessage_id** | **str** | Unique identifier for the omnimessage | 
**errors** | [**List[ErrorItemOmnichannel]**](ErrorItemOmnichannel.md) | An array of errors | 

## Example

```python
from messente_api.models.bulk_omni_message_create_success_response_messages_inner import BulkOmniMessageCreateSuccessResponseMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOmniMessageCreateSuccessResponseMessagesInner from a JSON string
bulk_omni_message_create_success_response_messages_inner_instance = BulkOmniMessageCreateSuccessResponseMessagesInner.from_json(json)
# print the JSON string representation of the object
print(BulkOmniMessageCreateSuccessResponseMessagesInner.to_json())

# convert the object into a dict
bulk_omni_message_create_success_response_messages_inner_dict = bulk_omni_message_create_success_response_messages_inner_instance.to_dict()
# create an instance of BulkOmniMessageCreateSuccessResponseMessagesInner from a dict
bulk_omni_message_create_success_response_messages_inner_from_dict = BulkOmniMessageCreateSuccessResponseMessagesInner.from_dict(bulk_omni_message_create_success_response_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


