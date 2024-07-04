# DeliveryReportResponse

A container for successful delivery report response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[DeliveryResult]**](DeliveryResult.md) | Contains the delivery reports for each channel, ordered by send order | 
**to** | **str** | Phone number in e.164 format | 
**omnimessage_id** | **str** | Unique identifier for the omnimessage | 

## Example

```python
from messente_api.models.delivery_report_response import DeliveryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryReportResponse from a JSON string
delivery_report_response_instance = DeliveryReportResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveryReportResponse.to_json())

# convert the object into a dict
delivery_report_response_dict = delivery_report_response_instance.to_dict()
# create an instance of DeliveryReportResponse from a dict
delivery_report_response_from_dict = DeliveryReportResponse.from_dict(delivery_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


