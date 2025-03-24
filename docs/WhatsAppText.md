# WhatsAppText

A text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_url** | **bool** | Whether to display link preview if the message contains a hyperlink | [optional] [default to True]
**body** | **str** | Plaintext content for WhatsApp, can contain URLs, emojis and formatting | 

## Example

```python
from messente_api.models.whats_app_text import WhatsAppText

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppText from a JSON string
whats_app_text_instance = WhatsAppText.from_json(json)
# print the JSON string representation of the object
print(WhatsAppText.to_json())

# convert the object into a dict
whats_app_text_dict = whats_app_text_instance.to_dict()
# create an instance of WhatsAppText from a dict
whats_app_text_from_dict = WhatsAppText.from_dict(whats_app_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


