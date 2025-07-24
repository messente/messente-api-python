# WhatsApp

WhatsApp message content.   Only one of \"text\", \"image\", \"document\" or \"audio\" can be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is   considered as failed and the next channel is attempted | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted.       Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**template** | [**WhatsAppTemplate**](WhatsAppTemplate.md) |  | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'whatsapp']
**text** | [**WhatsAppText**](WhatsAppText.md) |  | [optional] 
**image** | [**WhatsAppImage**](WhatsAppImage.md) |  | [optional] 
**video** | [**WhatsAppVideo**](WhatsAppVideo.md) |  | [optional] 
**audio** | [**WhatsAppAudio**](WhatsAppAudio.md) |  | [optional] 
**document** | [**WhatsAppDocument**](WhatsAppDocument.md) |  | [optional] 
**sticker** | [**WhatsAppSticker**](WhatsAppSticker.md) |  | [optional] 

## Example

```python
from messente_api.models.whats_app import WhatsApp

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsApp from a JSON string
whats_app_instance = WhatsApp.from_json(json)
# print the JSON string representation of the object
print(WhatsApp.to_json())

# convert the object into a dict
whats_app_dict = whats_app_instance.to_dict()
# create an instance of WhatsApp from a dict
whats_app_from_dict = WhatsApp.from_dict(whats_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


