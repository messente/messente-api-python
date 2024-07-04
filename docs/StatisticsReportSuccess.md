# StatisticsReportSuccess

A container for statistics reports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[StatisticsReport]**](StatisticsReport.md) | Array of report objects | 

## Example

```python
from messente_api.models.statistics_report_success import StatisticsReportSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsReportSuccess from a JSON string
statistics_report_success_instance = StatisticsReportSuccess.from_json(json)
# print the JSON string representation of the object
print(StatisticsReportSuccess.to_json())

# convert the object into a dict
statistics_report_success_dict = statistics_report_success_instance.to_dict()
# create an instance of StatisticsReportSuccess from a dict
statistics_report_success_from_dict = StatisticsReportSuccess.from_dict(statistics_report_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


