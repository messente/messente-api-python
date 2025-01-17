# MobileNetwork

Info about the network related to the phone number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mccmnc** | **str** | Mobile country and mobile network code | [optional] 
**network_name** | **str** | Mobile network name | [optional] 
**country_name** | **str** | Country name | [optional] 
**country_prefix** | **str** | Country prefix | [optional] 
**country_code** | **str** | Country code | [optional] 

## Example

```python
from messente_api.models.mobile_network import MobileNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of MobileNetwork from a JSON string
mobile_network_instance = MobileNetwork.from_json(json)
# print the JSON string representation of the object
print(MobileNetwork.to_json())

# convert the object into a dict
mobile_network_dict = mobile_network_instance.to_dict()
# create an instance of MobileNetwork from a dict
mobile_network_from_dict = MobileNetwork.from_dict(mobile_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


