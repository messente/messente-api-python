# WhatsappTemplateResponse

Whatsapp Cloud API template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template ID | 
**components** | [**List[WhatsappTemplateComponent]**](WhatsappTemplateComponent.md) | List of template components | 
**language** | **str** | Language of the template | 
**name** | **str** | Name of the template | 
**category** | [**WhatsappTemplateCategory**](WhatsappTemplateCategory.md) |  | 
**status** | [**WhatsappTemplateStatus**](WhatsappTemplateStatus.md) |  | 

## Example

```python
from messente_api.models.whatsapp_template_response import WhatsappTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappTemplateResponse from a JSON string
whatsapp_template_response_instance = WhatsappTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(WhatsappTemplateResponse.to_json())

# convert the object into a dict
whatsapp_template_response_dict = whatsapp_template_response_instance.to_dict()
# create an instance of WhatsappTemplateResponse from a dict
whatsapp_template_response_from_dict = WhatsappTemplateResponse.from_dict(whatsapp_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


