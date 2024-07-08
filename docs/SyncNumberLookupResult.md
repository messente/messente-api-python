# SyncNumberLookupResult

Info about a phone number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Phone number in e.164 format | 
**roaming** | **bool** | Indicates if a number is roaming | [optional] 
**ported** | **bool** | Indicates if a number is ported | [optional] 
**roaming_network** | [**MobileNetwork**](MobileNetwork.md) |  | [optional] 
**current_network** | [**MobileNetwork**](MobileNetwork.md) |  | [optional] 
**original_network** | [**MobileNetwork**](MobileNetwork.md) |  | [optional] 
**ported_network** | [**MobileNetwork**](MobileNetwork.md) |  | [optional] 
**status** | **str** | Status of the phone number | [optional] 
**error** | **object** | Indicates if any error occurred while handling the request | [optional] 

## Example

```python
from messente_api.models.sync_number_lookup_result import SyncNumberLookupResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyncNumberLookupResult from a JSON string
sync_number_lookup_result_instance = SyncNumberLookupResult.from_json(json)
# print the JSON string representation of the object
print(SyncNumberLookupResult.to_json())

# convert the object into a dict
sync_number_lookup_result_dict = sync_number_lookup_result_instance.to_dict()
# create an instance of SyncNumberLookupResult from a dict
sync_number_lookup_result_from_dict = SyncNumberLookupResult.from_dict(sync_number_lookup_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


