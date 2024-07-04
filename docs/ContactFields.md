# ContactFields

A container for fields of a request body of a contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number in e.164 format | 
**email** | **str** | The email of the contact | [optional] 
**first_name** | **str** | The first name of the contact | [optional] 
**last_name** | **str** | The last name of the contact | [optional] 
**company** | **str** | The company of the contact | [optional] 
**title** | **str** | The title of the contact | [optional] 
**custom** | **str** | The first custom field | [optional] 
**custom2** | **str** | The second custom field | [optional] 
**custom3** | **str** | The third custom field | [optional] 
**custom4** | **str** | The fourth custom field | [optional] 

## Example

```python
from messente_api.models.contact_fields import ContactFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContactFields from a JSON string
contact_fields_instance = ContactFields.from_json(json)
# print the JSON string representation of the object
print(ContactFields.to_json())

# convert the object into a dict
contact_fields_dict = contact_fields_instance.to_dict()
# create an instance of ContactFields from a dict
contact_fields_from_dict = ContactFields.from_dict(contact_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


