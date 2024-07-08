# Telegram

Telegram message content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is considered as failed and the next channel is attempted | [optional] 
**text** | **str** | Plaintext content for Telegram | [optional] 
**image_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;document_url\&quot; and \&quot;audio_url\&quot; | [optional] 
**document_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;audio_url\&quot; and \&quot;image_url\&quot; | [optional] 
**audio_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;document_url\&quot; and \&quot;image_url\&quot; | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'telegram']

## Example

```python
from messente_api.models.telegram import Telegram

# TODO update the JSON string below
json = "{}"
# create an instance of Telegram from a JSON string
telegram_instance = Telegram.from_json(json)
# print the JSON string representation of the object
print(Telegram.to_json())

# convert the object into a dict
telegram_dict = telegram_instance.to_dict()
# create an instance of Telegram from a dict
telegram_from_dict = Telegram.from_dict(telegram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


