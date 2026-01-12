# RcsCreateCalendarEventAction

Action to create a calendar event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The start time of the event. | 
**end_time** | **str** | The end time of the event. | 
**title** | **str** | The title of the event. | 
**description** | **str** | The description of the event. | 

## Example

```python
from messente_api.models.rcs_create_calendar_event_action import RcsCreateCalendarEventAction

# TODO update the JSON string below
json = "{}"
# create an instance of RcsCreateCalendarEventAction from a JSON string
rcs_create_calendar_event_action_instance = RcsCreateCalendarEventAction.from_json(json)
# print the JSON string representation of the object
print(RcsCreateCalendarEventAction.to_json())

# convert the object into a dict
rcs_create_calendar_event_action_dict = rcs_create_calendar_event_action_instance.to_dict()
# create an instance of RcsCreateCalendarEventAction from a dict
rcs_create_calendar_event_action_from_dict = RcsCreateCalendarEventAction.from_dict(rcs_create_calendar_event_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


