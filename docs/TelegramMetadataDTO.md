# TelegramMetadataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telegram_id** | **str** |  | 
**telegram_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.telegram_metadata_dto import TelegramMetadataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramMetadataDTO from a JSON string
telegram_metadata_dto_instance = TelegramMetadataDTO.from_json(json)
# print the JSON string representation of the object
print(TelegramMetadataDTO.to_json())

# convert the object into a dict
telegram_metadata_dto_dict = telegram_metadata_dto_instance.to_dict()
# create an instance of TelegramMetadataDTO from a dict
telegram_metadata_dto_from_dict = TelegramMetadataDTO.from_dict(telegram_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


