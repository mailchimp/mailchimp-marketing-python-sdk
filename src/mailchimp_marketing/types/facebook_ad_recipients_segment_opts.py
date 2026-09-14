# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facebook_ad_recipients_segment_opts_match import FacebookAdRecipientsSegmentOptsMatch
from .facebook_ad_recipients_segment_opts_saved_segment_id import FacebookAdRecipientsSegmentOptsSavedSegmentId
from .segment_type import SegmentType


class FacebookAdRecipientsSegmentOpts(UniversalBaseModel):
    """
    An object representing all segmentation options. This object should contain a `saved_segment_id` to use an existing segment, or you can create a new segment by including both `match` and `conditions` options.
    """

    conditions: typing.Optional[SegmentType] = None
    match: typing.Optional[FacebookAdRecipientsSegmentOptsMatch] = pydantic.Field(default=None)
    """
    Segment match type.
    """

    prebuilt_segment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The prebuilt segment id, if a prebuilt segment has been designated for this campaign.
    """

    saved_segment_id: typing.Optional[FacebookAdRecipientsSegmentOptsSavedSegmentId] = pydantic.Field(default=None)
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
