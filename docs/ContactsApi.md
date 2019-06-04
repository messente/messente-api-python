# messente_api.ContactsApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_to_group**](ContactsApi.md#add_contact_to_group) | **POST** /groups/{groupId}/contacts/{phone} | Adds a contact to a group
[**create_contact**](ContactsApi.md#create_contact) | **POST** /contacts | Creates a new contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /contacts/{phone} | Deletes a contact
[**fetch_contact**](ContactsApi.md#fetch_contact) | **GET** /contacts/{phone} | Lists a contact
[**fetch_contact_groups**](ContactsApi.md#fetch_contact_groups) | **GET** /contacts/{phone}/groups | Lists groups of a contact
[**fetch_contacts**](ContactsApi.md#fetch_contacts) | **GET** /contacts | Returns all contacts
[**remove_contact_from_group**](ContactsApi.md#remove_contact_from_group) | **DELETE** /groups/{groupId}/contacts/{phone} | Removes a contact from a group
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /contacts/{phone} | Updates a contact


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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
group_id = 'group_id_example' # str | String in uuid format.
phone = 'phone_example' # str | A phone number

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
 **group_id** | **str**| String in uuid format. | 
 **phone** | **str**| A phone number | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
contact_fields = messente_api.ContactFields() # ContactFields | 

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
phone = 'phone_example' # str | A phone number

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
phone = 'phone_example' # str | A phone number

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
phone = 'phone_example' # str | A phone number

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
group_ids = ['group_ids_example'] # list[str] | Optional one or many group id strings in uuid format. For example: \"/contacts?groupIds=group_id_one&groupIds=group_id_two\"  (optional)

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
 **group_ids** | [**list[str]**](str.md)| Optional one or many group id strings in uuid format. For example: \&quot;/contacts?groupIds&#x3D;group_id_one&amp;groupIds&#x3D;group_id_two\&quot;  | [optional] 

### Return type

[**ContactListEnvelope**](ContactListEnvelope.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
group_id = 'group_id_example' # str | String in uuid format.
phone = 'phone_example' # str | A phone number

try:
    # Removes a contact from a group
    api_instance.remove_contact_from_group(group_id, phone)
except ApiException as e:
    print("Exception when calling ContactsApi->remove_contact_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| String in uuid format. | 
 **phone** | **str**| A phone number | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
configuration = messente_api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messente_api.ContactsApi(messente_api.ApiClient(configuration))
phone = 'phone_example' # str | A phone number
contact_update_fields = messente_api.ContactUpdateFields() # ContactUpdateFields | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

