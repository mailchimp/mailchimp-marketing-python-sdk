# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_language_field import SegmentTypeItemLanguageField
from .segment_type_item_language_op import SegmentTypeItemLanguageOp


class SegmentTypeItemLanguage(UniversalBaseModel):
    """
    Segment by language.
    """

    field: SegmentTypeItemLanguageField = pydantic.Field()
    """
    Segmenting based off of a subscriber's language.
    """

    op: SegmentTypeItemLanguageOp = pydantic.Field()
    """
    Whether the member's language is or is not set to a specific language.
    """

    value: str = pydantic.Field()
    """
    A two-letter language identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
