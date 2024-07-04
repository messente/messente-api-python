# StatisticsReportSettings

A container for statistics report settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date for the report | 
**end_date** | **date** | End date for the report | 
**message_types** | **List[str]** | Optional list of message types (sms, viber, whatsapp, hlr, telegram) | [optional] 

## Example

```python
from messente_api.models.statistics_report_settings import StatisticsReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsReportSettings from a JSON string
statistics_report_settings_instance = StatisticsReportSettings.from_json(json)
# print the JSON string representation of the object
print(StatisticsReportSettings.to_json())

# convert the object into a dict
statistics_report_settings_dict = statistics_report_settings_instance.to_dict()
# create an instance of StatisticsReportSettings from a dict
statistics_report_settings_from_dict = StatisticsReportSettings.from_dict(statistics_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


