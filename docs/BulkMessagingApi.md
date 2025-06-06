# messente_api.BulkMessagingApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_bulk_omnimessage**](BulkMessagingApi.md#send_bulk_omnimessage) | **POST** /omnimessages | Sends a bulk Omnimessage


# **send_bulk_omnimessage**
> BulkOmniMessageCreateSuccessResponse send_bulk_omnimessage(bulk_omnimessage)

Sends a bulk Omnimessage

### Example

* Basic Authentication (basicAuth):

```python
import messente_api
from messente_api.models.bulk_omni_message_create_success_response import BulkOmniMessageCreateSuccessResponse
from messente_api.models.bulk_omnimessage import BulkOmnimessage
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
    api_instance = messente_api.BulkMessagingApi(api_client)
    bulk_omnimessage = messente_api.BulkOmnimessage() # BulkOmnimessage | Bulk Omnimessage to be sent

    try:
        # Sends a bulk Omnimessage
        api_response = api_instance.send_bulk_omnimessage(bulk_omnimessage)
        print("The response of BulkMessagingApi->send_bulk_omnimessage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkMessagingApi->send_bulk_omnimessage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_omnimessage** | [**BulkOmnimessage**](BulkOmnimessage.md)| Bulk Omnimessage to be sent | 

### Return type

[**BulkOmniMessageCreateSuccessResponse**](BulkOmniMessageCreateSuccessResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bulk Omnimessage success response |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

