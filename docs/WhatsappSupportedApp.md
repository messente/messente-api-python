# WhatsappSupportedApp

Supported app for the button

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** | Package name | 
**signature_hash** | **str** | Signature hash | 

## Example

```python
from messente_api.models.whatsapp_supported_app import WhatsappSupportedApp

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappSupportedApp from a JSON string
whatsapp_supported_app_instance = WhatsappSupportedApp.from_json(json)
# print the JSON string representation of the object
print(WhatsappSupportedApp.to_json())

# convert the object into a dict
whatsapp_supported_app_dict = whatsapp_supported_app_instance.to_dict()
# create an instance of WhatsappSupportedApp from a dict
whatsapp_supported_app_from_dict = WhatsappSupportedApp.from_dict(whatsapp_supported_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


