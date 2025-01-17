# WhatsAppCurrency

Whatsapp currency object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_value** | **str** | Default text if localization fails. | 
**code** | **str** | Currency code as defined in ISO 4217. | 
**amount_1000** | **str** | Amount multiplied by 1000. | 

## Example

```python
from messente_api.models.whats_app_currency import WhatsAppCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppCurrency from a JSON string
whats_app_currency_instance = WhatsAppCurrency.from_json(json)
# print the JSON string representation of the object
print(WhatsAppCurrency.to_json())

# convert the object into a dict
whats_app_currency_dict = whats_app_currency_instance.to_dict()
# create an instance of WhatsAppCurrency from a dict
whats_app_currency_from_dict = WhatsAppCurrency.from_dict(whats_app_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


