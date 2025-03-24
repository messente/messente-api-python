# NumberToBlacklist

A container for a soon-to-be blacklisted number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number in e.164 format | 

## Example

```python
from messente_api.models.number_to_blacklist import NumberToBlacklist

# TODO update the JSON string below
json = "{}"
# create an instance of NumberToBlacklist from a JSON string
number_to_blacklist_instance = NumberToBlacklist.from_json(json)
# print the JSON string representation of the object
print(NumberToBlacklist.to_json())

# convert the object into a dict
number_to_blacklist_dict = number_to_blacklist_instance.to_dict()
# create an instance of NumberToBlacklist from a dict
number_to_blacklist_from_dict = NumberToBlacklist.from_dict(number_to_blacklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


