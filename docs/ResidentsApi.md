# openapi_client.ResidentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_residents**](ResidentsApi.md#list_residents) | **GET** /api/tg-accounting/residents/debt | Get residents list


# **list_residents**
> list[Resident] list_residents(limit=limit, offset=offset)

Get residents list

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
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

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResidentsApi(api_client)
    limit = 100 # int | Record limit (optional) (default to 100)
offset = 0 # int | Record offset (optional) (default to 0)

    try:
        # Get residents list
        api_response = api_instance.list_residents(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResidentsApi->list_residents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Record limit | [optional] [default to 100]
 **offset** | **int**| Record offset | [optional] [default to 0]

### Return type

[**list[Resident]**](Resident.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success request |  * x-next - Success request <br>  |
**401** | Access token is missing or invalid |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

