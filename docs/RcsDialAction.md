# RcsDialAction

Action to dial a phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | The phone number to dial in E.164 format. | 

## Example

```python
from messente_api.models.rcs_dial_action import RcsDialAction

# TODO update the JSON string below
json = "{}"
# create an instance of RcsDialAction from a JSON string
rcs_dial_action_instance = RcsDialAction.from_json(json)
# print the JSON string representation of the object
print(RcsDialAction.to_json())

# convert the object into a dict
rcs_dial_action_dict = rcs_dial_action_instance.to_dict()
# create an instance of RcsDialAction from a dict
rcs_dial_action_from_dict = RcsDialAction.from_dict(rcs_dial_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


