# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_section_request_question_options_item import SurveySectionRequestQuestionOptionsItem
from .survey_section_request_question_type import SurveySectionRequestQuestionType


class SurveySectionRequestQuestion(UniversalBaseModel):
    """
    A survey question. On PATCH, include the question id to update it. Omitting question id creates a new question; it does not delete an existing one. To delete a question, omit its section from the sections array.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The question ID. On PATCH, include to update an existing question; omit to add a new question.
    """

    query: str = pydantic.Field()
    """
    The question text.
    """

    type: SurveySectionRequestQuestionType = pydantic.Field()
    """
    The response type of the survey question.
    """

    is_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this question is required.
    """

    has_other: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this question has an 'other' option.
    """

    other_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the 'other' option.
    """

    range_low_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the low end of a range question.
    """

    range_high_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the high end of a range question.
    """

    range_low_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Low value for a range question.
    """

    range_high_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    High value for a range question.
    """

    range_presentation: typing.Optional[str] = pydantic.Field(default=None)
    """
    How a range question is presented.
    """

    placeholder_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Placeholder text for text or email questions.
    """

    subscribe_checkbox_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the subscribe checkbox is enabled.
    """

    subscribe_checkbox_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the subscribe checkbox.
    """

    should_auto_tag: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether responses should automatically apply tags.
    """

    options: typing.Optional[typing.List[SurveySectionRequestQuestionOptionsItem]] = pydantic.Field(default=None)
    """
    Answer options for pickOne, pickMany, or dropdown questions.
    """

    merge_field: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Merge field mapping for contact information questions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
