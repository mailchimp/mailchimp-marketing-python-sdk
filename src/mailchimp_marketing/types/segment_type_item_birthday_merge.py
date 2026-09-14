# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_birthday_merge_op import SegmentTypeItemBirthdayMergeOp


class SegmentTypeItemBirthdayMerge(UniversalBaseModel):
    """
    Segment by a contact's birthday.
    """

    field: str = pydantic.Field()
    """
    A date merge field to segment.
    """

    op: SegmentTypeItemBirthdayMergeOp = pydantic.Field()
    """
    Whether the member's birthday merge information is/is not a certain date or is/is not blank.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    A date to segment against (mm/dd).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
