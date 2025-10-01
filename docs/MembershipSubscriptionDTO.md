# MembershipSubscriptionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**member_id** | **str** |  | 
**membership_id** | **str** |  | 
**subscribed_at** | **datetime** |  | 
**declined_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.membership_subscription_dto import MembershipSubscriptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipSubscriptionDTO from a JSON string
membership_subscription_dto_instance = MembershipSubscriptionDTO.from_json(json)
# print the JSON string representation of the object
print(MembershipSubscriptionDTO.to_json())

# convert the object into a dict
membership_subscription_dto_dict = membership_subscription_dto_instance.to_dict()
# create an instance of MembershipSubscriptionDTO from a dict
membership_subscription_dto_from_dict = MembershipSubscriptionDTO.from_dict(membership_subscription_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


