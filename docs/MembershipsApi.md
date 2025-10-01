# openapi_client.MembershipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memberships_controller_create**](MembershipsApi.md#memberships_controller_create) | **POST** /api/memberships | Create new membership
[**memberships_controller_find_all**](MembershipsApi.md#memberships_controller_find_all) | **GET** /api/memberships | Get all memberships
[**memberships_controller_update_membership**](MembershipsApi.md#memberships_controller_update_membership) | **PATCH** /api/memberships/{id} | Update membership


# **memberships_controller_create**
> MembershipDTO memberships_controller_create(create_update_membership_dto)

Create new membership

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_update_membership_dto import CreateUpdateMembershipDTO
from openapi_client.models.membership_dto import MembershipDTO
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
    api_instance = openapi_client.MembershipsApi(api_client)
    create_update_membership_dto = openapi_client.CreateUpdateMembershipDTO() # CreateUpdateMembershipDTO | 

    try:
        # Create new membership
        api_response = api_instance.memberships_controller_create(create_update_membership_dto)
        print("The response of MembershipsApi->memberships_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipsApi->memberships_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_membership_dto** | [**CreateUpdateMembershipDTO**](CreateUpdateMembershipDTO.md)|  | 

### Return type

[**MembershipDTO**](MembershipDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfull response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memberships_controller_find_all**
> List[MembershipDTO] memberships_controller_find_all()

Get all memberships

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.membership_dto import MembershipDTO
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
    api_instance = openapi_client.MembershipsApi(api_client)

    try:
        # Get all memberships
        api_response = api_instance.memberships_controller_find_all()
        print("The response of MembershipsApi->memberships_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipsApi->memberships_controller_find_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MembershipDTO]**](MembershipDTO.md)

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

# **memberships_controller_update_membership**
> MembershipDTO memberships_controller_update_membership(id, create_update_membership_dto)

Update membership

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_update_membership_dto import CreateUpdateMembershipDTO
from openapi_client.models.membership_dto import MembershipDTO
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
    api_instance = openapi_client.MembershipsApi(api_client)
    id = 'id_example' # str | 
    create_update_membership_dto = openapi_client.CreateUpdateMembershipDTO() # CreateUpdateMembershipDTO | 

    try:
        # Update membership
        api_response = api_instance.memberships_controller_update_membership(id, create_update_membership_dto)
        print("The response of MembershipsApi->memberships_controller_update_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipsApi->memberships_controller_update_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_update_membership_dto** | [**CreateUpdateMembershipDTO**](CreateUpdateMembershipDTO.md)|  | 

### Return type

[**MembershipDTO**](MembershipDTO.md)

### Authorization

[cookie](../README.md#cookie), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfull response |  -  |
**0** | Erroneous response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

