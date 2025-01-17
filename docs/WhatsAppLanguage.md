# WhatsAppLanguage

Whatsapp template language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Language code | 
**policy** | **str** | Language policy | [optional] 

## Example

```python
from messente_api.models.whats_app_language import WhatsAppLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppLanguage from a JSON string
whats_app_language_instance = WhatsAppLanguage.from_json(json)
# print the JSON string representation of the object
print(WhatsAppLanguage.to_json())

# convert the object into a dict
whats_app_language_dict = whats_app_language_instance.to_dict()
# create an instance of WhatsAppLanguage from a dict
whats_app_language_from_dict = WhatsAppLanguage.from_dict(whats_app_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


