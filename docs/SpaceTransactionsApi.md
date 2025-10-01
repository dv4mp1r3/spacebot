# openapi_client.SpaceTransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**space_transactions_controller_create**](SpaceTransactionsApi.md#space_transactions_controller_create) | **POST** /api/space-transactions | Create new space transaction
[**space_transactions_controller_find_all**](SpaceTransactionsApi.md#space_transactions_controller_find_all) | **GET** /api/space-transactions | Get all space transactions
[**space_transactions_controller_find_all_by_actor**](SpaceTransactionsApi.md#space_transactions_controller_find_all_by_actor) | **GET** /api/space-transactions/actor/{memberId} | Get all space transactions


# **space_transactions_controller_create**
> List[SpaceTransactionDTO] space_transactions_controller_create(create_space_transaction_dto)

Create new space transaction

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_space_transaction_dto import CreateSpaceTransactionDTO
from openapi_client.models.space_transaction_dto import SpaceTransactionDTO
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
    api_instance = openapi_client.SpaceTransactionsApi(api_client)
    create_space_transaction_dto = openapi_client.CreateSpaceTransactionDTO() # CreateSpaceTransactionDTO | 

    try:
        # Create new space transaction
        api_response = api_instance.space_transactions_controller_create(create_space_transaction_dto)
        print("The response of SpaceTransactionsApi->space_transactions_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceTransactionsApi->space_transactions_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_space_transaction_dto** | [**CreateSpaceTransactionDTO**](CreateSpaceTransactionDTO.md)|  | 

### Return type

[**List[SpaceTransactionDTO]**](SpaceTransactionDTO.md)

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

# **space_transactions_controller_find_all**
> SpaceTransactionsDTO space_transactions_controller_find_all(offset, count, order_by, order_direction)

Get all space transactions

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.space_transactions_dto import SpaceTransactionsDTO
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
    api_instance = openapi_client.SpaceTransactionsApi(api_client)
    offset = 'offset_example' # str | 
    count = 'count_example' # str | 
    order_by = 'order_by_example' # str | 
    order_direction = 'order_direction_example' # str | 

    try:
        # Get all space transactions
        api_response = api_instance.space_transactions_controller_find_all(offset, count, order_by, order_direction)
        print("The response of SpaceTransactionsApi->space_transactions_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceTransactionsApi->space_transactions_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**|  | 
 **count** | **str**|  | 
 **order_by** | **str**|  | 
 **order_direction** | **str**|  | 

### Return type

[**SpaceTransactionsDTO**](SpaceTransactionsDTO.md)

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

# **space_transactions_controller_find_all_by_actor**
> SpaceTransactionsDTO space_transactions_controller_find_all_by_actor(member_id, offset, count, order_by, order_direction)

Get all space transactions

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.space_transactions_dto import SpaceTransactionsDTO
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
    api_instance = openapi_client.SpaceTransactionsApi(api_client)
    member_id = 'member_id_example' # str | 
    offset = 'offset_example' # str | 
    count = 'count_example' # str | 
    order_by = 'order_by_example' # str | 
    order_direction = 'order_direction_example' # str | 

    try:
        # Get all space transactions
        api_response = api_instance.space_transactions_controller_find_all_by_actor(member_id, offset, count, order_by, order_direction)
        print("The response of SpaceTransactionsApi->space_transactions_controller_find_all_by_actor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceTransactionsApi->space_transactions_controller_find_all_by_actor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **offset** | **str**|  | 
 **count** | **str**|  | 
 **order_by** | **str**|  | 
 **order_direction** | **str**|  | 

### Return type

[**SpaceTransactionsDTO**](SpaceTransactionsDTO.md)

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

