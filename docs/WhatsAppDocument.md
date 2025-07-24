# WhatsAppDocument

WhatsApp document content. Either \"id\" or \"link\" must be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document file. | [optional] 
**caption** | **str** | Caption for the document. | [optional] 
**mime_type** | **str** | MIME type of the document file. | [optional] 
**file_name** | **str** | Name of the document file. | [optional] 
**link** | **str** | URL link to the document file. | [optional] 

## Example

```python
from messente_api.models.whats_app_document import WhatsAppDocument

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppDocument from a JSON string
whats_app_document_instance = WhatsAppDocument.from_json(json)
# print the JSON string representation of the object
print(WhatsAppDocument.to_json())

# convert the object into a dict
whats_app_document_dict = whats_app_document_instance.to_dict()
# create an instance of WhatsAppDocument from a dict
whats_app_document_from_dict = WhatsAppDocument.from_dict(whats_app_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


