# ErrorOmnichannel

A container for errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorItemOmnichannel]**](ErrorItemOmnichannel.md) | An array of errors | 

## Example

```python
from messente_api.models.error_omnichannel import ErrorOmnichannel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorOmnichannel from a JSON string
error_omnichannel_instance = ErrorOmnichannel.from_json(json)
# print the JSON string representation of the object
print(ErrorOmnichannel.to_json())

# convert the object into a dict
error_omnichannel_dict = error_omnichannel_instance.to_dict()
# create an instance of ErrorOmnichannel from a dict
error_omnichannel_from_dict = ErrorOmnichannel.from_dict(error_omnichannel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


