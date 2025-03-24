# SMS

SMS message content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text content of the SMS | 
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is considered as failed and the next channel is attempted.                     Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted.                     Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**autoconvert** | **str** | Defines how non-GSM characters will be treated:    - \&quot;on\&quot; Use replacement settings from the account&#39;s [API Auto Replace settings page](https://dashboard.messente.com/api-settings/auto-replace) (default)   - \&quot;full\&quot; All non GSM 03.38 characters will be replaced with suitable alternatives   - \&quot;off\&quot; Message content is not modified in any way | [optional] 
**udh** | **str** | hex-encoded string containing SMS UDH | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'sms']

## Example

```python
from messente_api.models.sms import SMS

# TODO update the JSON string below
json = "{}"
# create an instance of SMS from a JSON string
sms_instance = SMS.from_json(json)
# print the JSON string representation of the object
print(SMS.to_json())

# convert the object into a dict
sms_dict = sms_instance.to_dict()
# create an instance of SMS from a dict
sms_from_dict = SMS.from_dict(sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


