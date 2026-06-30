# ViberCarouselButton

Viber carousel button object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Button label text. | 
**action_url** | **str** | URL opened when the button is clicked. | 

## Example

```python
from messente_api.models.viber_carousel_button import ViberCarouselButton

# TODO update the JSON string below
json = "{}"
# create an instance of ViberCarouselButton from a JSON string
viber_carousel_button_instance = ViberCarouselButton.from_json(json)
# print the JSON string representation of the object
print(ViberCarouselButton.to_json())

# convert the object into a dict
viber_carousel_button_dict = viber_carousel_button_instance.to_dict()
# create an instance of ViberCarouselButton from a dict
viber_carousel_button_from_dict = ViberCarouselButton.from_dict(viber_carousel_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


