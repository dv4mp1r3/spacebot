# openapi_client.AcsKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_cs_keys_controller_create**](AcsKeysApi.md#a_cs_keys_controller_create) | **POST** /api/acs-keys | Create ACS key
[**a_cs_keys_controller_find_all_by_member_id**](AcsKeysApi.md#a_cs_keys_controller_find_all_by_member_id) | **GET** /api/acs-keys/member/{memberId} | Get ACS keys for specific member
[**a_cs_keys_controller_remove**](AcsKeysApi.md#a_cs_keys_controller_remove) | **DELETE** /api/acs-keys/{id} | Delete ACS key


# **a_cs_keys_controller_create**
> ACSKeyDTO a_cs_keys_controller_create(create_acs_key_dto)

Create ACS key

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.acs_key_dto import ACSKeyDTO
from openapi_client.models.create_acs_key_dto import CreateACSKeyDTO
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
    api_instance = openapi_client.AcsKeysApi(api_client)
    create_acs_key_dto = openapi_client.CreateACSKeyDTO() # CreateACSKeyDTO | 

    try:
        # Create ACS key
        api_response = api_instance.a_cs_keys_controller_create(create_acs_key_dto)
        print("The response of AcsKeysApi->a_cs_keys_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcsKeysApi->a_cs_keys_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_acs_key_dto** | [**CreateACSKeyDTO**](CreateACSKeyDTO.md)|  | 

### Return type

[**ACSKeyDTO**](ACSKeyDTO.md)

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

# **a_cs_keys_controller_find_all_by_member_id**
> List[ACSKeyDTO] a_cs_keys_controller_find_all_by_member_id(member_id)

Get ACS keys for specific member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.acs_key_dto import ACSKeyDTO
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
    api_instance = openapi_client.AcsKeysApi(api_client)
    member_id = 'member_id_example' # str | 

    try:
        # Get ACS keys for specific member
        api_response = api_instance.a_cs_keys_controller_find_all_by_member_id(member_id)
        print("The response of AcsKeysApi->a_cs_keys_controller_find_all_by_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcsKeysApi->a_cs_keys_controller_find_all_by_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 

### Return type

[**List[ACSKeyDTO]**](ACSKeyDTO.md)

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

# **a_cs_keys_controller_remove**
> object a_cs_keys_controller_remove(id)

Delete ACS key

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
    api_instance = openapi_client.AcsKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete ACS key
        api_response = api_instance.a_cs_keys_controller_remove(id)
        print("The response of AcsKeysApi->a_cs_keys_controller_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcsKeysApi->a_cs_keys_controller_remove: %s\n" % e)
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

