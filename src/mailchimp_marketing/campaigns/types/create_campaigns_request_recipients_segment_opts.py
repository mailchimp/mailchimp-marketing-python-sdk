# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.segment_type import SegmentType
from .create_campaigns_request_recipients_segment_opts_match import CreateCampaignsRequestRecipientsSegmentOptsMatch


class CreateCampaignsRequestRecipientsSegmentOpts(UniversalBaseModel):
    """
    An object representing all segmentation options. This object should contain a `saved_segment_id` to use an existing segment, or you can create a new segment by including both `match` and `conditions` options.
    """

    conditions: typing.Optional[SegmentType] = None
    match: typing.Optional[CreateCampaignsRequestRecipientsSegmentOptsMatch] = pydantic.Field(default=None)
    """
    Segment match type.
    """

    saved_segment_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id for an existing saved segment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
