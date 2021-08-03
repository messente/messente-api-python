# messente_api.OmnimessageApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_message**](OmnimessageApi.md#cancel_scheduled_message) | **DELETE** /omnimessage/{omnimessageId} | Cancels a scheduled Omnimessage
[**send_omnimessage**](OmnimessageApi.md#send_omnimessage) | **POST** /omnimessage | Sends an Omnimessage


# **cancel_scheduled_message**
> object cancel_scheduled_message(omnimessage_id)

Cancels a scheduled Omnimessage

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
    api_instance = messente_api.OmnimessageApi(api_client)
    omnimessage_id = 'omnimessage_id_example' # str | UUID of the scheduled omnimessage to be cancelled

    try:
        # Cancels a scheduled Omnimessage
        api_response = api_instance.cancel_scheduled_message(omnimessage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OmnimessageApi->cancel_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage_id** | **str**| UUID of the scheduled omnimessage to be cancelled | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Scheduled omnimessage successfully cancelled |  -  |
**404** | If the omnimessage has already been sent or no such message exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_omnimessage**
> OmniMessageCreateSuccessResponse send_omnimessage(omnimessage)

Sends an Omnimessage

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
    api_instance = messente_api.OmnimessageApi(api_client)
    omnimessage = messente_api.Omnimessage() # Omnimessage | Omnimessage to be sent

    try:
        # Sends an Omnimessage
        api_response = api_instance.send_omnimessage(omnimessage)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OmnimessageApi->send_omnimessage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage** | [**Omnimessage**](Omnimessage.md)| Omnimessage to be sent | 

### Return type

[**OmniMessageCreateSuccessResponse**](OmniMessageCreateSuccessResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Omnimessage success response |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

