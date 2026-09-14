# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaigns_resend_shortcut_usage_original_campaign import CampaignsResendShortcutUsageOriginalCampaign
from .campaigns_resend_shortcut_usage_shortcut_campaigns_item import CampaignsResendShortcutUsageShortcutCampaignsItem


class CampaignsResendShortcutUsage(UniversalBaseModel):
    """
    Information about campaigns related through shortcuts.
    """

    original_campaign: typing.Optional[CampaignsResendShortcutUsageOriginalCampaign] = pydantic.Field(default=None)
    """
    The original campaign that was resent.
    """

    shortcut_campaigns: typing.Optional[typing.List[CampaignsResendShortcutUsageShortcutCampaignsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Campaigns that were created from Campaign Resend Shortcuts for this campaign
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
