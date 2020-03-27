# messente_api.GroupsApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /phonebook/groups | Creates a new group with the provided name
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /phonebook/groups/{groupId} | Deletes a group
[**fetch_group**](GroupsApi.md#fetch_group) | **GET** /phonebook/groups/{groupId} | Lists a group
[**fetch_groups**](GroupsApi.md#fetch_groups) | **GET** /phonebook/groups | Returns all groups
[**update_group**](GroupsApi.md#update_group) | **PUT** /phonebook/groups/{groupId} | Updates a group with the provided name


# **create_group**
> GroupEnvelope create_group(group_name)

Creates a new group with the provided name

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
    api_instance = messente_api.GroupsApi(api_client)
    group_name = {"name":"Any group name"} # GroupName | 

    try:
        # Creates a new group with the provided name
        api_response = api_instance.create_group(group_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | [**GroupName**](GroupName.md)|  | 

### Return type

[**GroupEnvelope**](GroupEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An object containing a group object |  -  |
**400** | Name is invalid string or shorter than length 1 |  -  |
**401** | Unauthorized |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Deletes a group

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
    api_instance = messente_api.GroupsApi(api_client)
    group_id = '5792a02a-e5c2-422b-a0a0-0ae65d814663' # str | String in UUID format

    try:
        # Deletes a group
        api_instance.delete_group(group_id)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in UUID format | 

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
**204** | Group deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Group missing |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_group**
> GroupEnvelope fetch_group(group_id)

Lists a group

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
    api_instance = messente_api.GroupsApi(api_client)
    group_id = '5792a02a-e5c2-422b-a0a0-0ae65d814663' # str | String in UUID format

    try:
        # Lists a group
        api_response = api_instance.fetch_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->fetch_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in UUID format | 

### Return type

[**GroupEnvelope**](GroupEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a group object |  -  |
**401** | Unauthorized |  -  |
**404** | Missing group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_groups**
> GroupListEnvelope fetch_groups()

Returns all groups

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
    api_instance = messente_api.GroupsApi(api_client)
    
    try:
        # Returns all groups
        api_response = api_instance.fetch_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->fetch_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupListEnvelope**](GroupListEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a list of group objects |  -  |
**401** | Unauthorized |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GroupEnvelope update_group(group_id, group_name)

Updates a group with the provided name

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
    api_instance = messente_api.GroupsApi(api_client)
    group_id = '5792a02a-e5c2-422b-a0a0-0ae65d814663' # str | String in UUID format
group_name = {"name":"Any group name"} # GroupName | 

    try:
        # Updates a group with the provided name
        api_response = api_instance.update_group(group_id, group_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in UUID format | 
 **group_name** | [**GroupName**](GroupName.md)|  | 

### Return type

[**GroupEnvelope**](GroupEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a group object |  -  |
**400** | Name is invalid string or shorter than length 1 |  -  |
**401** | Unauthorized |  -  |
**404** | Group missing |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

