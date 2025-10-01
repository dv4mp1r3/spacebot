# openapi_client.MembersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**members_controller_create**](MembersApi.md#members_controller_create) | **POST** /api/members | Create new member
[**members_controller_delete_git_hub_metadata**](MembersApi.md#members_controller_delete_git_hub_metadata) | **DELETE** /api/members/{id}/github | Delete GitHub metadata for member
[**members_controller_delete_telegram_metadata**](MembersApi.md#members_controller_delete_telegram_metadata) | **DELETE** /api/members/{id}/telegram | Delete Telegram metadata for member
[**members_controller_find_all**](MembersApi.md#members_controller_find_all) | **GET** /api/members | Get info about all members
[**members_controller_find_by_id**](MembersApi.md#members_controller_find_by_id) | **GET** /api/members/{id} | Get full info about member
[**members_controller_stats**](MembersApi.md#members_controller_stats) | **GET** /api/members/stats | Get stats of all members
[**members_controller_update**](MembersApi.md#members_controller_update) | **PATCH** /api/members/{id} | Update member
[**members_controller_update_git_hub_metadata**](MembersApi.md#members_controller_update_git_hub_metadata) | **PATCH** /api/members/{id}/github | Add/update GitHub metadata for member
[**members_controller_update_status**](MembersApi.md#members_controller_update_status) | **PATCH** /api/members/{id}/status | Freeze/unfreeze member
[**members_controller_update_telegram_metadata**](MembersApi.md#members_controller_update_telegram_metadata) | **PATCH** /api/members/{id}/telegram | Add/update Telegram metadata for member


# **members_controller_create**
> MemberDTO members_controller_create(create_update_member_dto)

Create new member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_update_member_dto import CreateUpdateMemberDTO
from openapi_client.models.member_dto import MemberDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    create_update_member_dto = openapi_client.CreateUpdateMemberDTO() # CreateUpdateMemberDTO | 

    try:
        # Create new member
        api_response = api_instance.members_controller_create(create_update_member_dto)
        print("The response of MembersApi->members_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_member_dto** | [**CreateUpdateMemberDTO**](CreateUpdateMemberDTO.md)|  | 

### Return type

[**MemberDTO**](MemberDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_delete_git_hub_metadata**
> object members_controller_delete_git_hub_metadata(id)

Delete GitHub metadata for member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete GitHub metadata for member
        api_response = api_instance.members_controller_delete_git_hub_metadata(id)
        print("The response of MembersApi->members_controller_delete_git_hub_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_delete_git_hub_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_delete_telegram_metadata**
> object members_controller_delete_telegram_metadata(id)

Delete Telegram metadata for member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Telegram metadata for member
        api_response = api_instance.members_controller_delete_telegram_metadata(id)
        print("The response of MembersApi->members_controller_delete_telegram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_delete_telegram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_find_all**
> List[MemberDTO] members_controller_find_all()

Get info about all members

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_dto import MemberDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)

    try:
        # Get info about all members
        api_response = api_instance.members_controller_find_all()
        print("The response of MembersApi->members_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_find_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MemberDTO]**](MemberDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_find_by_id**
> MemberDTO members_controller_find_by_id(id)

Get full info about member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_dto import MemberDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get full info about member
        api_response = api_instance.members_controller_find_by_id(id)
        print("The response of MembersApi->members_controller_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MemberDTO**](MemberDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_stats**
> MemberStatsDTO members_controller_stats()

Get stats of all members

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_stats_dto import MemberStatsDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)

    try:
        # Get stats of all members
        api_response = api_instance.members_controller_stats()
        print("The response of MembersApi->members_controller_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MemberStatsDTO**](MemberStatsDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_update**
> MemberDTO members_controller_update(id, create_update_member_dto)

Update member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_update_member_dto import CreateUpdateMemberDTO
from openapi_client.models.member_dto import MemberDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 
    create_update_member_dto = openapi_client.CreateUpdateMemberDTO() # CreateUpdateMemberDTO | 

    try:
        # Update member
        api_response = api_instance.members_controller_update(id, create_update_member_dto)
        print("The response of MembersApi->members_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_update_member_dto** | [**CreateUpdateMemberDTO**](CreateUpdateMemberDTO.md)|  | 

### Return type

[**MemberDTO**](MemberDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_update_git_hub_metadata**
> object members_controller_update_git_hub_metadata(id, update_git_hub_metadata_dto)

Add/update GitHub metadata for member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.update_git_hub_metadata_dto import UpdateGitHubMetadataDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 
    update_git_hub_metadata_dto = openapi_client.UpdateGitHubMetadataDTO() # UpdateGitHubMetadataDTO | 

    try:
        # Add/update GitHub metadata for member
        api_response = api_instance.members_controller_update_git_hub_metadata(id, update_git_hub_metadata_dto)
        print("The response of MembersApi->members_controller_update_git_hub_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_update_git_hub_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_git_hub_metadata_dto** | [**UpdateGitHubMetadataDTO**](UpdateGitHubMetadataDTO.md)|  | 

### Return type

**object**

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_update_status**
> MemberDTO members_controller_update_status(id, update_status_dto)

Freeze/unfreeze member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_dto import MemberDTO
from openapi_client.models.update_status_dto import UpdateStatusDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 
    update_status_dto = openapi_client.UpdateStatusDTO() # UpdateStatusDTO | 

    try:
        # Freeze/unfreeze member
        api_response = api_instance.members_controller_update_status(id, update_status_dto)
        print("The response of MembersApi->members_controller_update_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_update_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_status_dto** | [**UpdateStatusDTO**](UpdateStatusDTO.md)|  | 

### Return type

[**MemberDTO**](MemberDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_controller_update_telegram_metadata**
> object members_controller_update_telegram_metadata(id, update_telegram_metadata_dto)

Add/update Telegram metadata for member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.update_telegram_metadata_dto import UpdateTelegramMetadataDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MembersApi(api_client)
    id = 'id_example' # str | 
    update_telegram_metadata_dto = openapi_client.UpdateTelegramMetadataDTO() # UpdateTelegramMetadataDTO | 

    try:
        # Add/update Telegram metadata for member
        api_response = api_instance.members_controller_update_telegram_metadata(id, update_telegram_metadata_dto)
        print("The response of MembersApi->members_controller_update_telegram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_controller_update_telegram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_telegram_metadata_dto** | [**UpdateTelegramMetadataDTO**](UpdateTelegramMetadataDTO.md)|  | 

### Return type

**object**

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

