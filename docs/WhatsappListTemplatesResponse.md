# WhatsappListTemplatesResponse

Whatsapp Cloud API list of templates response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[WhatsappTemplateResponse]**](WhatsappTemplateResponse.md) | List of templates | 
**paging** | [**WhatsappPagination**](WhatsappPagination.md) |  | 

## Example

```python
from messente_api.models.whatsapp_list_templates_response import WhatsappListTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappListTemplatesResponse from a JSON string
whatsapp_list_templates_response_instance = WhatsappListTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(WhatsappListTemplatesResponse.to_json())

# convert the object into a dict
whatsapp_list_templates_response_dict = whatsapp_list_templates_response_instance.to_dict()
# create an instance of WhatsappListTemplatesResponse from a dict
whatsapp_list_templates_response_from_dict = WhatsappListTemplatesResponse.from_dict(whatsapp_list_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


