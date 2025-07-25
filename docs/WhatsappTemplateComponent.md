# WhatsappTemplateComponent

Template component object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WhatsappComponentType**](WhatsappComponentType.md) |  | [optional] 
**format** | [**WhatsappHeaderFormat**](WhatsappHeaderFormat.md) |  | [optional] 
**text** | **str** | Text content of the component | [optional] 
**example** | [**WhatsappTemplateExample**](WhatsappTemplateExample.md) |  | [optional] 
**buttons** | [**List[WhatsappTemplateButton]**](WhatsappTemplateButton.md) | List of buttons for the component | [optional] 

## Example

```python
from messente_api.models.whatsapp_template_component import WhatsappTemplateComponent

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappTemplateComponent from a JSON string
whatsapp_template_component_instance = WhatsappTemplateComponent.from_json(json)
# print the JSON string representation of the object
print(WhatsappTemplateComponent.to_json())

# convert the object into a dict
whatsapp_template_component_dict = whatsapp_template_component_instance.to_dict()
# create an instance of WhatsappTemplateComponent from a dict
whatsapp_template_component_from_dict = WhatsappTemplateComponent.from_dict(whatsapp_template_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


