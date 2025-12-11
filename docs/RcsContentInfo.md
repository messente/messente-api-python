# RcsContentInfo

RCS content info object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Required file URL | 
**thumbnail_url** | **str** | Optional thumbnail URL | [optional] 
**force_refresh** | **bool** | Force refresh the content | 

## Example

```python
from messente_api.models.rcs_content_info import RcsContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RcsContentInfo from a JSON string
rcs_content_info_instance = RcsContentInfo.from_json(json)
# print the JSON string representation of the object
print(RcsContentInfo.to_json())

# convert the object into a dict
rcs_content_info_dict = rcs_content_info_instance.to_dict()
# create an instance of RcsContentInfo from a dict
rcs_content_info_from_dict = RcsContentInfo.from_dict(rcs_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


