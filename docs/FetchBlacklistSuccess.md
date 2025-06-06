# FetchBlacklistSuccess

A container for blacklisted numbers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** | Array of unique phone numbers | [optional] 

## Example

```python
from messente_api.models.fetch_blacklist_success import FetchBlacklistSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of FetchBlacklistSuccess from a JSON string
fetch_blacklist_success_instance = FetchBlacklistSuccess.from_json(json)
# print the JSON string representation of the object
print(FetchBlacklistSuccess.to_json())

# convert the object into a dict
fetch_blacklist_success_dict = fetch_blacklist_success_instance.to_dict()
# create an instance of FetchBlacklistSuccess from a dict
fetch_blacklist_success_from_dict = FetchBlacklistSuccess.from_dict(fetch_blacklist_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


