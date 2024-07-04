# ErrorItemPhonebook

A container for Phonebook API error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**ErrorTitlePhonebook**](ErrorTitlePhonebook.md) |  | 
**detail** | **str** | Free form more detailed description of the error | 
**code** | [**ErrorCodePhonebook**](ErrorCodePhonebook.md) |  | 

## Example

```python
from messente_api.models.error_item_phonebook import ErrorItemPhonebook

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorItemPhonebook from a JSON string
error_item_phonebook_instance = ErrorItemPhonebook.from_json(json)
# print the JSON string representation of the object
print(ErrorItemPhonebook.to_json())

# convert the object into a dict
error_item_phonebook_dict = error_item_phonebook_instance.to_dict()
# create an instance of ErrorItemPhonebook from a dict
error_item_phonebook_from_dict = ErrorItemPhonebook.from_dict(error_item_phonebook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


