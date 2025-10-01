# MemberTransactionDTO


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
**subject** | [**MemberDTO**](MemberDTO.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.member_transaction_dto import MemberTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTransactionDTO from a JSON string
member_transaction_dto_instance = MemberTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(MemberTransactionDTO.to_json())

# convert the object into a dict
member_transaction_dto_dict = member_transaction_dto_instance.to_dict()
# create an instance of MemberTransactionDTO from a dict
member_transaction_dto_from_dict = MemberTransactionDTO.from_dict(member_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


