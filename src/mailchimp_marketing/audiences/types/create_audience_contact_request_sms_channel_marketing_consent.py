# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_audience_contact_request_sms_channel_marketing_consent_source import (
    CreateAudienceContactRequestSmsChannelMarketingConsentSource,
)
from .create_audience_contact_request_sms_channel_marketing_consent_status import (
    CreateAudienceContactRequestSmsChannelMarketingConsentStatus,
)


class CreateAudienceContactRequestSmsChannelMarketingConsent(UniversalBaseModel):
    """
    A contact's current consent status for SMS marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    source: typing.Optional[CreateAudienceContactRequestSmsChannelMarketingConsentSource] = pydantic.Field(default=None)
    """
    The source from which the parent's entity was created.
    """

    status: typing.Optional[CreateAudienceContactRequestSmsChannelMarketingConsentStatus] = pydantic.Field(default=None)
    """
    The contact's SMS marketing consent status. Use `confirmed` for double opt-in audiences, `consented` for single opt-in audiences.
    """

    captured_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when SMS marketing consent was captured (ISO 8601). Only accepted and returned when status is `confirmed`. The timestamp of the consent state change being recorded. Defaults to the current time if not provided. If the contact already has a consent timestamp on record that is equal to or newer than the supplied value, the supplied value is ignored (staleness guard); to update the consent timestamp supply a value strictly newer than the stored one.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
