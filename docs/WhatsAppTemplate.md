# WhatsAppTemplate

Whatsapp Cloud API template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the template | 
**language** | [**WhatsAppLanguage**](WhatsAppLanguage.md) |  | 
**components** | [**List[WhatsAppComponent]**](WhatsAppComponent.md) | List of template components | [optional] 

## Example

```python
from messente_api.models.whats_app_template import WhatsAppTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppTemplate from a JSON string
whats_app_template_instance = WhatsAppTemplate.from_json(json)
# print the JSON string representation of the object
print(WhatsAppTemplate.to_json())

# convert the object into a dict
whats_app_template_dict = whats_app_template_instance.to_dict()
# create an instance of WhatsAppTemplate from a dict
whats_app_template_from_dict = WhatsAppTemplate.from_dict(whats_app_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


