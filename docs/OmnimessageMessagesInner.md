# OmnimessageMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is considered as failed and the next channel is attempted | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted.       Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**text** | **str** | Plaintext content for Telegram | 
**image_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;document_url\&quot; and \&quot;audio_url\&quot; | [optional] 
**button_url** | **str** | URL of the button, must be specified along with &#39;&#39;text&#39;&#39;, &#39;&#39;button_text&#39;&#39; and &#39;&#39;image_url&#39;&#39; (optional) | [optional] 
**button_text** | **str** | Must be specified along with &#39;&#39;text&#39;&#39;, &#39;&#39;button_url&#39;&#39;, &#39;&#39;button_text&#39;&#39;, &#39;&#39;image_url&#39;&#39; (optional) | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'telegram']
**autoconvert** | **str** | Defines how non-GSM characters will be treated:    - \&quot;on\&quot; Use replacement settings from the account&#39;s [API Auto Replace settings page](https://dashboard.messente.com/api-settings/auto-replace) (default)   - \&quot;full\&quot; All non GSM 03.38 characters will be replaced with suitable alternatives   - \&quot;off\&quot; Message content is not modified in any way | [optional] 
**udh** | **str** | hex-encoded string containing SMS UDH | [optional] 
**template** | [**WhatsAppTemplate**](WhatsAppTemplate.md) |  | [optional] 
**document_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;audio_url\&quot; and \&quot;image_url\&quot; | [optional] 
**audio_url** | **str** | URL for the embedded image. Mutually exclusive with \&quot;document_url\&quot; and \&quot;image_url\&quot; | [optional] 

## Example

```python
from messente_api.models.omnimessage_messages_inner import OmnimessageMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OmnimessageMessagesInner from a JSON string
omnimessage_messages_inner_instance = OmnimessageMessagesInner.from_json(json)
# print the JSON string representation of the object
print(OmnimessageMessagesInner.to_json())

# convert the object into a dict
omnimessage_messages_inner_dict = omnimessage_messages_inner_instance.to_dict()
# create an instance of OmnimessageMessagesInner from a dict
omnimessage_messages_inner_from_dict = OmnimessageMessagesInner.from_dict(omnimessage_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


