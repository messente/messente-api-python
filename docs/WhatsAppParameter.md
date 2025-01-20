# WhatsAppParameter

Whatsapp component parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the parameter. | 
**text** | **str** | A text. | [optional] 
**currency** | [**WhatsAppCurrency**](WhatsAppCurrency.md) |  | [optional] 
**date_time** | [**WhatsAppDatetime**](WhatsAppDatetime.md) |  | [optional] 
**image** | [**WhatsAppMedia**](WhatsAppMedia.md) |  | [optional] 
**document** | [**WhatsAppMedia**](WhatsAppMedia.md) |  | [optional] 
**video** | [**WhatsAppMedia**](WhatsAppMedia.md) |  | [optional] 
**coupon_code** | **str** | A coupon code. | [optional] 
**payload** | **str** | A payload. | [optional] 

## Example

```python
from messente_api.models.whats_app_parameter import WhatsAppParameter

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppParameter from a JSON string
whats_app_parameter_instance = WhatsAppParameter.from_json(json)
# print the JSON string representation of the object
print(WhatsAppParameter.to_json())

# convert the object into a dict
whats_app_parameter_dict = whats_app_parameter_instance.to_dict()
# create an instance of WhatsAppParameter from a dict
whats_app_parameter_from_dict = WhatsAppParameter.from_dict(whats_app_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


