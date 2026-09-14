# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_select_merge_op import SegmentTypeItemSelectMergeOp


class SegmentTypeItemSelectMerge(UniversalBaseModel):
    """
    An individual segment condition
    """

    field: str = pydantic.Field()
    """
    A merge field to segment.
    """

    op: SegmentTypeItemSelectMergeOp = pydantic.Field()
    """
    Whether the member's merge information is/is not a value or is/is not blank.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value to segment a text merge field with.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
