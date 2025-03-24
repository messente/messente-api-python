# BulkOmnimessage

A bulk omnimessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Omnimessage]**](Omnimessage.md) | A list of omnimessages. | 

## Example

```python
from messente_api.models.bulk_omnimessage import BulkOmnimessage

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOmnimessage from a JSON string
bulk_omnimessage_instance = BulkOmnimessage.from_json(json)
# print the JSON string representation of the object
print(BulkOmnimessage.to_json())

# convert the object into a dict
bulk_omnimessage_dict = bulk_omnimessage_instance.to_dict()
# create an instance of BulkOmnimessage from a dict
bulk_omnimessage_from_dict = BulkOmnimessage.from_dict(bulk_omnimessage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


