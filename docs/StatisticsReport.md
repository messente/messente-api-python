# StatisticsReport

Report for one country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **int** | Sum of all messages | 
**total_price** | **str** | Price for all messages | 
**country** | **str** | Target country of all messages | 

## Example

```python
from messente_api.models.statistics_report import StatisticsReport

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsReport from a JSON string
statistics_report_instance = StatisticsReport.from_json(json)
# print the JSON string representation of the object
print(StatisticsReport.to_json())

# convert the object into a dict
statistics_report_dict = statistics_report_instance.to_dict()
# create an instance of StatisticsReport from a dict
statistics_report_from_dict = StatisticsReport.from_dict(statistics_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


