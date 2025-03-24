# OmniMessageCreateSuccessResponse

A container for a response received after successfully created omnimessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[MessageResult]**](MessageResult.md) | List of messages that compose the omnimessage | 
**to** | **str** | Phone number in e.164 format | 
**omnimessage_id** | **str** | Unique identifier for the omnimessage | 

## Example

```python
from messente_api.models.omni_message_create_success_response import OmniMessageCreateSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OmniMessageCreateSuccessResponse from a JSON string
omni_message_create_success_response_instance = OmniMessageCreateSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(OmniMessageCreateSuccessResponse.to_json())

# convert the object into a dict
omni_message_create_success_response_dict = omni_message_create_success_response_instance.to_dict()
# create an instance of OmniMessageCreateSuccessResponse from a dict
omni_message_create_success_response_from_dict = OmniMessageCreateSuccessResponse.from_dict(omni_message_create_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


