# SyncNumberLookupSuccess

A container for number lookup response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | ID of the request | 
**result** | [**List[SyncNumberLookupResult]**](SyncNumberLookupResult.md) | A container for phone number info objects | 

## Example

```python
from messente_api.models.sync_number_lookup_success import SyncNumberLookupSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of SyncNumberLookupSuccess from a JSON string
sync_number_lookup_success_instance = SyncNumberLookupSuccess.from_json(json)
# print the JSON string representation of the object
print(SyncNumberLookupSuccess.to_json())

# convert the object into a dict
sync_number_lookup_success_dict = sync_number_lookup_success_instance.to_dict()
# create an instance of SyncNumberLookupSuccess from a dict
sync_number_lookup_success_from_dict = SyncNumberLookupSuccess.from_dict(sync_number_lookup_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


