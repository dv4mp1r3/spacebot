# CreateACSKeyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**member_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_acs_key_dto import CreateACSKeyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACSKeyDTO from a JSON string
create_acs_key_dto_instance = CreateACSKeyDTO.from_json(json)
# print the JSON string representation of the object
print(CreateACSKeyDTO.to_json())

# convert the object into a dict
create_acs_key_dto_dict = create_acs_key_dto_instance.to_dict()
# create an instance of CreateACSKeyDTO from a dict
create_acs_key_dto_from_dict = CreateACSKeyDTO.from_dict(create_acs_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


