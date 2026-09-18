# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_audience_contact_request_sms_channel_marketing_consent import (
    PatchAudienceContactRequestSmsChannelMarketingConsent,
)


class PatchAudienceContactRequestSmsChannel(UniversalBaseModel):
    marketing_consent: typing.Optional[PatchAudienceContactRequestSmsChannelMarketingConsent] = pydantic.Field(
        default=None
    )
    """
    A contact's current consent status for SMS marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    sms_phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    SMS Phone Number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
