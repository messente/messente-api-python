# RcsRichCard

RCS rich card object. Exactly one of \"standalone_card\" and \"carousel_card\" must be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standalone_card** | [**RcsStandaloneCard**](RcsStandaloneCard.md) |  | [optional] 
**carousel_card** | [**RcsCarouselCard**](RcsCarouselCard.md) |  | [optional] 

## Example

```python
from messente_api.models.rcs_rich_card import RcsRichCard

# TODO update the JSON string below
json = "{}"
# create an instance of RcsRichCard from a JSON string
rcs_rich_card_instance = RcsRichCard.from_json(json)
# print the JSON string representation of the object
print(RcsRichCard.to_json())

# convert the object into a dict
rcs_rich_card_dict = rcs_rich_card_instance.to_dict()
# create an instance of RcsRichCard from a dict
rcs_rich_card_from_dict = RcsRichCard.from_dict(rcs_rich_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


