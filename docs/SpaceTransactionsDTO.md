# SpaceTransactionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** |  | 
**transactions** | [**List[SpaceTransactionDTO]**](SpaceTransactionDTO.md) |  | 

## Example

```python
from openapi_client.models.space_transactions_dto import SpaceTransactionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceTransactionsDTO from a JSON string
space_transactions_dto_instance = SpaceTransactionsDTO.from_json(json)
# print the JSON string representation of the object
print(SpaceTransactionsDTO.to_json())

# convert the object into a dict
space_transactions_dto_dict = space_transactions_dto_instance.to_dict()
# create an instance of SpaceTransactionsDTO from a dict
space_transactions_dto_from_dict = SpaceTransactionsDTO.from_dict(space_transactions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


