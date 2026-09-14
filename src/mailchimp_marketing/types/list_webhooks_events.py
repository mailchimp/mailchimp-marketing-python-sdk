# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListWebhooksEvents(UniversalBaseModel):
    """
    The events that can trigger the webhook and whether they are enabled.
    """

    campaign: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a campaign is sent or cancelled.
    """

    cleaned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a subscriber's email address is cleaned from the list.
    """

    profile: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a contact's profile is updated. This includes email subscribers and SMS-only contacts [BETA].
    """

    subscribe: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a list subscriber is added.
    """

    unsubscribe: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a list member unsubscribes.
    """

    upemail: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is triggered when a subscriber's email address is changed.
    """

    sms_subscribe: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [BETA] Whether the webhook is triggered when a contact subscribes to SMS.
    """

    sms_unsubscribe: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [BETA] Whether the webhook is triggered when a contact unsubscribes from SMS.
    """

    upsms: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [BETA] Whether the webhook is triggered when a contact's SMS phone number is updated.
    """

    sms_campaign: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [BETA] Whether the webhook is triggered when an SMS campaign is sent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
