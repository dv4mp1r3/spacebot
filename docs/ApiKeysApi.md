# openapi_client.ApiKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_controller_create**](ApiKeysApi.md#api_keys_controller_create) | **POST** /api/api-keys | Create new API key
[**api_keys_controller_find_my**](ApiKeysApi.md#api_keys_controller_find_my) | **GET** /api/api-keys | Get your API keys
[**api_keys_controller_remove**](ApiKeysApi.md#api_keys_controller_remove) | **DELETE** /api/api-keys/{id} | Delete API key


# **api_keys_controller_create**
> ApiKeyDTO api_keys_controller_create()

Create new API key

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.api_key_dto import ApiKeyDTO
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
    api_instance = openapi_client.ApiKeysApi(api_client)

    try:
        # Create new API key
        api_response = api_instance.api_keys_controller_create()
        print("The response of ApiKeysApi->api_keys_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_controller_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

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

# **api_keys_controller_find_my**
> List[ApiKeyDTO] api_keys_controller_find_my()

Get your API keys

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.api_key_dto import ApiKeyDTO
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
    api_instance = openapi_client.ApiKeysApi(api_client)

    try:
        # Get your API keys
        api_response = api_instance.api_keys_controller_find_my()
        print("The response of ApiKeysApi->api_keys_controller_find_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_controller_find_my: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyDTO]**](ApiKeyDTO.md)

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

# **api_keys_controller_remove**
> object api_keys_controller_remove(id)

Delete API key

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
    api_instance = openapi_client.ApiKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete API key
        api_response = api_instance.api_keys_controller_remove(id)
        print("The response of ApiKeysApi->api_keys_controller_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_controller_remove: %s\n" % e)
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

