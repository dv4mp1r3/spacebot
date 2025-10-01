# MemberTransactionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** |  | 
**transactions** | [**List[MemberTransactionDTO]**](MemberTransactionDTO.md) |  | 

## Example

```python
from openapi_client.models.member_transactions_dto import MemberTransactionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTransactionsDTO from a JSON string
member_transactions_dto_instance = MemberTransactionsDTO.from_json(json)
# print the JSON string representation of the object
print(MemberTransactionsDTO.to_json())

# convert the object into a dict
member_transactions_dto_dict = member_transactions_dto_instance.to_dict()
# create an instance of MemberTransactionsDTO from a dict
member_transactions_dto_from_dict = MemberTransactionsDTO.from_dict(member_transactions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


