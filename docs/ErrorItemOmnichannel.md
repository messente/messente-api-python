# ErrorItemOmnichannel

A container for Omnichannel API error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**ErrorTitleOmnichannel**](ErrorTitleOmnichannel.md) |  | 
**detail** | **str** | Free form more detailed description of the error | 
**code** | [**ErrorCodeOmnichannel**](ErrorCodeOmnichannel.md) |  | 
**source** | **str** | Describes which field is causing the issue in the payload, null for non 400 status code responses | 

## Example

```python
from messente_api.models.error_item_omnichannel import ErrorItemOmnichannel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorItemOmnichannel from a JSON string
error_item_omnichannel_instance = ErrorItemOmnichannel.from_json(json)
# print the JSON string representation of the object
print(ErrorItemOmnichannel.to_json())

# convert the object into a dict
error_item_omnichannel_dict = error_item_omnichannel_instance.to_dict()
# create an instance of ErrorItemOmnichannel from a dict
error_item_omnichannel_from_dict = ErrorItemOmnichannel.from_dict(error_item_omnichannel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


