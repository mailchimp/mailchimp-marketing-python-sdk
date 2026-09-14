# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubscriberListStats(UniversalBaseModel):
    """
    Stats for the list. Many of these are cached for at least five minutes.
    """

    avg_sub_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average number of subscriptions per month for the list (not returned if we haven't calculated it yet).
    """

    avg_unsub_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average number of unsubscriptions per month for the list (not returned if we haven't calculated it yet).
    """

    campaign_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of campaigns in any status that use this list.
    """

    campaign_last_sent: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the last campaign was sent to this list in ISO 8601 format. This is updated when a campaign is sent to 10 or more recipients.
    """

    cleaned_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of members cleaned from the list.
    """

    cleaned_count_since_send: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of members cleaned from the list since the last campaign was sent.
    """

    click_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average click rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).
    """

    last_sub_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the last time someone subscribed to this list in ISO 8601 format.
    """

    last_unsub_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the last time someone unsubscribed from this list in ISO 8601 format.
    """

    member_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of active members in the list.
    """

    member_count_since_send: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of active members in the list since the last campaign was sent.
    """

    merge_field_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of merge fields ([audience field](https://mailchimp.com/help/getting-started-with-merge-tags/)) for this list (doesn't include EMAIL).
    """

    open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average open rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).
    """

    target_sub_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The target number of subscriptions per month for the list to keep it growing (not returned if we haven't calculated it yet).
    """

    total_contacts: typing.Optional[int] = pydantic.Field(default=None)
    """
    An approximate count of subscribed, unsubscribed, and transactional contacts in the list. Does not include cleaned, archived, pending, or contacts that need to be reconfirmed. Requires the (deprecated) include_total_contacts query parameter to be included; for a complete audience contact count, use the /audiences endpoint instead.
    """

    unsubscribe_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of members who have unsubscribed from the list.
    """

    unsubscribe_count_since_send: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of members who have unsubscribed since the last campaign was sent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
