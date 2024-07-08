# GroupResponseFields

A container for fields of a group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id string in UUID format | 
**name** | **str** | The name of the group | 
**created_on** | **str** | When the group was created | [optional] 
**contacts_count** | **int** | The count of contacts in the group | 

## Example

```python
from messente_api.models.group_response_fields import GroupResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResponseFields from a JSON string
group_response_fields_instance = GroupResponseFields.from_json(json)
# print the JSON string representation of the object
print(GroupResponseFields.to_json())

# convert the object into a dict
group_response_fields_dict = group_response_fields_instance.to_dict()
# create an instance of GroupResponseFields from a dict
group_response_fields_from_dict = GroupResponseFields.from_dict(group_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


