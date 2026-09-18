# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audiences_contact_sms_channel_effective_subscription_status import (
    AudiencesContactSmsChannelEffectiveSubscriptionStatus,
)
from .audiences_contact_sms_channel_marketing_consent import AudiencesContactSmsChannelMarketingConsent
from .audiences_contact_sms_channel_source import AudiencesContactSmsChannelSource


class AudiencesContactSmsChannel(UniversalBaseModel):
    effective_subscription_status: typing.Optional[AudiencesContactSmsChannelEffectiveSubscriptionStatus] = (
        pydantic.Field(default=None)
    )
    """
    A computation performed by the Mailchimp platform, triggered whenever any of its inputs change. Some inputs are controlled by API users, while others are tracked internally by the platform. Computation is based on: audience opt-in configuration (single vs. double opt-in), marketing consent status, and deliverability status (an internal state for a contact, maintained by Mailchimp for a specific marketing channel instance). This new API field is distinct from how contacts are displayed in the UI. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    marketing_consent: typing.Optional[AudiencesContactSmsChannelMarketingConsent] = pydantic.Field(default=None)
    """
    A contact's current consent status for SMS marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    sms_phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    SMS Phone Number
    """

    source: typing.Optional[AudiencesContactSmsChannelSource] = pydantic.Field(default=None)
    """
    The source from which the parent's entity was created.
    """

    hashed_sms_phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 hash of the SMS phone number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
