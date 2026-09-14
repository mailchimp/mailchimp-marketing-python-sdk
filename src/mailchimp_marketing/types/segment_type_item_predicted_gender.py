# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_predicted_gender_field import SegmentTypeItemPredictedGenderField
from .segment_type_item_predicted_gender_op import SegmentTypeItemPredictedGenderOp
from .segment_type_item_predicted_gender_value import SegmentTypeItemPredictedGenderValue


class SegmentTypeItemPredictedGender(UniversalBaseModel):
    """
    Segment by predicted gender.
    """

    field: SegmentTypeItemPredictedGenderField = pydantic.Field()
    """
    Segment by predicted gender.
    """

    op: SegmentTypeItemPredictedGenderOp = pydantic.Field()
    """
    Members who are/not the exact criteria listed.
    """

    value: SegmentTypeItemPredictedGenderValue = pydantic.Field()
    """
    The predicted gender to segment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
