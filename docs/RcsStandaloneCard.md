# RcsStandaloneCard

RCS standalone card object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_orientation** | [**RcsCardOrientation**](RcsCardOrientation.md) |  | 
**thumbnail_image_alignment** | [**RcsImageAlignment**](RcsImageAlignment.md) |  | 
**card_content** | [**RcsCardContent**](RcsCardContent.md) |  | 

## Example

```python
from messente_api.models.rcs_standalone_card import RcsStandaloneCard

# TODO update the JSON string below
json = "{}"
# create an instance of RcsStandaloneCard from a JSON string
rcs_standalone_card_instance = RcsStandaloneCard.from_json(json)
# print the JSON string representation of the object
print(RcsStandaloneCard.to_json())

# convert the object into a dict
rcs_standalone_card_dict = rcs_standalone_card_instance.to_dict()
# create an instance of RcsStandaloneCard from a dict
rcs_standalone_card_from_dict = RcsStandaloneCard.from_dict(rcs_standalone_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


