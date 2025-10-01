# MembershipSubscriptionStatsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_active_amount** | **str** |  | 

## Example

```python
from openapi_client.models.membership_subscription_stats_dto import MembershipSubscriptionStatsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipSubscriptionStatsDTO from a JSON string
membership_subscription_stats_dto_instance = MembershipSubscriptionStatsDTO.from_json(json)
# print the JSON string representation of the object
print(MembershipSubscriptionStatsDTO.to_json())

# convert the object into a dict
membership_subscription_stats_dto_dict = membership_subscription_stats_dto_instance.to_dict()
# create an instance of MembershipSubscriptionStatsDTO from a dict
membership_subscription_stats_dto_from_dict = MembershipSubscriptionStatsDTO.from_dict(membership_subscription_stats_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


