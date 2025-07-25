# messente_api.WhatsAppTemplatesApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_whatsapp_template**](WhatsAppTemplatesApi.md#create_whatsapp_template) | **POST** /whatsapp/wabas/{wabaId}/templates | Creates a WhatsApp template
[**delete_whatsapp_template**](WhatsAppTemplatesApi.md#delete_whatsapp_template) | **DELETE** /whatsapp/wabas/{wabaId}/templates | Deletes a WhatsApp template
[**get_whatsapp_template_by_id**](WhatsAppTemplatesApi.md#get_whatsapp_template_by_id) | **GET** /whatsapp/wabas/{wabaId}/templates/{templateId} | Requests a WhatsApp template with the given ID
[**list_whatsapp_templates**](WhatsAppTemplatesApi.md#list_whatsapp_templates) | **GET** /whatsapp/wabas/{wabaId}/templates | Requests a list of WhatsApp templates
[**update_whatsapp_template**](WhatsAppTemplatesApi.md#update_whatsapp_template) | **PUT** /whatsapp/wabas/{wabaId}/templates/{templateId} | Updates a WhatsApp template


# **create_whatsapp_template**
> WhatsappCreateTemplateResponse create_whatsapp_template(waba_id, whatsapp_create_template_request)

Creates a WhatsApp template

### Example

* Basic Authentication (basicAuth):

```python
import messente_api
from messente_api.models.whatsapp_create_template_request import WhatsappCreateTemplateRequest
from messente_api.models.whatsapp_create_template_response import WhatsappCreateTemplateResponse
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
    api_instance = messente_api.WhatsAppTemplatesApi(api_client)
    waba_id = 'waba_id_example' # str | The ID of the WABA
    whatsapp_create_template_request = messente_api.WhatsappCreateTemplateRequest() # WhatsappCreateTemplateRequest | The WhatsApp template to create

    try:
        # Creates a WhatsApp template
        api_response = api_instance.create_whatsapp_template(waba_id, whatsapp_create_template_request)
        print("The response of WhatsAppTemplatesApi->create_whatsapp_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppTemplatesApi->create_whatsapp_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_id** | **str**| The ID of the WABA | 
 **whatsapp_create_template_request** | [**WhatsappCreateTemplateRequest**](WhatsappCreateTemplateRequest.md)| The WhatsApp template to create | 

### Return type

[**WhatsappCreateTemplateResponse**](WhatsappCreateTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template creation successful |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_whatsapp_template**
> object delete_whatsapp_template(waba_id, name, hsm_id=hsm_id)

Deletes a WhatsApp template

### Example

* Basic Authentication (basicAuth):

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

# Configure HTTP basic authorization: basicAuth
configuration = messente_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with messente_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messente_api.WhatsAppTemplatesApi(api_client)
    waba_id = 'waba_id_example' # str | The ID of the WABA
    name = 'template_name' # str | The name of the template to delete
    hsm_id = '1' # str | The ID of the template to delete (optional)

    try:
        # Deletes a WhatsApp template
        api_response = api_instance.delete_whatsapp_template(waba_id, name, hsm_id=hsm_id)
        print("The response of WhatsAppTemplatesApi->delete_whatsapp_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppTemplatesApi->delete_whatsapp_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_id** | **str**| The ID of the WABA | 
 **name** | **str**| The name of the template to delete | 
 **hsm_id** | **str**| The ID of the template to delete | [optional] 

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
**200** | template deletion successful |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whatsapp_template_by_id**
> WhatsappTemplateResponse get_whatsapp_template_by_id(waba_id, template_id)

Requests a WhatsApp template with the given ID

### Example

* Basic Authentication (basicAuth):

```python
import messente_api
from messente_api.models.whatsapp_template_response import WhatsappTemplateResponse
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
    api_instance = messente_api.WhatsAppTemplatesApi(api_client)
    waba_id = 'waba_id_example' # str | The ID of the WABA
    template_id = 'template_id_example' # str | The ID of the template to retrieve

    try:
        # Requests a WhatsApp template with the given ID
        api_response = api_instance.get_whatsapp_template_by_id(waba_id, template_id)
        print("The response of WhatsAppTemplatesApi->get_whatsapp_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppTemplatesApi->get_whatsapp_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_id** | **str**| The ID of the WABA | 
 **template_id** | **str**| The ID of the template to retrieve | 

### Return type

[**WhatsappTemplateResponse**](WhatsappTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template fetched successfully |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_whatsapp_templates**
> WhatsappListTemplatesResponse list_whatsapp_templates(waba_id, limit=limit, before=before, after=after, category=category, content=content, language=language, name=name, status=status)

Requests a list of WhatsApp templates

### Example

* Basic Authentication (basicAuth):

```python
import messente_api
from messente_api.models.whatsapp_list_templates_response import WhatsappListTemplatesResponse
from messente_api.models.whatsapp_template_category import WhatsappTemplateCategory
from messente_api.models.whatsapp_template_status import WhatsappTemplateStatus
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
    api_instance = messente_api.WhatsAppTemplatesApi(api_client)
    waba_id = 'waba_id_example' # str | The ID of the WABA
    limit = 25 # int | The number of templates to return in the list. Although the max size is 500, for large datasets it is recommended to use a lower limit and instead use pagination to avoid potential timeouts. Defaults to 25. (optional) (default to 25)
    before = 'MAZDZD' # str | A cursor point used for a paginated request to indicate the template to paginate backwards from. (optional)
    after = 'MjQZD' # str | A cursor point used for a paginated request to indicate the template to paginate forwards from. (optional)
    category = messente_api.WhatsappTemplateCategory() # WhatsappTemplateCategory | A filter for returning only templates matching a specific category. (optional)
    content = 'special offer' # str | A search filter representing the content of a template. Only matching templates will be returned in the list. (optional)
    language = 'en' # str | A filter  for returning only templates matching a specific language code. A list of supported languages is available in the [WhatsApp documentation](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates/)  (optional)
    name = 'Sample Template' # str | A search filter representing the name, either full or partial, of a template. Only matching templates will be returned in the list. (optional)
    status = messente_api.WhatsappTemplateStatus() # WhatsappTemplateStatus | A filter for returning only templates matching a specific status. (optional)

    try:
        # Requests a list of WhatsApp templates
        api_response = api_instance.list_whatsapp_templates(waba_id, limit=limit, before=before, after=after, category=category, content=content, language=language, name=name, status=status)
        print("The response of WhatsAppTemplatesApi->list_whatsapp_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppTemplatesApi->list_whatsapp_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_id** | **str**| The ID of the WABA | 
 **limit** | **int**| The number of templates to return in the list. Although the max size is 500, for large datasets it is recommended to use a lower limit and instead use pagination to avoid potential timeouts. Defaults to 25. | [optional] [default to 25]
 **before** | **str**| A cursor point used for a paginated request to indicate the template to paginate backwards from. | [optional] 
 **after** | **str**| A cursor point used for a paginated request to indicate the template to paginate forwards from. | [optional] 
 **category** | [**WhatsappTemplateCategory**](.md)| A filter for returning only templates matching a specific category. | [optional] 
 **content** | **str**| A search filter representing the content of a template. Only matching templates will be returned in the list. | [optional] 
 **language** | **str**| A filter  for returning only templates matching a specific language code. A list of supported languages is available in the [WhatsApp documentation](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates/)  | [optional] 
 **name** | **str**| A search filter representing the name, either full or partial, of a template. Only matching templates will be returned in the list. | [optional] 
 **status** | [**WhatsappTemplateStatus**](.md)| A filter for returning only templates matching a specific status. | [optional] 

### Return type

[**WhatsappListTemplatesResponse**](WhatsappListTemplatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template list fetched successfully |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_whatsapp_template**
> object update_whatsapp_template(waba_id, template_id, whatsapp_update_template_request)

Updates a WhatsApp template

### Example

* Basic Authentication (basicAuth):

```python
import messente_api
from messente_api.models.whatsapp_update_template_request import WhatsappUpdateTemplateRequest
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
    api_instance = messente_api.WhatsAppTemplatesApi(api_client)
    waba_id = 'waba_id_example' # str | The ID of the WABA
    template_id = 'template_id_example' # str | The ID of the template to update
    whatsapp_update_template_request = messente_api.WhatsappUpdateTemplateRequest() # WhatsappUpdateTemplateRequest | The template data to be updated

    try:
        # Updates a WhatsApp template
        api_response = api_instance.update_whatsapp_template(waba_id, template_id, whatsapp_update_template_request)
        print("The response of WhatsAppTemplatesApi->update_whatsapp_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppTemplatesApi->update_whatsapp_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_id** | **str**| The ID of the WABA | 
 **template_id** | **str**| The ID of the template to update | 
 **whatsapp_update_template_request** | [**WhatsappUpdateTemplateRequest**](WhatsappUpdateTemplateRequest.md)| The template data to be updated | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template update successful |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

