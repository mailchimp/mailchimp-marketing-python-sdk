# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_goal_timestamp_field import SegmentTypeItemGoalTimestampField
from .segment_type_item_goal_timestamp_op import SegmentTypeItemGoalTimestampOp


class SegmentTypeItemGoalTimestamp(UniversalBaseModel):
    """
    Segment by most recent interaction with a website.
    """

    field: SegmentTypeItemGoalTimestampField = pydantic.Field()
    """
    Segment by most recent interaction with a website.
    """

    op: SegmentTypeItemGoalTimestampOp = pydantic.Field()
    """
    Whether the website activity happened after, before, or at a given timestamp.
    """

    value: str = pydantic.Field()
    """
    The date to check Goal activity against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
