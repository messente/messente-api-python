# ContactEnvelope

A container for a contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ContactResponseFields**](ContactResponseFields.md) |  | [optional] 

## Example

```python
from messente_api.models.contact_envelope import ContactEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ContactEnvelope from a JSON string
contact_envelope_instance = ContactEnvelope.from_json(json)
# print the JSON string representation of the object
print(ContactEnvelope.to_json())

# convert the object into a dict
contact_envelope_dict = contact_envelope_instance.to_dict()
# create an instance of ContactEnvelope from a dict
contact_envelope_from_dict = ContactEnvelope.from_dict(contact_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


