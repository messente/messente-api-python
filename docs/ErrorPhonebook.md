# ErrorPhonebook

A container for errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorItemPhonebook]**](ErrorItemPhonebook.md) | An array of errors | 

## Example

```python
from messente_api.models.error_phonebook import ErrorPhonebook

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorPhonebook from a JSON string
error_phonebook_instance = ErrorPhonebook.from_json(json)
# print the JSON string representation of the object
print(ErrorPhonebook.to_json())

# convert the object into a dict
error_phonebook_dict = error_phonebook_instance.to_dict()
# create an instance of ErrorPhonebook from a dict
error_phonebook_from_dict = ErrorPhonebook.from_dict(error_phonebook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


