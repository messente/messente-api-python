# RcsLatLng

Latitude and longitude coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude coordinate. | 
**longitude** | **float** | The longitude coordinate. | 

## Example

```python
from messente_api.models.rcs_lat_lng import RcsLatLng

# TODO update the JSON string below
json = "{}"
# create an instance of RcsLatLng from a JSON string
rcs_lat_lng_instance = RcsLatLng.from_json(json)
# print the JSON string representation of the object
print(RcsLatLng.to_json())

# convert the object into a dict
rcs_lat_lng_dict = rcs_lat_lng_instance.to_dict()
# create an instance of RcsLatLng from a dict
rcs_lat_lng_from_dict = RcsLatLng.from_dict(rcs_lat_lng_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


