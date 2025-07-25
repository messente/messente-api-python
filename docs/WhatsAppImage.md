# WhatsAppImage

WhatsApp image content. Either \"id\" or \"link\" must be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the image file. | [optional] 
**caption** | **str** | Caption for the image. | [optional] 
**mime_type** | **str** | MIME type of the image file. | [optional] 
**link** | **str** | URL link to the image file. | [optional] 

## Example

```python
from messente_api.models.whats_app_image import WhatsAppImage

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppImage from a JSON string
whats_app_image_instance = WhatsAppImage.from_json(json)
# print the JSON string representation of the object
print(WhatsAppImage.to_json())

# convert the object into a dict
whats_app_image_dict = whats_app_image_instance.to_dict()
# create an instance of WhatsAppImage from a dict
whats_app_image_from_dict = WhatsAppImage.from_dict(whats_app_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


