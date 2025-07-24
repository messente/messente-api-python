# WhatsAppVideo

WhatsApp video content. Either \"id\" or \"link\" must be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the video file. | [optional] 
**caption** | **str** | Caption for the video. | [optional] 
**mime_type** | **str** | MIME type of the video file. | [optional] 
**link** | **str** | URL link to the video file. | [optional] 

## Example

```python
from messente_api.models.whats_app_video import WhatsAppVideo

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppVideo from a JSON string
whats_app_video_instance = WhatsAppVideo.from_json(json)
# print the JSON string representation of the object
print(WhatsAppVideo.to_json())

# convert the object into a dict
whats_app_video_dict = whats_app_video_instance.to_dict()
# create an instance of WhatsAppVideo from a dict
whats_app_video_from_dict = WhatsAppVideo.from_dict(whats_app_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


