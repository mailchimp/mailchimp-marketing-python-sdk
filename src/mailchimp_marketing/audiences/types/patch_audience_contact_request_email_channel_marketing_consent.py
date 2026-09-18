# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_audience_contact_request_email_channel_marketing_consent_source import (
    PatchAudienceContactRequestEmailChannelMarketingConsentSource,
)
from .patch_audience_contact_request_email_channel_marketing_consent_status import (
    PatchAudienceContactRequestEmailChannelMarketingConsentStatus,
)


class PatchAudienceContactRequestEmailChannelMarketingConsent(UniversalBaseModel):
    """
    A contact's current consent status for email marketing communications. See the [Audiences (BETA) documentation](https://mailchimp.com/developer/marketing/docs/audiences-introduction) to learn about supported values.
    """

    source: typing.Optional[PatchAudienceContactRequestEmailChannelMarketingConsentSource] = pydantic.Field(
        default=None
    )
    """
    The source from which the parent's entity was created.
    """

    status: typing.Optional[PatchAudienceContactRequestEmailChannelMarketingConsentStatus] = None
    captured_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The ISO 8601 timestamp when the email marketing consent state was recorded; accepted and returned only when status is `confirmed` or `consented`; defaults to the current time if omitted; ignored if older than an existing stored timestamp (staleness guard).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
