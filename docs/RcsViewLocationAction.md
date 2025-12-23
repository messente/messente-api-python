# RcsViewLocationAction

Action to view a location on a map.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat_long** | [**RcsLatLng**](RcsLatLng.md) |  | [optional] 
**label** | **str** | The label of the pin dropped at latLong. | [optional] 
**query** | **str** | (Optional, only supported on Android Messages clients) Instead of specifying a latLong (and optionally, a label), the agent can specify a query string. For default map apps that support search functionality (including Google Maps), tapping this suggested action results in a location search centered around the user&#39;s current location.              For instance, setting the query string to \&quot;Growing Tree Bank\&quot; will show all Growing Tree Bank locations in the user&#39;s vicinity. Setting the query string to \&quot;1600 Amphitheater Parkway, Mountain View, CA 94043\&quot; will select that specific address, regardless of the user&#39;s location.        | [optional] 

## Example

```python
from messente_api.models.rcs_view_location_action import RcsViewLocationAction

# TODO update the JSON string below
json = "{}"
# create an instance of RcsViewLocationAction from a JSON string
rcs_view_location_action_instance = RcsViewLocationAction.from_json(json)
# print the JSON string representation of the object
print(RcsViewLocationAction.to_json())

# convert the object into a dict
rcs_view_location_action_dict = rcs_view_location_action_instance.to_dict()
# create an instance of RcsViewLocationAction from a dict
rcs_view_location_action_from_dict = RcsViewLocationAction.from_dict(rcs_view_location_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


