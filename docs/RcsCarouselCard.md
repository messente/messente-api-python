# RcsCarouselCard

RCS Carousel Card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_width** | [**RcsCardWidth**](RcsCardWidth.md) |  | 
**card_contents** | [**List[RcsCardContent]**](RcsCardContent.md) | The contents of the carousel card. | 

## Example

```python
from messente_api.models.rcs_carousel_card import RcsCarouselCard

# TODO update the JSON string below
json = "{}"
# create an instance of RcsCarouselCard from a JSON string
rcs_carousel_card_instance = RcsCarouselCard.from_json(json)
# print the JSON string representation of the object
print(RcsCarouselCard.to_json())

# convert the object into a dict
rcs_carousel_card_dict = rcs_carousel_card_instance.to_dict()
# create an instance of RcsCarouselCard from a dict
rcs_carousel_card_from_dict = RcsCarouselCard.from_dict(rcs_carousel_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


