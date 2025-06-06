# messente_api.PricingApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pricelist**](PricingApi.md#get_pricelist) | **GET** /pricelist | Get pricelist for account
[**get_prices**](PricingApi.md#get_prices) | **GET** /prices | Get pricing for a specific country


# **get_pricelist**
> str get_pricelist(username, password)

Get pricelist for account

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
    api_instance = messente_api.PricingApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password

    try:
        # Get pricelist for account
        api_response = api_instance.get_pricelist(username, password)
        print("The response of PricingApi->get_pricelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->get_pricelist: %s\n" % e)
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
**200** | Both errors and success responses are returned as plain text with HTTP status 200. Unsuccessful responses contain the error code, while successful ones contain the pricelist in CSV format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices**
> Price get_prices(username, password, country, format=format)

Get pricing for a specific country

### Example

* Api Key Authentication (apiPassword):
* Api Key Authentication (apiUsername):

```python
import messente_api
from messente_api.models.price import Price
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
    api_instance = messente_api.PricingApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password
    country = 'country_example' # str | The country code, for which to get the prices
    format = 'format_example' # str | The format of the response. Can be either 'json' or 'xml'. If not specified, defaults to 'json'. (optional)

    try:
        # Get pricing for a specific country
        api_response = api_instance.get_prices(username, password, country, format=format)
        print("The response of PricingApi->get_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->get_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The API username | 
 **password** | **str**| The API password | 
 **country** | **str**| The country code, for which to get the prices | 
 **format** | **str**| The format of the response. Can be either &#39;json&#39; or &#39;xml&#39;. If not specified, defaults to &#39;json&#39;. | [optional] 

### Return type

[**Price**](Price.md)

### Authorization

[apiPassword](../README.md#apiPassword), [apiUsername](../README.md#apiUsername)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsuccessful responses are returned as plain text with an error code, while successful ones contain either JSON or XML depending on the user&#39;s choice. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

