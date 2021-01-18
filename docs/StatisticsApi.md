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
import time
import messente_api
from messente_api.api import statistics_api
from messente_api.model.statistics_report_success import StatisticsReportSuccess
from messente_api.model.statistics_report_settings import StatisticsReportSettings
from messente_api.model.error_statistics import ErrorStatistics
from pprint import pprint
# Defining the host is optional and defaults to https://api.messente.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = messente_api.Configuration(
    host = "https://api.messente.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = messente_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
    statistics_report_settings = StatisticsReportSettings(
        start_date=dateutil_parser('1970-01-01').date(),
        end_date=dateutil_parser('1970-01-01').date(),
        message_types=[
            "message_types_example",
        ],
    ) # StatisticsReportSettings | Settings for statistics report

    # example passing only required values which don't have defaults set
    try:
        # Requests statistics reports for each country
        api_response = api_instance.create_statistics_report(statistics_report_settings)
        pprint(api_response)
    except messente_api.ApiException as e:
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

