# ContactListEnvelope

A container for contacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[ContactResponseFields]**](ContactResponseFields.md) | An array of contacts | [optional] 

## Example

```python
from messente_api.models.contact_list_envelope import ContactListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ContactListEnvelope from a JSON string
contact_list_envelope_instance = ContactListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ContactListEnvelope.to_json())

# convert the object into a dict
contact_list_envelope_dict = contact_list_envelope_instance.to_dict()
# create an instance of ContactListEnvelope from a dict
contact_list_envelope_from_dict = ContactListEnvelope.from_dict(contact_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


