# WhatsappCreateTemplateRequest

Request to create a WhatsApp template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the template | 
**category** | [**WhatsappTemplateCategory**](WhatsappTemplateCategory.md) |  | 
**allow_category_change** | **bool** | Allow category change | [optional] [default to False]
**language** | **str** | Language of the template | 
**components** | [**List[WhatsappTemplateComponent]**](WhatsappTemplateComponent.md) | List of template components | 

## Example

```python
from messente_api.models.whatsapp_create_template_request import WhatsappCreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappCreateTemplateRequest from a JSON string
whatsapp_create_template_request_instance = WhatsappCreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(WhatsappCreateTemplateRequest.to_json())

# convert the object into a dict
whatsapp_create_template_request_dict = whatsapp_create_template_request_instance.to_dict()
# create an instance of WhatsappCreateTemplateRequest from a dict
whatsapp_create_template_request_from_dict = WhatsappCreateTemplateRequest.from_dict(whatsapp_create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


