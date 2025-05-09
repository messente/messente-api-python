# messente_api.NumberVerificationApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_number**](NumberVerificationApi.md#verify_number) | **POST** /verify/start | verify number
[**verify_pin**](NumberVerificationApi.md#verify_pin) | **POST** /verify/pin | verified the PIN code entered by the user.


# **verify_number**
> str verify_number(username, password, to, template=template, pin_length=pin_length, var_from=var_from, max_tries=max_tries, retry_delay=retry_delay, validity=validity, ip=ip, browser=browser, cookie=cookie)

verify number

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
    api_instance = messente_api.NumberVerificationApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password
    to = 'to_example' # str | Receiver's phone number with the country code
    template = 'template_example' # str | Template of the message, including PIN code. Placeholder for PIN code is <PIN>. When not set, default template is used: \"Your Verification PIN code is <PIN>\".  (optional)
    pin_length = 'pin_length_example' # str | Length of the PIN code. Minumum 4 digits, maximum 16. Defaults to 4. (optional)
    var_from = 'var_from_example' # str | Sender name. When not set, the default Sender name \"Verigator\" is used. This sender ID also needs to be added to your account beforehand. (optional)
    max_tries = 'max_tries_example' # str | Maximum number of times the PIN code is sent in total. Defaults to \"2\" - initial PIN code and one retry. It is discouraged to set this value to \"1\" as only the initial PIN code is sent and retry is disabled.   (optional)
    retry_delay = 'retry_delay_example' # str | For how long (in seconds) to wait for next retry, if the correct PIN code has not been entered yet? Defaults to 30 seconds. (optional)
    validity = 'validity_example' # str | For how long (in seconds) is the PIN code valid. Defaults to 5 minutes (300 seconds). Maximum 30 minutes (1800 seconds). (optional)
    ip = 'ip_example' # str | IP address of the client making verification request. (optional)
    browser = 'browser_example' # str | User Agent of the browser. For example \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36\". (optional)
    cookie = 'cookie_example' # str | Unique cookie assigned to this session. If a user tries logging in with the same cookie present, user is automatically logged in and no PIN code verification is needed. (optional)

    try:
        # verify number
        api_response = api_instance.verify_number(username, password, to, template=template, pin_length=pin_length, var_from=var_from, max_tries=max_tries, retry_delay=retry_delay, validity=validity, ip=ip, browser=browser, cookie=cookie)
        print("The response of NumberVerificationApi->verify_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumberVerificationApi->verify_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The API username | 
 **password** | **str**| The API password | 
 **to** | **str**| Receiver&#39;s phone number with the country code | 
 **template** | **str**| Template of the message, including PIN code. Placeholder for PIN code is &lt;PIN&gt;. When not set, default template is used: \&quot;Your Verification PIN code is &lt;PIN&gt;\&quot;.  | [optional] 
 **pin_length** | **str**| Length of the PIN code. Minumum 4 digits, maximum 16. Defaults to 4. | [optional] 
 **var_from** | **str**| Sender name. When not set, the default Sender name \&quot;Verigator\&quot; is used. This sender ID also needs to be added to your account beforehand. | [optional] 
 **max_tries** | **str**| Maximum number of times the PIN code is sent in total. Defaults to \&quot;2\&quot; - initial PIN code and one retry. It is discouraged to set this value to \&quot;1\&quot; as only the initial PIN code is sent and retry is disabled.   | [optional] 
 **retry_delay** | **str**| For how long (in seconds) to wait for next retry, if the correct PIN code has not been entered yet? Defaults to 30 seconds. | [optional] 
 **validity** | **str**| For how long (in seconds) is the PIN code valid. Defaults to 5 minutes (300 seconds). Maximum 30 minutes (1800 seconds). | [optional] 
 **ip** | **str**| IP address of the client making verification request. | [optional] 
 **browser** | **str**| User Agent of the browser. For example \&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36\&quot;. | [optional] 
 **cookie** | **str**| Unique cookie assigned to this session. If a user tries logging in with the same cookie present, user is automatically logged in and no PIN code verification is needed. | [optional] 

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

# **verify_pin**
> str verify_pin(username, password, verification_id, pin, ip=ip, browser=browser, cookie=cookie)

verified the PIN code entered by the user.

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
    api_instance = messente_api.NumberVerificationApi(api_client)
    username = 'username_example' # str | The API username
    password = 'password_example' # str | The API password
    verification_id = 'verification_id_example' # str | Verification ID returned by the successful verification request.
    pin = 'pin_example' # str | PIN code entered by the user.
    ip = 'ip_example' # str | IP address of the client making verification request. If the IP address is from another country, PIN is required even if the cookies match. (optional)
    browser = 'browser_example' # str | User Agent of the browser. For example \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36\". (optional)
    cookie = 'cookie_example' # str | Unique cookie assigned to this session. If a user tries logging in with the same cookie present, user is automatically logged in and no PIN code verification is needed. (optional)

    try:
        # verified the PIN code entered by the user.
        api_response = api_instance.verify_pin(username, password, verification_id, pin, ip=ip, browser=browser, cookie=cookie)
        print("The response of NumberVerificationApi->verify_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumberVerificationApi->verify_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The API username | 
 **password** | **str**| The API password | 
 **verification_id** | **str**| Verification ID returned by the successful verification request. | 
 **pin** | **str**| PIN code entered by the user. | 
 **ip** | **str**| IP address of the client making verification request. If the IP address is from another country, PIN is required even if the cookies match. | [optional] 
 **browser** | **str**| User Agent of the browser. For example \&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36\&quot;. | [optional] 
 **cookie** | **str**| Unique cookie assigned to this session. If a user tries logging in with the same cookie present, user is automatically logged in and no PIN code verification is needed. | [optional] 

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

