# messente_api.NumberLookupApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_number_lookup**](NumberLookupApi.md#sync_number_lookup) | **POST** /hlr/sync | Requests info about a phone number


# **sync_number_lookup**
> SyncNumberLookupSuccess sync_number_lookup(sync_number_lookup)

Requests info about a phone number

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
api_instance = messente_api.NumberLookupApi(messente_api.ApiClient(configuration))
sync_number_lookup = {"numbers":["+37251000000","+37251000001"]} # SyncNumberLookup | Numbers to lookup

try:
    # Requests info about a phone number
    api_response = api_instance.sync_number_lookup(sync_number_lookup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberLookupApi->sync_number_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_number_lookup** | [**SyncNumberLookup**](SyncNumberLookup.md)| Numbers to lookup | 

### Return type

[**SyncNumberLookupSuccess**](SyncNumberLookupSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Info about phone numbers returned |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**402** | Failed crediting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

