# WhatsappPagingCursors

WhatsApp paging cursors object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | The template before the first template in the current list | [optional] 
**after** | **str** | The template after the last template in the current list | [optional] 

## Example

```python
from messente_api.models.whatsapp_paging_cursors import WhatsappPagingCursors

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPagingCursors from a JSON string
whatsapp_paging_cursors_instance = WhatsappPagingCursors.from_json(json)
# print the JSON string representation of the object
print(WhatsappPagingCursors.to_json())

# convert the object into a dict
whatsapp_paging_cursors_dict = whatsapp_paging_cursors_instance.to_dict()
# create an instance of WhatsappPagingCursors from a dict
whatsapp_paging_cursors_from_dict = WhatsappPagingCursors.from_dict(whatsapp_paging_cursors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


