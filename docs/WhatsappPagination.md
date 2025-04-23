# WhatsappPagination

Whatsapp media object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** | A URL to ge the previous paginated page. | [optional] 
**next** | **str** | A URL to ge the next paginated page. | [optional] 
**cursors** | [**WhatsappPagingCursors**](WhatsappPagingCursors.md) |  | 

## Example

```python
from messente_api.models.whatsapp_pagination import WhatsappPagination

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPagination from a JSON string
whatsapp_pagination_instance = WhatsappPagination.from_json(json)
# print the JSON string representation of the object
print(WhatsappPagination.to_json())

# convert the object into a dict
whatsapp_pagination_dict = whatsapp_pagination_instance.to_dict()
# create an instance of WhatsappPagination from a dict
whatsapp_pagination_from_dict = WhatsappPagination.from_dict(whatsapp_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


