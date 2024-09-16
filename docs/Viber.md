# Viber

Viber message content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is considered as failed and the next channel is attempted.       Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted.       Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**text** | **str** | Plaintext content for Viber | [optional] 
**image_url** | **str** | URL for the embedded image    Valid combinations:    1) image_url,    2) text, image_url, button_url, button_text | [optional] 
**button_url** | **str** | URL of the button, must be specified along with &#39;&#39;text&#39;&#39;, &#39;&#39;button_text&#39;&#39; and &#39;&#39;image_url&#39;&#39; (optional) | [optional] 
**button_text** | **str** | Must be specified along with &#39;&#39;text&#39;&#39;, &#39;&#39;button_url&#39;&#39;, &#39;&#39;button_text&#39;&#39;, &#39;&#39;image_url&#39;&#39; (optional) | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'viber']
**video** | [**ViberVideo**](ViberVideo.md) |  | [optional] 

## Example

```python
from messente_api.models.viber import Viber

# TODO update the JSON string below
json = "{}"
# create an instance of Viber from a JSON string
viber_instance = Viber.from_json(json)
# print the JSON string representation of the object
print(Viber.to_json())

# convert the object into a dict
viber_dict = viber_instance.to_dict()
# create an instance of Viber from a dict
viber_from_dict = Viber.from_dict(viber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


