# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_signup_source_field import SegmentTypeItemSignupSourceField
from .segment_type_item_signup_source_op import SegmentTypeItemSignupSourceOp


class SegmentTypeItemSignupSource(UniversalBaseModel):
    """
    Segment by signup source.
    """

    field: SegmentTypeItemSignupSourceField
    op: SegmentTypeItemSignupSourceOp = pydantic.Field()
    """
    Whether the member's signup source was/was not a particular value.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The signup source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
