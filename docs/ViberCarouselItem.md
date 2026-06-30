# ViberCarouselItem

Viber carousel item object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Carousel item title. | 
**image_url** | **str** | URL of the carousel item image. | 
**primary_button** | [**ViberCarouselButton**](ViberCarouselButton.md) |  | 
**secondary_button** | [**ViberCarouselButton**](ViberCarouselButton.md) |  | [optional] 

## Example

```python
from messente_api.models.viber_carousel_item import ViberCarouselItem

# TODO update the JSON string below
json = "{}"
# create an instance of ViberCarouselItem from a JSON string
viber_carousel_item_instance = ViberCarouselItem.from_json(json)
# print the JSON string representation of the object
print(ViberCarouselItem.to_json())

# convert the object into a dict
viber_carousel_item_dict = viber_carousel_item_instance.to_dict()
# create an instance of ViberCarouselItem from a dict
viber_carousel_item_from_dict = ViberCarouselItem.from_dict(viber_carousel_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


