# SubscribeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | 
**membership_id** | **str** |  | 

## Example

```python
from openapi_client.models.subscribe_dto import SubscribeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeDTO from a JSON string
subscribe_dto_instance = SubscribeDTO.from_json(json)
# print the JSON string representation of the object
print(SubscribeDTO.to_json())

# convert the object into a dict
subscribe_dto_dict = subscribe_dto_instance.to_dict()
# create an instance of SubscribeDTO from a dict
subscribe_dto_from_dict = SubscribeDTO.from_dict(subscribe_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


