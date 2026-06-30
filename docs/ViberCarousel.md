# ViberCarousel

Viber carousel object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ViberCarouselItem]**](ViberCarouselItem.md) | Carousel items. Must contain between 2 and 5 items. | 

## Example

```python
from messente_api.models.viber_carousel import ViberCarousel

# TODO update the JSON string below
json = "{}"
# create an instance of ViberCarousel from a JSON string
viber_carousel_instance = ViberCarousel.from_json(json)
# print the JSON string representation of the object
print(ViberCarousel.to_json())

# convert the object into a dict
viber_carousel_dict = viber_carousel_instance.to_dict()
# create an instance of ViberCarousel from a dict
viber_carousel_from_dict = ViberCarousel.from_dict(viber_carousel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


