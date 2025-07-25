# messente_api.AccountBalanceApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balance**](AccountBalanceApi.md#get_account_balance) | **GET** /get_balance | Get account balance
[**get_account_balance_using_post**](AccountBalanceApi.md#get_account_balance_using_post) | **POST** /get_balance | Get account balance


# **get_account_balance**
> str get_account_balance(username, password)

Get account balance

### Example

* Api Key Authentication (apiPassword):
* Api Key Authentication (apiUsername):

```python
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

# Configure API key authorization: apiPassword
configuration.api_key['apiPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiPassword'] = 'Bearer'

# Configure API key authorization: apiUsername
configuration.api_key['apiUsername'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiUsername'] = 'Bearer'

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messente_api.AccountBalanceApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password

    try:
        # Get account balance
        api_response = api_instance.get_account_balance(username, password)
        print("The response of AccountBalanceApi->get_account_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBalanceApi->get_account_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The API username | 
 **password** | **str**| The API password | 

### Return type

**str**

### Authorization

[apiPassword](../README.md#apiPassword), [apiUsername](../README.md#apiUsername)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Both errors and success responses are returned as plain text with HTTP status 200. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balance_using_post**
> str get_account_balance_using_post(username, password)

Get account balance

### Example

* Api Key Authentication (apiPassword):
* Api Key Authentication (apiUsername):

```python
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

# Configure API key authorization: apiPassword
configuration.api_key['apiPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiPassword'] = 'Bearer'

# Configure API key authorization: apiUsername
configuration.api_key['apiUsername'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiUsername'] = 'Bearer'

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messente_api.AccountBalanceApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password

    try:
        # Get account balance
        api_response = api_instance.get_account_balance_using_post(username, password)
        print("The response of AccountBalanceApi->get_account_balance_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBalanceApi->get_account_balance_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The API username | 
 **password** | **str**| The API password | 

### Return type

**str**

### Authorization

[apiPassword](../README.md#apiPassword), [apiUsername](../README.md#apiUsername)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Both errors and success responses are returned as plain text with HTTP status 200. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

