# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaigns_resend_shortcut_usage_original_campaign_shortcut_type import (
    CampaignsResendShortcutUsageOriginalCampaignShortcutType,
)


class CampaignsResendShortcutUsageOriginalCampaign(UniversalBaseModel):
    """
    The original campaign that was resent.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID for the resent campaign.
    """

    shortcut_type: typing.Optional[CampaignsResendShortcutUsageOriginalCampaignShortcutType] = pydantic.Field(
        default=None
    )
    """
    Which campaign resend shortcut was used.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the original campaign.
    """

    web_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID for the resent campaign used in the Mailchimp web application. View this campaign in your Mailchimp account at `https://{dc}.admin.mailchimp.com/campaigns/show/?id={web_id}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
