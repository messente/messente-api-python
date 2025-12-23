# RcsCardContent

RCS Card Content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the card content | [optional] 
**description** | **str** | Description of the card content | [optional] 
**media** | [**RcsMedia**](RcsMedia.md) |  | [optional] 
**suggestions** | [**List[RcsSuggestion]**](RcsSuggestion.md) | List of suggestions that the recipient can use to respond. | [optional] 

## Example

```python
from messente_api.models.rcs_card_content import RcsCardContent

# TODO update the JSON string below
json = "{}"
# create an instance of RcsCardContent from a JSON string
rcs_card_content_instance = RcsCardContent.from_json(json)
# print the JSON string representation of the object
print(RcsCardContent.to_json())

# convert the object into a dict
rcs_card_content_dict = rcs_card_content_instance.to_dict()
# create an instance of RcsCardContent from a dict
rcs_card_content_from_dict = RcsCardContent.from_dict(rcs_card_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


