# ErrorApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.error_api_response import ErrorApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorApiResponse from a JSON string
error_api_response_instance = ErrorApiResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorApiResponse.to_json())

# convert the object into a dict
error_api_response_dict = error_api_response_instance.to_dict()
# create an instance of ErrorApiResponse from a dict
error_api_response_from_dict = ErrorApiResponse.from_dict(error_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


