# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_question_report_merge_field_type import SurveyQuestionReportMergeFieldType


class SurveyQuestionReportMergeField(UniversalBaseModel):
    """
    A [merge field](https://mailchimp.com/developer/marketing/docs/merge-fields/) for an audience.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    An unchanging id for the merge field.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [label](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.
    """

    type: typing.Optional[SurveyQuestionReportMergeFieldType] = pydantic.Field(default=None)
    """
    The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
