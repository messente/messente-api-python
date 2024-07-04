# Omnimessage

An omnimessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Phone number in e.164 format | 
**messages** | [**List[OmnimessageMessagesInner]**](OmnimessageMessagesInner.md) | An array of messages | 
**dlr_url** | **str** | URL where the delivery report will be sent | [optional] 
**text_store** | [**TextStore**](TextStore.md) |  | [optional] 
**time_to_send** | **datetime** | Optional parameter for sending messages at some specific time in the future.   Time must be specified in the ISO-8601 format.   If no timezone is specified, then the timezone is assumed to be UTC    Examples:    * Time specified with timezone: 2018-06-22T09:05:07+00:00 Time specified in UTC: 2018-06-22T09:05:07Z   * Time specified without timezone: 2018-06-22T09:05 (equivalent to 2018-06-22T09:05+00:00) | [optional] 
**priority** | [**Priority**](Priority.md) |  | [optional] 

## Example

```python
from messente_api.models.omnimessage import Omnimessage

# TODO update the JSON string below
json = "{}"
# create an instance of Omnimessage from a JSON string
omnimessage_instance = Omnimessage.from_json(json)
# print the JSON string representation of the object
print(Omnimessage.to_json())

# convert the object into a dict
omnimessage_dict = omnimessage_instance.to_dict()
# create an instance of Omnimessage from a dict
omnimessage_from_dict = Omnimessage.from_dict(omnimessage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


