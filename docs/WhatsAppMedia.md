# WhatsAppMedia

Whatsapp media object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The media object ID. Do not use this field when message type is set to text. | [optional] 
**link** | **str** | The protocol and URL of the media to be sent. Use only with HTTP/HTTPS URLs.       Do not use this field when message type is set to text. | [optional] 
**caption** | **str** | Media asset caption. Do not use with audio or sticker media. | [optional] 
**filename** | **str** | Describes the filename for the specific document. Use only with document media. | [optional] 

## Example

```python
from messente_api.models.whats_app_media import WhatsAppMedia

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppMedia from a JSON string
whats_app_media_instance = WhatsAppMedia.from_json(json)
# print the JSON string representation of the object
print(WhatsAppMedia.to_json())

# convert the object into a dict
whats_app_media_dict = whats_app_media_instance.to_dict()
# create an instance of WhatsAppMedia from a dict
whats_app_media_from_dict = WhatsAppMedia.from_dict(whats_app_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


