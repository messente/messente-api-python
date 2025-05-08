# Price

An object containing the pricing information for a given country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The alpha-2 code for the country | 
**name** | **str** | The name of the country | 
**prefix** | **str** | The country code prefix | 
**networks** | [**List[PriceNetworksInner]**](PriceNetworksInner.md) | A list of networks available in the country | 

## Example

```python
from messente_api.models.price import Price

# TODO update the JSON string below
json = "{}"
# create an instance of Price from a JSON string
price_instance = Price.from_json(json)
# print the JSON string representation of the object
print(Price.to_json())

# convert the object into a dict
price_dict = price_instance.to_dict()
# create an instance of Price from a dict
price_from_dict = Price.from_dict(price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


