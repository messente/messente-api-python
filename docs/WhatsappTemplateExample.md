# WhatsappTemplateExample

Example of the templated content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_text** | **List[List[str]]** | Example of the templated text for the header | [optional] 
**body_text** | **List[List[str]]** | Example of the templated text for the body | [optional] 

## Example

```python
from messente_api.models.whatsapp_template_example import WhatsappTemplateExample

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappTemplateExample from a JSON string
whatsapp_template_example_instance = WhatsappTemplateExample.from_json(json)
# print the JSON string representation of the object
print(WhatsappTemplateExample.to_json())

# convert the object into a dict
whatsapp_template_example_dict = whatsapp_template_example_instance.to_dict()
# create an instance of WhatsappTemplateExample from a dict
whatsapp_template_example_from_dict = WhatsappTemplateExample.from_dict(whatsapp_template_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


