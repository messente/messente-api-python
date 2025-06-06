# ErrorStatistics

A container for errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorItemStatistics]**](ErrorItemStatistics.md) | An array of errors | 

## Example

```python
from messente_api.models.error_statistics import ErrorStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorStatistics from a JSON string
error_statistics_instance = ErrorStatistics.from_json(json)
# print the JSON string representation of the object
print(ErrorStatistics.to_json())

# convert the object into a dict
error_statistics_dict = error_statistics_instance.to_dict()
# create an instance of ErrorStatistics from a dict
error_statistics_from_dict = ErrorStatistics.from_dict(error_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


