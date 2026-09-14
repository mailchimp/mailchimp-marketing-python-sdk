# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_survey_monkey_field import SegmentTypeItemSurveyMonkeyField
from .segment_type_item_survey_monkey_op import SegmentTypeItemSurveyMonkeyOp


class SegmentTypeItemSurveyMonkey(UniversalBaseModel):
    """
    Segment by interaction with a SurveyMonkey survey.
    """

    field: SegmentTypeItemSurveyMonkeyField = pydantic.Field()
    """
    Segment by interaction with a SurveyMonkey survey.
    """

    op: SegmentTypeItemSurveyMonkeyOp = pydantic.Field()
    """
    The status of the member with regard to the survey.One of the following: has started the survey, has completed the survey, has not started the survey, or has not completed the survey.
    """

    value: str = pydantic.Field()
    """
    The unique ID of the survey monkey survey.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
