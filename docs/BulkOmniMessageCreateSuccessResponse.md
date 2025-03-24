# BulkOmniMessageCreateSuccessResponse

Response received after successfully created bulk omnimessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[BulkOmniMessageCreateSuccessResponseMessagesInner]**](BulkOmniMessageCreateSuccessResponseMessagesInner.md) | List of responses for each Omnimessage in the bulk. These can be errors or successful responses | 

## Example

```python
from messente_api.models.bulk_omni_message_create_success_response import BulkOmniMessageCreateSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOmniMessageCreateSuccessResponse from a JSON string
bulk_omni_message_create_success_response_instance = BulkOmniMessageCreateSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(BulkOmniMessageCreateSuccessResponse.to_json())

# convert the object into a dict
bulk_omni_message_create_success_response_dict = bulk_omni_message_create_success_response_instance.to_dict()
# create an instance of BulkOmniMessageCreateSuccessResponse from a dict
bulk_omni_message_create_success_response_from_dict = BulkOmniMessageCreateSuccessResponse.from_dict(bulk_omni_message_create_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


