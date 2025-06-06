# PriceNetworksInner

An object containing the network information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the network | 
**price** | **str** | The price for sending a message to this network | 
**mccmnc** | **float** | The MCCMNC code for the network | 

## Example

```python
from messente_api.models.price_networks_inner import PriceNetworksInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceNetworksInner from a JSON string
price_networks_inner_instance = PriceNetworksInner.from_json(json)
# print the JSON string representation of the object
print(PriceNetworksInner.to_json())

# convert the object into a dict
price_networks_inner_dict = price_networks_inner_instance.to_dict()
# create an instance of PriceNetworksInner from a dict
price_networks_inner_from_dict = PriceNetworksInner.from_dict(price_networks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


