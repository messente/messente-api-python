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
import messente_api
from messente_api.models.numbers_to_investigate import NumbersToInvestigate
from messente_api.models.sync_number_lookup_success import SyncNumberLookupSuccess
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
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messente_api.NumberLookupApi(api_client)
    numbers_to_investigate = {"numbers":["+37251000000","+37251000001"]} # NumbersToInvestigate | Numbers for lookup

    try:
        # Requests info about phone numbers
        api_response = api_instance.fetch_info(numbers_to_investigate)
        print("The response of NumberLookupApi->fetch_info:\n")
        pprint(api_response)
    except Exception as e:
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

