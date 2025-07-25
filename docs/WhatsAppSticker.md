# WhatsAppSticker

WhatsApp sticker content. Either \"id\" or \"link\" must be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the sticker file. | [optional] 
**mime_type** | **str** | MIME type of the sticker file. | [optional] 
**animated** | **bool** | Indicates whether the sticker is animated. | [optional] 
**link** | **str** | URL link to the sticker file. | [optional] 

## Example

```python
from messente_api.models.whats_app_sticker import WhatsAppSticker

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppSticker from a JSON string
whats_app_sticker_instance = WhatsAppSticker.from_json(json)
# print the JSON string representation of the object
print(WhatsAppSticker.to_json())

# convert the object into a dict
whats_app_sticker_dict = whats_app_sticker_instance.to_dict()
# create an instance of WhatsAppSticker from a dict
whats_app_sticker_from_dict = WhatsAppSticker.from_dict(whats_app_sticker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


