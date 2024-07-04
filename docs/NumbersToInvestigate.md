# NumbersToInvestigate

A container for phone numbers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **List[str]** | A list of phone numbers. Max 10 numbers per request | 

## Example

```python
from messente_api.models.numbers_to_investigate import NumbersToInvestigate

# TODO update the JSON string below
json = "{}"
# create an instance of NumbersToInvestigate from a JSON string
numbers_to_investigate_instance = NumbersToInvestigate.from_json(json)
# print the JSON string representation of the object
print(NumbersToInvestigate.to_json())

# convert the object into a dict
numbers_to_investigate_dict = numbers_to_investigate_instance.to_dict()
# create an instance of NumbersToInvestigate from a dict
numbers_to_investigate_from_dict = NumbersToInvestigate.from_dict(numbers_to_investigate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


