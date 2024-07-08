# WhatsAppComponent

Whatsapp template component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the component | 
**sub_type** | **str** | Sub-type of the component | [optional] 
**index** | **int** | index used to position buttons | [optional] 
**parameters** | [**List[WhatsAppParameter]**](WhatsAppParameter.md) | List of parameters for the component | [optional] 

## Example

```python
from messente_api.models.whats_app_component import WhatsAppComponent

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppComponent from a JSON string
whats_app_component_instance = WhatsAppComponent.from_json(json)
# print the JSON string representation of the object
print(WhatsAppComponent.to_json())

# convert the object into a dict
whats_app_component_dict = whats_app_component_instance.to_dict()
# create an instance of WhatsAppComponent from a dict
whats_app_component_from_dict = WhatsAppComponent.from_dict(whats_app_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


