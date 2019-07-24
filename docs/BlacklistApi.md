# messente_api.BlacklistApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_blacklist**](BlacklistApi.md#add_to_blacklist) | **POST** /phonebook/blacklist | Adds a phone number to the blacklist
[**delete_from_blacklist**](BlacklistApi.md#delete_from_blacklist) | **DELETE** /phonebook/blacklist/{phone} | Deletes a phone number from the blacklist
[**fetch_blacklist**](BlacklistApi.md#fetch_blacklist) | **GET** /phonebook/blacklist | Returns all blacklisted phone numbers
[**is_blacklisted**](BlacklistApi.md#is_blacklisted) | **GET** /phonebook/blacklist/{phone} | Checks if a phone number is blacklisted


# **add_to_blacklist**
> add_to_blacklist(number_to_blacklist)

Adds a phone number to the blacklist

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
api_instance = messente_api.BlacklistApi(messente_api.ApiClient(configuration))
number_to_blacklist = {"phoneNumber":"+37251000000"} # NumberToBlacklist | Phone number to be blacklisted

try:
    # Adds a phone number to the blacklist
    api_instance.add_to_blacklist(number_to_blacklist)
except ApiException as e:
    print("Exception when calling BlacklistApi->add_to_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_to_blacklist** | [**NumberToBlacklist**](NumberToBlacklist.md)| Phone number to be blacklisted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Phone number added to the blacklist |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**409** | Phone number already blacklisted |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_from_blacklist**
> delete_from_blacklist(phone)

Deletes a phone number from the blacklist

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
api_instance = messente_api.BlacklistApi(messente_api.ApiClient(configuration))
phone = '+37251000000' # str | A phone number

try:
    # Deletes a phone number from the blacklist
    api_instance.delete_from_blacklist(phone)
except ApiException as e:
    print("Exception when calling BlacklistApi->delete_from_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| A phone number | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Phone number deleted from the blacklist |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Phone number is not in the blacklist |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_blacklist**
> FetchBlacklistSuccess fetch_blacklist()

Returns all blacklisted phone numbers

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
api_instance = messente_api.BlacklistApi(messente_api.ApiClient(configuration))

try:
    # Returns all blacklisted phone numbers
    api_response = api_instance.fetch_blacklist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistApi->fetch_blacklist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FetchBlacklistSuccess**](FetchBlacklistSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a list of blacklisted phone numbers |  -  |
**401** | Unauthorized |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_blacklisted**
> is_blacklisted(phone)

Checks if a phone number is blacklisted

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
api_instance = messente_api.BlacklistApi(messente_api.ApiClient(configuration))
phone = '+37251000000' # str | A phone number

try:
    # Checks if a phone number is blacklisted
    api_instance.is_blacklisted(phone)
except ApiException as e:
    print("Exception when calling BlacklistApi->is_blacklisted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| A phone number | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Phone number is in the blacklist |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Phone number is not in the blacklist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

