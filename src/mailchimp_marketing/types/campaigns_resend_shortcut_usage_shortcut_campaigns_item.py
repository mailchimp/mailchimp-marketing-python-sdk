# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaigns_resend_shortcut_usage_shortcut_campaigns_item_shortcut_type import (
    CampaignsResendShortcutUsageShortcutCampaignsItemShortcutType,
)
from .campaigns_resend_shortcut_usage_shortcut_campaigns_item_status import (
    CampaignsResendShortcutUsageShortcutCampaignsItemStatus,
)


class CampaignsResendShortcutUsageShortcutCampaignsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID for the resent campaign.
    """

    send_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time a resent campaign was sent.
    """

    shortcut_type: typing.Optional[CampaignsResendShortcutUsageShortcutCampaignsItemShortcutType] = pydantic.Field(
        default=None
    )
    """
    Which campaign resend shortcut was used.
    """

    status: typing.Optional[CampaignsResendShortcutUsageShortcutCampaignsItemStatus] = pydantic.Field(default=None)
    """
    The current status of the campaign.
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
