# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_goal_activity_field import SegmentTypeItemGoalActivityField
from .segment_type_item_goal_activity_op import SegmentTypeItemGoalActivityOp


class SegmentTypeItemGoalActivity(UniversalBaseModel):
    """
    Segment by Goal activity.
    """

    field: SegmentTypeItemGoalActivityField = pydantic.Field()
    """
    Segment by Goal activity.
    """

    op: SegmentTypeItemGoalActivityOp = pydantic.Field()
    """
    Whether the website URL is/not exactly, contains/doesn't contain, starts with/ends with a string.
    """

    value: str = pydantic.Field()
    """
    The URL to check Goal activity against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
