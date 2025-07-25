# WhatsappCreateTemplateResponse

Response for creating a WhatsApp template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template ID | 
**status** | [**WhatsappTemplateStatus**](WhatsappTemplateStatus.md) |  | 
**category** | [**WhatsappTemplateCategory**](WhatsappTemplateCategory.md) |  | 

## Example

```python
from messente_api.models.whatsapp_create_template_response import WhatsappCreateTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappCreateTemplateResponse from a JSON string
whatsapp_create_template_response_instance = WhatsappCreateTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(WhatsappCreateTemplateResponse.to_json())

# convert the object into a dict
whatsapp_create_template_response_dict = whatsapp_create_template_response_instance.to_dict()
# create an instance of WhatsappCreateTemplateResponse from a dict
whatsapp_create_template_response_from_dict = WhatsappCreateTemplateResponse.from_dict(whatsapp_create_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


