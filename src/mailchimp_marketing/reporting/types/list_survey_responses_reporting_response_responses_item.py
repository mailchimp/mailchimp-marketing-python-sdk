# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_survey_responses_reporting_response_responses_item_contact import (
    ListSurveyResponsesReportingResponseResponsesItemContact,
)


class ListSurveyResponsesReportingResponseResponsesItem(UniversalBaseModel):
    """
    Survey respondent details.
    """

    contact: typing.Optional[ListSurveyResponsesReportingResponseResponsesItemContact] = pydantic.Field(default=None)
    """
    Information about the contact.
    """

    is_new_contact: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this contact was added to the Mailchimp audience via this survey.
    """

    response_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID for the survey response.
    """

    submitted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the survey response was submitted in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
