# CreateUpdateMembershipDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**amount** | **str** |  | 
**active** | **bool** |  | 

## Example

```python
from openapi_client.models.create_update_membership_dto import CreateUpdateMembershipDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateMembershipDTO from a JSON string
create_update_membership_dto_instance = CreateUpdateMembershipDTO.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateMembershipDTO.to_json())

# convert the object into a dict
create_update_membership_dto_dict = create_update_membership_dto_instance.to_dict()
# create an instance of CreateUpdateMembershipDTO from a dict
create_update_membership_dto_from_dict = CreateUpdateMembershipDTO.from_dict(create_update_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


