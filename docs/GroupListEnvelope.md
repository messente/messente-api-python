# GroupListEnvelope

A container for groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GroupResponseFields]**](GroupResponseFields.md) | An array of groups | [optional] 

## Example

```python
from messente_api.models.group_list_envelope import GroupListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GroupListEnvelope from a JSON string
group_list_envelope_instance = GroupListEnvelope.from_json(json)
# print the JSON string representation of the object
print(GroupListEnvelope.to_json())

# convert the object into a dict
group_list_envelope_dict = group_list_envelope_instance.to_dict()
# create an instance of GroupListEnvelope from a dict
group_list_envelope_from_dict = GroupListEnvelope.from_dict(group_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


