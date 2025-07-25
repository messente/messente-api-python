# WhatsAppAudio

WhatsApp audio content. Either \"id\" or \"link\" must be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the audio file. | [optional] 
**mime_type** | **str** | MIME type of the audio file. | [optional] 
**link** | **str** | URL link to the audio file. | [optional] 

## Example

```python
from messente_api.models.whats_app_audio import WhatsAppAudio

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppAudio from a JSON string
whats_app_audio_instance = WhatsAppAudio.from_json(json)
# print the JSON string representation of the object
print(WhatsAppAudio.to_json())

# convert the object into a dict
whats_app_audio_dict = whats_app_audio_instance.to_dict()
# create an instance of WhatsAppAudio from a dict
whats_app_audio_from_dict = WhatsAppAudio.from_dict(whats_app_audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


