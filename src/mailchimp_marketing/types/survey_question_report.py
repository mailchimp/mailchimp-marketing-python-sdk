# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_question_report_contact_counts import SurveyQuestionReportContactCounts
from .survey_question_report_merge_field import SurveyQuestionReportMergeField
from .survey_question_report_options_item import SurveyQuestionReportOptionsItem
from .survey_question_report_type import SurveyQuestionReportType


class SurveyQuestionReport(UniversalBaseModel):
    """
    The details of a survey question's report.
    """

    average_rating: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average rating for this range question.
    """

    contact_counts: typing.Optional[SurveyQuestionReportContactCounts] = pydantic.Field(default=None)
    """
    For email question types, how many are new, known, or unknown contacts.
    """

    has_other: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this survey question has an 'other' option.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the survey question.
    """

    is_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this survey question is required to answer.
    """

    merge_field: typing.Optional[SurveyQuestionReportMergeField] = pydantic.Field(default=None)
    """
    A [merge field](https://mailchimp.com/developer/marketing/docs/merge-fields/) for an audience.
    """

    options: typing.Optional[typing.List[SurveyQuestionReportOptionsItem]] = pydantic.Field(default=None)
    """
    The answer choices for this question.
    """

    other_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label used for the 'other' option of this survey question.
    """

    placeholder_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Placeholder text for this survey question's answer box.
    """

    query: typing.Optional[str] = pydantic.Field(default=None)
    """
    The query of the survey question.
    """

    range_high_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the high end of the range.
    """

    range_low_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the low end of the range.
    """

    subscribe_checkbox_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the subscribe checkbox is shown for this email question.
    """

    subscribe_checkbox_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label used for the subscribe checkbox for this email question.
    """

    survey_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the survey.
    """

    total_responses: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of responses to this question.
    """

    type: typing.Optional[SurveyQuestionReportType] = pydantic.Field(default=None)
    """
    The response type of the survey question.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
