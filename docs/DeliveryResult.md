# DeliveryResult

A delivery report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | [optional] 
**message_id** | **str** | Unique identifier for the message | [optional] 
**error** | **str** | Human-readable description of what went wrong, *null* in case of success or if the message has not been processed yet | [optional] 
**err** | [**ErrorCodeOmnichannelMachine**](ErrorCodeOmnichannelMachine.md) |  | [optional] 
**timestamp** | **datetime** | When this status was received by Omnichannel API | [optional] 

## Example

```python
from messente_api.models.delivery_result import DeliveryResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryResult from a JSON string
delivery_result_instance = DeliveryResult.from_json(json)
# print the JSON string representation of the object
print(DeliveryResult.to_json())

# convert the object into a dict
delivery_result_dict = delivery_result_instance.to_dict()
# create an instance of DeliveryResult from a dict
delivery_result_from_dict = DeliveryResult.from_dict(delivery_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


