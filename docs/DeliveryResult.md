# DeliveryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | [optional] 
**message_id** | **str** | Unique identifier for the message | [optional] 
**error** | **str** | Human-readable description of what went wrong, *null* in case of success or if the message has not been processed yet | [optional] 
**err** | [**ErrorCodeOmnichannelMachine**](ErrorCodeOmnichannelMachine.md) |  | [optional] 
**timestamp** | **datetime** | When this status was received by Omnichannel API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


