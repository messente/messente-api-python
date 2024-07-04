# ErrorNumberLookup

A container for errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorItemNumberLookup]**](ErrorItemNumberLookup.md) | An array of errors | 

## Example

```python
from messente_api.models.error_number_lookup import ErrorNumberLookup

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorNumberLookup from a JSON string
error_number_lookup_instance = ErrorNumberLookup.from_json(json)
# print the JSON string representation of the object
print(ErrorNumberLookup.to_json())

# convert the object into a dict
error_number_lookup_dict = error_number_lookup_instance.to_dict()
# create an instance of ErrorNumberLookup from a dict
error_number_lookup_from_dict = ErrorNumberLookup.from_dict(error_number_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


