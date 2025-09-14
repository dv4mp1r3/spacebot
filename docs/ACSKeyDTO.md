# ACSKeyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**member_id** | **str** |  | 
**type** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.acs_key_dto import ACSKeyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ACSKeyDTO from a JSON string
acs_key_dto_instance = ACSKeyDTO.from_json(json)
# print the JSON string representation of the object
print(ACSKeyDTO.to_json())

# convert the object into a dict
acs_key_dto_dict = acs_key_dto_instance.to_dict()
# create an instance of ACSKeyDTO from a dict
acs_key_dto_from_dict = ACSKeyDTO.from_dict(acs_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


