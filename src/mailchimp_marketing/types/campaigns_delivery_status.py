# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaigns_delivery_status_status import CampaignsDeliveryStatusStatus


class CampaignsDeliveryStatus(UniversalBaseModel):
    """
    Updates on campaigns in the process of sending.
    """

    can_cancel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a campaign send can be canceled.
    """

    emails_canceled: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of emails canceled for this campaign.
    """

    emails_sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of emails confirmed sent for this campaign so far.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Campaign Delivery Status is enabled for this account and campaign.
    """

    status: typing.Optional[CampaignsDeliveryStatusStatus] = pydantic.Field(default=None)
    """
    The current state of a campaign delivery.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
