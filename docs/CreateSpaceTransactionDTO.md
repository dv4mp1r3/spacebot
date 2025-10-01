# CreateSpaceTransactionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **str** |  | 
**comment** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_space_transaction_dto import CreateSpaceTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSpaceTransactionDTO from a JSON string
create_space_transaction_dto_instance = CreateSpaceTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(CreateSpaceTransactionDTO.to_json())

# convert the object into a dict
create_space_transaction_dto_dict = create_space_transaction_dto_instance.to_dict()
# create an instance of CreateSpaceTransactionDTO from a dict
create_space_transaction_dto_from_dict = CreateSpaceTransactionDTO.from_dict(create_space_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


