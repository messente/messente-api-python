# ErrorItemNumberLookup

A container for Number Lookup API error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorItemNumberLookupError**](ErrorItemNumberLookupError.md) |  | 

## Example

```python
from messente_api.models.error_item_number_lookup import ErrorItemNumberLookup

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorItemNumberLookup from a JSON string
error_item_number_lookup_instance = ErrorItemNumberLookup.from_json(json)
# print the JSON string representation of the object
print(ErrorItemNumberLookup.to_json())

# convert the object into a dict
error_item_number_lookup_dict = error_item_number_lookup_instance.to_dict()
# create an instance of ErrorItemNumberLookup from a dict
error_item_number_lookup_from_dict = ErrorItemNumberLookup.from_dict(error_item_number_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


