# PriceInfo

Contains price information for the message. This value is *null* if the message is still being processed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_price** | **str** | price per message part - relevant mostly for SMS | 
**parts_count** | **int** | the number of parts the message consists of | 
**total_price** | **str** | total price for the message | 

## Example

```python
from messente_api.models.price_info import PriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfo from a JSON string
price_info_instance = PriceInfo.from_json(json)
# print the JSON string representation of the object
print(PriceInfo.to_json())

# convert the object into a dict
price_info_dict = price_info_instance.to_dict()
# create an instance of PriceInfo from a dict
price_info_from_dict = PriceInfo.from_dict(price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


