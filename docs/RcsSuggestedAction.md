# RcsSuggestedAction

RCS suggested action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text of the suggested action. Exactly one of the action fields (types) must be provided. | 
**postback_data** | **str** | The postback data associated with the suggested action. This is sent back to the sender when the user selects the suggested action. | 
**fallback_url** | **str** | The fallback URL to open if the suggested action is not supported. | [optional] 
**dial_action** | [**RcsDialAction**](RcsDialAction.md) |  | [optional] 
**view_location_action** | [**RcsViewLocationAction**](RcsViewLocationAction.md) |  | [optional] 
**create_calendar_event_action** | [**RcsCreateCalendarEventAction**](RcsCreateCalendarEventAction.md) |  | [optional] 
**open_url_action** | [**RcsOpenUrlAction**](RcsOpenUrlAction.md) |  | [optional] 
**share_location_action** | **object** | This action does not have any properties. It simply triggers the share location action. | [optional] 

## Example

```python
from messente_api.models.rcs_suggested_action import RcsSuggestedAction

# TODO update the JSON string below
json = "{}"
# create an instance of RcsSuggestedAction from a JSON string
rcs_suggested_action_instance = RcsSuggestedAction.from_json(json)
# print the JSON string representation of the object
print(RcsSuggestedAction.to_json())

# convert the object into a dict
rcs_suggested_action_dict = rcs_suggested_action_instance.to_dict()
# create an instance of RcsSuggestedAction from a dict
rcs_suggested_action_from_dict = RcsSuggestedAction.from_dict(rcs_suggested_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


