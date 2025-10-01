# CreateMemberTransactionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **str** |  | 
**comment** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**subject_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_member_transaction_dto import CreateMemberTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberTransactionDTO from a JSON string
create_member_transaction_dto_instance = CreateMemberTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(CreateMemberTransactionDTO.to_json())

# convert the object into a dict
create_member_transaction_dto_dict = create_member_transaction_dto_instance.to_dict()
# create an instance of CreateMemberTransactionDTO from a dict
create_member_transaction_dto_from_dict = CreateMemberTransactionDTO.from_dict(create_member_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


