# WhatsappTemplateButton

Whatsapp button object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WhatsappButtonType**](WhatsappButtonType.md) |  | [optional] 
**otp_type** | [**WhatsappOtpButtonType**](WhatsappOtpButtonType.md) |  | [optional] 
**autofill_text** | **str** | Text to be autofilled in the OTP field | [optional] 
**supported_apps** | [**List[WhatsappSupportedApp]**](WhatsappSupportedApp.md) | List of supported apps for the button | [optional] 
**text** | **str** | Text content of the button | [optional] 
**phone_number** | **str** | Phone number for the button | [optional] 
**url** | **str** | URL for the button | [optional] 

## Example

```python
from messente_api.models.whatsapp_template_button import WhatsappTemplateButton

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappTemplateButton from a JSON string
whatsapp_template_button_instance = WhatsappTemplateButton.from_json(json)
# print the JSON string representation of the object
print(WhatsappTemplateButton.to_json())

# convert the object into a dict
whatsapp_template_button_dict = whatsapp_template_button_instance.to_dict()
# create an instance of WhatsappTemplateButton from a dict
whatsapp_template_button_from_dict = WhatsappTemplateButton.from_dict(whatsapp_template_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


