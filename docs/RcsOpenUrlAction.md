# RcsOpenUrlAction

Action to open a URL in a browser.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to open. | 
**description** | **str** | A description of the URL being opened. | [optional] 
**application** | [**RcsOpenUrlApplication**](RcsOpenUrlApplication.md) |  | 
**webview_view_mode** | [**RcsWebviewViewMode**](RcsWebviewViewMode.md) |  | [optional] 

## Example

```python
from messente_api.models.rcs_open_url_action import RcsOpenUrlAction

# TODO update the JSON string below
json = "{}"
# create an instance of RcsOpenUrlAction from a JSON string
rcs_open_url_action_instance = RcsOpenUrlAction.from_json(json)
# print the JSON string representation of the object
print(RcsOpenUrlAction.to_json())

# convert the object into a dict
rcs_open_url_action_dict = rcs_open_url_action_instance.to_dict()
# create an instance of RcsOpenUrlAction from a dict
rcs_open_url_action_from_dict = RcsOpenUrlAction.from_dict(rcs_open_url_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


