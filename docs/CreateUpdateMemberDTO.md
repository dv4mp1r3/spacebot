# CreateUpdateMemberDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.create_update_member_dto import CreateUpdateMemberDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateMemberDTO from a JSON string
create_update_member_dto_instance = CreateUpdateMemberDTO.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateMemberDTO.to_json())

# convert the object into a dict
create_update_member_dto_dict = create_update_member_dto_instance.to_dict()
# create an instance of CreateUpdateMemberDTO from a dict
create_update_member_dto_from_dict = CreateUpdateMemberDTO.from_dict(create_update_member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


