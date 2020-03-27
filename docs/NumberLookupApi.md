# messente_api.NumberLookupApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_info**](NumberLookupApi.md#fetch_info) | **POST** /hlr/sync | Requests info about phone numbers


# **fetch_info**
> SyncNumberLookupSuccess fetch_info(numbers_to_investigate)

Requests info about phone numbers

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
    api_instance = messente_api.NumberLookupApi(api_client)
    numbers_to_investigate = {"numbers":["+37251000000","+37251000001"]} # NumbersToInvestigate | Numbers for lookup

    try:
        # Requests info about phone numbers
        api_response = api_instance.fetch_info(numbers_to_investigate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NumberLookupApi->fetch_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numbers_to_investigate** | [**NumbersToInvestigate**](NumbersToInvestigate.md)| Numbers for lookup | 

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

