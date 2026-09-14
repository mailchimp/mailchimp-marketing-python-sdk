# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_social_gender_field import SegmentTypeItemSocialGenderField
from .segment_type_item_social_gender_op import SegmentTypeItemSocialGenderOp
from .segment_type_item_social_gender_value import SegmentTypeItemSocialGenderValue


class SegmentTypeItemSocialGender(UniversalBaseModel):
    """
    Segment by listed gender in Social Profiles data.
    """

    field: SegmentTypeItemSocialGenderField = pydantic.Field()
    """
    Segment by listed gender in Social Profiles data.
    """

    op: SegmentTypeItemSocialGenderOp = pydantic.Field()
    """
    Members who are/not the exact criteria listed.
    """

    value: SegmentTypeItemSocialGenderValue = pydantic.Field()
    """
    The Social Profiles gender to segment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
