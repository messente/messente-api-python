# ViberTemplate

Viber template object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template ID. | 
**lang** | **str** | Template language code. | 
**params** | **Dict[str, str]** | Optional template parameters as key-value string pairs. | [optional] 

## Example

```python
from messente_api.models.viber_template import ViberTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ViberTemplate from a JSON string
viber_template_instance = ViberTemplate.from_json(json)
# print the JSON string representation of the object
print(ViberTemplate.to_json())

# convert the object into a dict
viber_template_dict = viber_template_instance.to_dict()
# create an instance of ViberTemplate from a dict
viber_template_from_dict = ViberTemplate.from_dict(viber_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


