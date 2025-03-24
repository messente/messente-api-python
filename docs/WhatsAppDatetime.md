# WhatsAppDatetime

Whatsapp datetime object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_value** | **str** | Default text. | 

## Example

```python
from messente_api.models.whats_app_datetime import WhatsAppDatetime

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppDatetime from a JSON string
whats_app_datetime_instance = WhatsAppDatetime.from_json(json)
# print the JSON string representation of the object
print(WhatsAppDatetime.to_json())

# convert the object into a dict
whats_app_datetime_dict = whats_app_datetime_instance.to_dict()
# create an instance of WhatsAppDatetime from a dict
whats_app_datetime_from_dict = WhatsAppDatetime.from_dict(whats_app_datetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


