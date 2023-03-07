# messente_api.DeliveryReportApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_delivery_report**](DeliveryReportApi.md#retrieve_delivery_report) | **GET** /omnimessage/{omnimessageId}/status | Retrieves the delivery report for the Omnimessage


# **retrieve_delivery_report**
> DeliveryReportResponse retrieve_delivery_report(omnimessage_id)

Retrieves the delivery report for the Omnimessage

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import messente_api
from messente_api.rest import ApiException
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
    api_instance = messente_api.DeliveryReportApi(api_client)
    omnimessage_id = 'omnimessage_id_example' # str | UUID of the omnimessage to for which the delivery report is to be retrieved

    try:
        # Retrieves the delivery report for the Omnimessage
        api_response = api_instance.retrieve_delivery_report(omnimessage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryReportApi->retrieve_delivery_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage_id** | **str**| UUID of the omnimessage to for which the delivery report is to be retrieved | 

### Return type

[**DeliveryReportResponse**](DeliveryReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delivery report success |  -  |
**401** | Unauthorized |  -  |
**404** | If no such message exists or you do not have access to the particular message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

