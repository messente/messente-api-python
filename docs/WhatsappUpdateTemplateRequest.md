# WhatsappUpdateTemplateRequest

Request to create a WhatsApp template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**WhatsappTemplateCategory**](WhatsappTemplateCategory.md) |  | [optional] 
**components** | [**List[WhatsappTemplateComponent]**](WhatsappTemplateComponent.md) | List of template components | [optional] 

## Example

```python
from messente_api.models.whatsapp_update_template_request import WhatsappUpdateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappUpdateTemplateRequest from a JSON string
whatsapp_update_template_request_instance = WhatsappUpdateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(WhatsappUpdateTemplateRequest.to_json())

# convert the object into a dict
whatsapp_update_template_request_dict = whatsapp_update_template_request_instance.to_dict()
# create an instance of WhatsappUpdateTemplateRequest from a dict
whatsapp_update_template_request_from_dict = WhatsappUpdateTemplateRequest.from_dict(whatsapp_update_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


