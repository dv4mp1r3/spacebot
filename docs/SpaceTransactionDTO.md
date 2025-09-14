# SpaceTransactionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**amount** | **str** |  | 
**comment** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**actor** | [**MemberDTO**](MemberDTO.md) |  | 
**related_member_transaction_subject** | [**MemberDTO**](MemberDTO.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.space_transaction_dto import SpaceTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceTransactionDTO from a JSON string
space_transaction_dto_instance = SpaceTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(SpaceTransactionDTO.to_json())

# convert the object into a dict
space_transaction_dto_dict = space_transaction_dto_instance.to_dict()
# create an instance of SpaceTransactionDTO from a dict
space_transaction_dto_from_dict = SpaceTransactionDTO.from_dict(space_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


