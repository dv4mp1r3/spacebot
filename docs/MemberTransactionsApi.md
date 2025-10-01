# openapi_client.MemberTransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**member_transactions_controller_create**](MemberTransactionsApi.md#member_transactions_controller_create) | **POST** /api/member-transactions | Create new member transaction
[**member_transactions_controller_find_all**](MemberTransactionsApi.md#member_transactions_controller_find_all) | **GET** /api/member-transactions | Get all member transactions
[**member_transactions_controller_find_all_by_actor_member**](MemberTransactionsApi.md#member_transactions_controller_find_all_by_actor_member) | **GET** /api/member-transactions/actor/{memberId} | Get all member transactions for actor member
[**member_transactions_controller_find_all_by_subject_member**](MemberTransactionsApi.md#member_transactions_controller_find_all_by_subject_member) | **GET** /api/member-transactions/subject/{memberId} | Get all member transactions for subject member


# **member_transactions_controller_create**
> MemberTransactionDTO member_transactions_controller_create(create_member_transaction_dto)

Create new member transaction

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.create_member_transaction_dto import CreateMemberTransactionDTO
from openapi_client.models.member_transaction_dto import MemberTransactionDTO
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
    api_instance = openapi_client.MemberTransactionsApi(api_client)
    create_member_transaction_dto = openapi_client.CreateMemberTransactionDTO() # CreateMemberTransactionDTO | 

    try:
        # Create new member transaction
        api_response = api_instance.member_transactions_controller_create(create_member_transaction_dto)
        print("The response of MemberTransactionsApi->member_transactions_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberTransactionsApi->member_transactions_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_member_transaction_dto** | [**CreateMemberTransactionDTO**](CreateMemberTransactionDTO.md)|  | 

### Return type

[**MemberTransactionDTO**](MemberTransactionDTO.md)

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

# **member_transactions_controller_find_all**
> MemberTransactionsDTO member_transactions_controller_find_all(offset, count, order_by, order_direction)

Get all member transactions

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_transactions_dto import MemberTransactionsDTO
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
    api_instance = openapi_client.MemberTransactionsApi(api_client)
    offset = 'offset_example' # str | 
    count = 'count_example' # str | 
    order_by = 'order_by_example' # str | 
    order_direction = 'order_direction_example' # str | 

    try:
        # Get all member transactions
        api_response = api_instance.member_transactions_controller_find_all(offset, count, order_by, order_direction)
        print("The response of MemberTransactionsApi->member_transactions_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberTransactionsApi->member_transactions_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**|  | 
 **count** | **str**|  | 
 **order_by** | **str**|  | 
 **order_direction** | **str**|  | 

### Return type

[**MemberTransactionsDTO**](MemberTransactionsDTO.md)

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

# **member_transactions_controller_find_all_by_actor_member**
> MemberTransactionsDTO member_transactions_controller_find_all_by_actor_member(member_id, offset, count, order_by, order_direction)

Get all member transactions for actor member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_transactions_dto import MemberTransactionsDTO
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
    api_instance = openapi_client.MemberTransactionsApi(api_client)
    member_id = 'member_id_example' # str | 
    offset = 'offset_example' # str | 
    count = 'count_example' # str | 
    order_by = 'order_by_example' # str | 
    order_direction = 'order_direction_example' # str | 

    try:
        # Get all member transactions for actor member
        api_response = api_instance.member_transactions_controller_find_all_by_actor_member(member_id, offset, count, order_by, order_direction)
        print("The response of MemberTransactionsApi->member_transactions_controller_find_all_by_actor_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberTransactionsApi->member_transactions_controller_find_all_by_actor_member: %s\n" % e)
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

[**MemberTransactionsDTO**](MemberTransactionsDTO.md)

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

# **member_transactions_controller_find_all_by_subject_member**
> MemberTransactionsDTO member_transactions_controller_find_all_by_subject_member(member_id, offset, count, order_by, order_direction)

Get all member transactions for subject member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.member_transactions_dto import MemberTransactionsDTO
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
    api_instance = openapi_client.MemberTransactionsApi(api_client)
    member_id = 'member_id_example' # str | 
    offset = 'offset_example' # str | 
    count = 'count_example' # str | 
    order_by = 'order_by_example' # str | 
    order_direction = 'order_direction_example' # str | 

    try:
        # Get all member transactions for subject member
        api_response = api_instance.member_transactions_controller_find_all_by_subject_member(member_id, offset, count, order_by, order_direction)
        print("The response of MemberTransactionsApi->member_transactions_controller_find_all_by_subject_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberTransactionsApi->member_transactions_controller_find_all_by_subject_member: %s\n" % e)
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

[**MemberTransactionsDTO**](MemberTransactionsDTO.md)

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

