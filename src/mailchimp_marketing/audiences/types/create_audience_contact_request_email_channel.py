# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_audience_contact_request_email_channel_marketing_consent import (
    CreateAudienceContactRequestEmailChannelMarketingConsent,
)


class CreateAudienceContactRequestEmailChannel(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address
    """

    marketing_consent: typing.Optional[CreateAudienceContactRequestEmailChannelMarketingConsent] = pydantic.Field(
        default=None
    )
    """
    A contact's current consent status for email marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
