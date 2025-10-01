# openapi_client.MacsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**m_acs_controller_create**](MacsApi.md#m_acs_controller_create) | **POST** /api/macs | Create new MAC
[**m_acs_controller_find_by_member_id**](MacsApi.md#m_acs_controller_find_by_member_id) | **GET** /api/macs/member/{memberId} | Get MACs for specific member
[**m_acs_controller_remove**](MacsApi.md#m_acs_controller_remove) | **DELETE** /api/macs/{id} | Delete MAC


# **m_acs_controller_create**
> MACDTO m_acs_controller_create(create_macdto)

Create new MAC

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_macdto import CreateMACDTO
from openapi_client.models.macdto import MACDTO
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
    api_instance = openapi_client.MacsApi(api_client)
    create_macdto = openapi_client.CreateMACDTO() # CreateMACDTO | 

    try:
        # Create new MAC
        api_response = api_instance.m_acs_controller_create(create_macdto)
        print("The response of MacsApi->m_acs_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacsApi->m_acs_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_macdto** | [**CreateMACDTO**](CreateMACDTO.md)|  | 

### Return type

[**MACDTO**](MACDTO.md)

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

# **m_acs_controller_find_by_member_id**
> List[MACDTO] m_acs_controller_find_by_member_id(member_id)

Get MACs for specific member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.macdto import MACDTO
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
    api_instance = openapi_client.MacsApi(api_client)
    member_id = 'member_id_example' # str | 

    try:
        # Get MACs for specific member
        api_response = api_instance.m_acs_controller_find_by_member_id(member_id)
        print("The response of MacsApi->m_acs_controller_find_by_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacsApi->m_acs_controller_find_by_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 

### Return type

[**List[MACDTO]**](MACDTO.md)

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

# **m_acs_controller_remove**
> object m_acs_controller_remove(id)

Delete MAC

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
    api_instance = openapi_client.MacsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete MAC
        api_response = api_instance.m_acs_controller_remove(id)
        print("The response of MacsApi->m_acs_controller_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacsApi->m_acs_controller_remove: %s\n" % e)
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

