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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.messente.com/v1
configuration.host = "https://api.messente.com/v1"
# Create an instance of the API class
api_instance = messente_api.DeliveryReportApi(messente_api.ApiClient(configuration))
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
**404** | If no such message exists or you do not have access to the particular message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

