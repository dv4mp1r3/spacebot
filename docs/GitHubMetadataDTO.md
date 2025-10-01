# GitHubMetadataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_id** | **str** |  | 
**github_username** | **str** |  | 

## Example

```python
from openapi_client.models.git_hub_metadata_dto import GitHubMetadataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubMetadataDTO from a JSON string
git_hub_metadata_dto_instance = GitHubMetadataDTO.from_json(json)
# print the JSON string representation of the object
print(GitHubMetadataDTO.to_json())

# convert the object into a dict
git_hub_metadata_dto_dict = git_hub_metadata_dto_instance.to_dict()
# create an instance of GitHubMetadataDTO from a dict
git_hub_metadata_dto_from_dict = GitHubMetadataDTO.from_dict(git_hub_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


