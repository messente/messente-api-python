# RcsMedia

RCS media object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | [**RcsMediaHeight**](RcsMediaHeight.md) |  | 
**content_info** | [**RcsContentInfo**](RcsContentInfo.md) |  | 

## Example

```python
from messente_api.models.rcs_media import RcsMedia

# TODO update the JSON string below
json = "{}"
# create an instance of RcsMedia from a JSON string
rcs_media_instance = RcsMedia.from_json(json)
# print the JSON string representation of the object
print(RcsMedia.to_json())

# convert the object into a dict
rcs_media_dict = rcs_media_instance.to_dict()
# create an instance of RcsMedia from a dict
rcs_media_from_dict = RcsMedia.from_dict(rcs_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


