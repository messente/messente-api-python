# ContactResponseFields

A container for response fields of a contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number in e.164 format | [optional] 
**email** | **str** | The email of the contact | [optional] 
**first_name** | **str** | The first name of the contact | [optional] 
**last_name** | **str** | The last name of the contact | [optional] 
**company** | **str** | The company of the contact | [optional] 
**title** | **str** | The title of the contact | [optional] 
**custom** | **str** | The first custom field | [optional] 
**custom2** | **str** | The second custom field | [optional] 
**custom3** | **str** | The third custom field | [optional] 
**custom4** | **str** | The fourth custom field | [optional] 
**scheduled_deletion_date** | **date** | The date in ISO 8601 format, YYYY-MM-DD,  on which the contact is going to be deleted  because it has not belonged to a group for 30 days | [optional] 

## Example

```python
from messente_api.models.contact_response_fields import ContactResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContactResponseFields from a JSON string
contact_response_fields_instance = ContactResponseFields.from_json(json)
# print the JSON string representation of the object
print(ContactResponseFields.to_json())

# convert the object into a dict
contact_response_fields_dict = contact_response_fields_instance.to_dict()
# create an instance of ContactResponseFields from a dict
contact_response_fields_from_dict = ContactResponseFields.from_dict(contact_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


