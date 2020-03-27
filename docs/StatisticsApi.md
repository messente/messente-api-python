# messente_api.StatisticsApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_statistics_report**](StatisticsApi.md#create_statistics_report) | **POST** /statistics/reports | Requests statistics reports for each country


# **create_statistics_report**
> StatisticsReportSuccess create_statistics_report(statistics_report_settings)

Requests statistics reports for each country

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import messente_api
from messente_api.rest import ApiException
from pprint import pprint
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.messente.com/v1
configuration.host = "https://api.messente.com/v1"

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messente_api.StatisticsApi(api_client)
    statistics_report_settings = {"start_date":"2017-01-01","end_date":"2019-06-20","message_types":["sms"]} # StatisticsReportSettings | Settings for statistics report

    try:
        # Requests statistics reports for each country
        api_response = api_instance.create_statistics_report(statistics_report_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->create_statistics_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_report_settings** | [**StatisticsReportSettings**](StatisticsReportSettings.md)| Settings for statistics report | 

### Return type

[**StatisticsReportSuccess**](StatisticsReportSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created reports by countries |  -  |
**400** | Client Error |  -  |
**401** | Unauthorized |  -  |
**422** | Invalid data |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

