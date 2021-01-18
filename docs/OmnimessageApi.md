# messente_api.OmnimessageApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_message**](OmnimessageApi.md#cancel_scheduled_message) | **DELETE** /omnimessage/{omnimessageId} | Cancels a scheduled Omnimessage
[**send_omnimessage**](OmnimessageApi.md#send_omnimessage) | **POST** /omnimessage | Sends an Omnimessage


# **cancel_scheduled_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} cancel_scheduled_message(omnimessage_id)

Cancels a scheduled Omnimessage

### Example

* Basic Authentication (basicAuth):
```python
import time
import messente_api
from messente_api.api import omnimessage_api
from messente_api.model.error_omnichannel import ErrorOmnichannel
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
    api_instance = omnimessage_api.OmnimessageApi(api_client)
    omnimessage_id = "omnimessageId_example" # str | UUID of the scheduled omnimessage to be cancelled

    # example passing only required values which don't have defaults set
    try:
        # Cancels a scheduled Omnimessage
        api_response = api_instance.cancel_scheduled_message(omnimessage_id)
        pprint(api_response)
    except messente_api.ApiException as e:
        print("Exception when calling OmnimessageApi->cancel_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage_id** | **str**| UUID of the scheduled omnimessage to be cancelled |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
import time
import messente_api
from messente_api.api import omnimessage_api
from messente_api.model.error_omnichannel import ErrorOmnichannel
from messente_api.model.omni_message_create_success_response import OmniMessageCreateSuccessResponse
from messente_api.model.omnimessage import Omnimessage
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
    api_instance = omnimessage_api.OmnimessageApi(api_client)
    omnimessage = Omnimessage(
        to="to_example",
        messages=[
            ,
        ],
        dlr_url="dlr_url_example",
        text_store=TextStore("nostore"),
        time_to_send=dateutil_parser('1970-01-01T00:00:00.00Z'),
        priority=Priority("low"),
    ) # Omnimessage | Omnimessage to be sent

    # example passing only required values which don't have defaults set
    try:
        # Sends an Omnimessage
        api_response = api_instance.send_omnimessage(omnimessage)
        pprint(api_response)
    except messente_api.ApiException as e:
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

