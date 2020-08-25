# messente_api.ContactsApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_to_group**](ContactsApi.md#add_contact_to_group) | **POST** /phonebook/groups/{groupId}/contacts/{phone} | Adds a contact to a group
[**create_contact**](ContactsApi.md#create_contact) | **POST** /phonebook/contacts | Creates a new contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /phonebook/contacts/{phone} | Deletes a contact
[**fetch_contact**](ContactsApi.md#fetch_contact) | **GET** /phonebook/contacts/{phone} | Lists a contact
[**fetch_contact_groups**](ContactsApi.md#fetch_contact_groups) | **GET** /phonebook/contacts/{phone}/groups | Lists groups of a contact
[**fetch_contacts**](ContactsApi.md#fetch_contacts) | **GET** /phonebook/contacts | Returns all contacts
[**remove_contact_from_group**](ContactsApi.md#remove_contact_from_group) | **DELETE** /phonebook/groups/{groupId}/contacts/{phone} | Removes a contact from a group
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /phonebook/contacts/{phone} | Updates a contact


# **add_contact_to_group**
> object add_contact_to_group(group_id, phone)

Adds a contact to a group

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
    api_instance = messente_api.ContactsApi(api_client)
    group_id = '5792a02a-e5c2-422b-a0a0-0ae65d814663' # str | String in UUID format
phone = '+37251000000' # str | A phone number

    try:
        # Adds a contact to a group
        api_response = api_instance.add_contact_to_group(group_id, phone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->add_contact_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in UUID format | 
 **phone** | **str**| A phone number | 

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
**201** | An empty object |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact or group is missing |  -  |
**409** | Contact already added to group |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ContactEnvelope create_contact(contact_fields)

Creates a new contact

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
    api_instance = messente_api.ContactsApi(api_client)
    contact_fields = {"phoneNumber":"+37251000000","email":"anyone@messente.com","firstName":"Any","lastName":"One","company":"Messente","title":"Sir","custom":"Any custom","custom2":"Any custom two","custom3":"Any custom three","custom4":"Any custom four"} # ContactFields | 

    try:
        # Creates a new contact
        api_response = api_instance.create_contact(contact_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_fields** | [**ContactFields**](ContactFields.md)|  | 

### Return type

[**ContactEnvelope**](ContactEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An object containing a contact object |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**409** | Contact with phone already created |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(phone)

Deletes a contact

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
    api_instance = messente_api.ContactsApi(api_client)
    phone = '+37251000000' # str | A phone number

    try:
        # Deletes a contact
        api_instance.delete_contact(phone)
    except ApiException as e:
        print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
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
**204** | Contact deleted |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact missing |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_contact**
> ContactEnvelope fetch_contact(phone)

Lists a contact

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
    api_instance = messente_api.ContactsApi(api_client)
    phone = '+37251000000' # str | A phone number

    try:
        # Lists a contact
        api_response = api_instance.fetch_contact(phone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->fetch_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| A phone number | 

### Return type

[**ContactEnvelope**](ContactEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a contact object |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_contact_groups**
> GroupListEnvelope fetch_contact_groups(phone)

Lists groups of a contact

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
    api_instance = messente_api.ContactsApi(api_client)
    phone = '+37251000000' # str | A phone number

    try:
        # Lists groups of a contact
        api_response = api_instance.fetch_contact_groups(phone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->fetch_contact_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| A phone number | 

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
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_contacts**
> ContactListEnvelope fetch_contacts(group_ids=group_ids)

Returns all contacts

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
    api_instance = messente_api.ContactsApi(api_client)
    group_ids = ['[\"5792a02a-e5c2-422b-a0a0-0ae65d814663\",\"4792a02a-e5c2-422b-a0a0-0ae65d814662\"]'] # list[str] | Optional one or many group id strings in UUID format. For example: \"/contacts?groupIds=group_id_one&groupIds=group_id_two\"  (optional)

    try:
        # Returns all contacts
        api_response = api_instance.fetch_contacts(group_ids=group_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->fetch_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_ids** | [**list[str]**](str.md)| Optional one or many group id strings in UUID format. For example: \&quot;/contacts?groupIds&#x3D;group_id_one&amp;groupIds&#x3D;group_id_two\&quot;  | [optional] 

### Return type

[**ContactListEnvelope**](ContactListEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a list of contact objects |  -  |
**400** | Invalid \&quot;groupIds\&quot; parameters provided |  -  |
**401** | Unauthorized |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contact_from_group**
> remove_contact_from_group(group_id, phone)

Removes a contact from a group

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
    api_instance = messente_api.ContactsApi(api_client)
    group_id = '5792a02a-e5c2-422b-a0a0-0ae65d814663' # str | String in UUID format
phone = '+37251000000' # str | A phone number

    try:
        # Removes a contact from a group
        api_instance.remove_contact_from_group(group_id, phone)
    except ApiException as e:
        print("Exception when calling ContactsApi->remove_contact_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in UUID format | 
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
**204** | Contact removed from group |  -  |
**400** | Invalid phone number provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact or group is missing or contact is missing from group |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ContactEnvelope update_contact(phone, contact_update_fields)

Updates a contact

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
    api_instance = messente_api.ContactsApi(api_client)
    phone = '+37251000000' # str | A phone number
contact_update_fields = {"email":"anyone@messente.com","firstName":"Any","lastName":"One","company":"Messente","title":"Sir","custom":"Any custom","custom2":"Any custom two","custom3":"Any custom three","custom4":"Any custom four"} # ContactUpdateFields | 

    try:
        # Updates a contact
        api_response = api_instance.update_contact(phone, contact_update_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| A phone number | 
 **contact_update_fields** | [**ContactUpdateFields**](ContactUpdateFields.md)|  | 

### Return type

[**ContactEnvelope**](ContactEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a contact object |  -  |
**400** | Invalid phone number or empty patch body or unknown fields provided |  -  |
**401** | Unauthorized |  -  |
**404** | Contact missing |  -  |
**0** | General error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

