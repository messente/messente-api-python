# ViberVideo

Viber video object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL pointing to the video resource. | 
**thumbnail** | **str** | URL pointing to the video thumbnail resource. | 
**file_size** | **int** | Size of the video file in bytes. Cannot be larger than 200MB. | 
**duration** | [**List[WhatsAppParameter]**](WhatsAppParameter.md) | Duration of the video in seconds. Cannot be longer than 600 seconds. | 

## Example

```python
from messente_api.models.viber_video import ViberVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ViberVideo from a JSON string
viber_video_instance = ViberVideo.from_json(json)
# print the JSON string representation of the object
print(ViberVideo.to_json())

# convert the object into a dict
viber_video_dict = viber_video_instance.to_dict()
# create an instance of ViberVideo from a dict
viber_video_from_dict = ViberVideo.from_dict(viber_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


