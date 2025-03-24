# ErrorItemStatistics

Error fields container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Error title | 
**details** | **str** | Error details | 
**code** | [**ErrorCodeStatistics**](ErrorCodeStatistics.md) |  | 

## Example

```python
from messente_api.models.error_item_statistics import ErrorItemStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorItemStatistics from a JSON string
error_item_statistics_instance = ErrorItemStatistics.from_json(json)
# print the JSON string representation of the object
print(ErrorItemStatistics.to_json())

# convert the object into a dict
error_item_statistics_dict = error_item_statistics_instance.to_dict()
# create an instance of ErrorItemStatistics from a dict
error_item_statistics_from_dict = ErrorItemStatistics.from_dict(error_item_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


