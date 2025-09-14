# openapi_client.MembershipSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_subscriptions_controller_find_all_by_member_id**](MembershipSubscriptionsApi.md#membership_subscriptions_controller_find_all_by_member_id) | **GET** /api/membership-subscriptions/member/{memberId} | Get all membership subscriptions for member
[**membership_subscriptions_controller_find_all_by_membership_id**](MembershipSubscriptionsApi.md#membership_subscriptions_controller_find_all_by_membership_id) | **GET** /api/membership-subscriptions/membership/{membershipId} | Get all membership subscriptions for membership
[**membership_subscriptions_controller_stats**](MembershipSubscriptionsApi.md#membership_subscriptions_controller_stats) | **GET** /api/membership-subscriptions/stats | Get all membership subscriptions statistics
[**membership_subscriptions_controller_subscribe**](MembershipSubscriptionsApi.md#membership_subscriptions_controller_subscribe) | **POST** /api/membership-subscriptions | Subscribe member to membership
[**membership_subscriptions_controller_unsubscribe**](MembershipSubscriptionsApi.md#membership_subscriptions_controller_unsubscribe) | **DELETE** /api/membership-subscriptions/{id} | Unsubscribe member from membership


# **membership_subscriptions_controller_find_all_by_member_id**
> List[MembershipSubscriptionDTO] membership_subscriptions_controller_find_all_by_member_id(member_id)

Get all membership subscriptions for member

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.membership_subscription_dto import MembershipSubscriptionDTO
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
    api_instance = openapi_client.MembershipSubscriptionsApi(api_client)
    member_id = 'member_id_example' # str | 

    try:
        # Get all membership subscriptions for member
        api_response = api_instance.membership_subscriptions_controller_find_all_by_member_id(member_id)
        print("The response of MembershipSubscriptionsApi->membership_subscriptions_controller_find_all_by_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipSubscriptionsApi->membership_subscriptions_controller_find_all_by_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 

### Return type

[**List[MembershipSubscriptionDTO]**](MembershipSubscriptionDTO.md)

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

# **membership_subscriptions_controller_find_all_by_membership_id**
> List[MembershipSubscriptionDTO] membership_subscriptions_controller_find_all_by_membership_id(membership_id)

Get all membership subscriptions for membership

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.membership_subscription_dto import MembershipSubscriptionDTO
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
    api_instance = openapi_client.MembershipSubscriptionsApi(api_client)
    membership_id = 'membership_id_example' # str | 

    try:
        # Get all membership subscriptions for membership
        api_response = api_instance.membership_subscriptions_controller_find_all_by_membership_id(membership_id)
        print("The response of MembershipSubscriptionsApi->membership_subscriptions_controller_find_all_by_membership_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipSubscriptionsApi->membership_subscriptions_controller_find_all_by_membership_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **str**|  | 

### Return type

[**List[MembershipSubscriptionDTO]**](MembershipSubscriptionDTO.md)

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

# **membership_subscriptions_controller_stats**
> MembershipSubscriptionStatsDTO membership_subscriptions_controller_stats()

Get all membership subscriptions statistics

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.membership_subscription_stats_dto import MembershipSubscriptionStatsDTO
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
    api_instance = openapi_client.MembershipSubscriptionsApi(api_client)

    try:
        # Get all membership subscriptions statistics
        api_response = api_instance.membership_subscriptions_controller_stats()
        print("The response of MembershipSubscriptionsApi->membership_subscriptions_controller_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipSubscriptionsApi->membership_subscriptions_controller_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MembershipSubscriptionStatsDTO**](MembershipSubscriptionStatsDTO.md)

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

# **membership_subscriptions_controller_subscribe**
> MembershipSubscriptionDTO membership_subscriptions_controller_subscribe(subscribe_dto)

Subscribe member to membership

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.membership_subscription_dto import MembershipSubscriptionDTO
from openapi_client.models.subscribe_dto import SubscribeDTO
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
    api_instance = openapi_client.MembershipSubscriptionsApi(api_client)
    subscribe_dto = openapi_client.SubscribeDTO() # SubscribeDTO | 

    try:
        # Subscribe member to membership
        api_response = api_instance.membership_subscriptions_controller_subscribe(subscribe_dto)
        print("The response of MembershipSubscriptionsApi->membership_subscriptions_controller_subscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipSubscriptionsApi->membership_subscriptions_controller_subscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribe_dto** | [**SubscribeDTO**](SubscribeDTO.md)|  | 

### Return type

[**MembershipSubscriptionDTO**](MembershipSubscriptionDTO.md)

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

# **membership_subscriptions_controller_unsubscribe**
> object membership_subscriptions_controller_unsubscribe(id)

Unsubscribe member from membership

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
    api_instance = openapi_client.MembershipSubscriptionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unsubscribe member from membership
        api_response = api_instance.membership_subscriptions_controller_unsubscribe(id)
        print("The response of MembershipSubscriptionsApi->membership_subscriptions_controller_unsubscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipSubscriptionsApi->membership_subscriptions_controller_unsubscribe: %s\n" % e)
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

