# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_campaign_poll_field import SegmentTypeItemCampaignPollField
from .segment_type_item_campaign_poll_op import SegmentTypeItemCampaignPollOp


class SegmentTypeItemCampaignPoll(UniversalBaseModel):
    """
    Segment by poll activity.
    """

    field: SegmentTypeItemCampaignPollField = pydantic.Field()
    """
    Segment by poll activity.
    """

    op: SegmentTypeItemCampaignPollOp = pydantic.Field()
    """
    Members have/have not interacted with a specific poll in a Mailchimp email.
    """

    value: float = pydantic.Field()
    """
    The id for the poll.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
