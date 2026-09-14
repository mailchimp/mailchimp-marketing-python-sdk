# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_survey_respons_reporting_response_results_item_question_type import (
    GetSurveyResponsReportingResponseResultsItemQuestionType,
)


class GetSurveyResponsReportingResponseResultsItem(UniversalBaseModel):
    """
    A single question and the response to that question.
    """

    answer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The answer to this survey question.
    """

    query: typing.Optional[str] = pydantic.Field(default=None)
    """
    The survey question.
    """

    question_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for this question.
    """

    question_type: typing.Optional[GetSurveyResponsReportingResponseResultsItemQuestionType] = pydantic.Field(
        default=None
    )
    """
    The type of question this is.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
