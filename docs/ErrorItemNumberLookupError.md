# ErrorItemNumberLookupError

Error fields container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Error description | 
**code** | **int** | Matches the following error title.   This field is a constant  * 101 - Unauthorized * 102 - Invalid arguments or parameters * 103 - Server error * 104 - Crediting error #1 * 105 - Crediting error #2 * 106 - Client error | 

## Example

```python
from messente_api.models.error_item_number_lookup_error import ErrorItemNumberLookupError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorItemNumberLookupError from a JSON string
error_item_number_lookup_error_instance = ErrorItemNumberLookupError.from_json(json)
# print the JSON string representation of the object
print(ErrorItemNumberLookupError.to_json())

# convert the object into a dict
error_item_number_lookup_error_dict = error_item_number_lookup_error_instance.to_dict()
# create an instance of ErrorItemNumberLookupError from a dict
error_item_number_lookup_error_from_dict = ErrorItemNumberLookupError.from_dict(error_item_number_lookup_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


