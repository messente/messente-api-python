# WhatsApp

WhatsApp message content.   Only one of \"text\", \"image\", \"document\" or \"audio\" can be provided
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Phone number or alphanumeric sender name | [optional] 
**validity** | **int** | After how many minutes this channel is   considered as failed and the next channel is attempted | [optional] 
**ttl** | **int** | After how many seconds this channel is considered as failed and the next channel is attempted.       Only one of \&quot;ttl\&quot; and \&quot;validity\&quot; can be used. | [optional] 
**text** | [**WhatsAppText**](WhatsAppText.md) |  | [optional] 
**image** | [**WhatsAppImage**](WhatsAppImage.md) |  | [optional] 
**document** | [**WhatsAppDocument**](WhatsAppDocument.md) |  | [optional] 
**audio** | [**WhatsAppAudio**](WhatsAppAudio.md) |  | [optional] 
**channel** | **str** | The channel used to deliver the message | [optional] [default to 'whatsapp']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


