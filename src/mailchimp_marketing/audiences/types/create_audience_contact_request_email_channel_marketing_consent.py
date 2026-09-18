# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_audience_contact_request_email_channel_marketing_consent_status import (
    CreateAudienceContactRequestEmailChannelMarketingConsentStatus,
)


class CreateAudienceContactRequestEmailChannelMarketingConsent(UniversalBaseModel):
    """
    A contact's current consent status for email marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    status: typing.Optional[CreateAudienceContactRequestEmailChannelMarketingConsentStatus] = pydantic.Field(
        default=None
    )
    """
    Status of a contacts Marketing Consent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
