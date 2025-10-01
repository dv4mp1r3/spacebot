# CreateMACDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | 
**mac** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from openapi_client.models.create_macdto import CreateMACDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMACDTO from a JSON string
create_macdto_instance = CreateMACDTO.from_json(json)
# print the JSON string representation of the object
print(CreateMACDTO.to_json())

# convert the object into a dict
create_macdto_dict = create_macdto_instance.to_dict()
# create an instance of CreateMACDTO from a dict
create_macdto_from_dict = CreateMACDTO.from_dict(create_macdto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


