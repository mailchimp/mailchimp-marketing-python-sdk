# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_surveys_reporting_response_surveys_item_status import ListSurveysReportingResponseSurveysItemStatus


class ListSurveysReportingResponseSurveysItem(UniversalBaseModel):
    """
    The report for a survey.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the survey was created in ISO 8601 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this survey.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the list connected to this survey.
    """

    list_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the list connected to this survey.
    """

    published_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the survey was published in ISO 8601 format.
    """

    status: typing.Optional[ListSurveysReportingResponseSurveysItemStatus] = pydantic.Field(default=None)
    """
    The survey's status.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the survey.
    """

    total_responses: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of responses to this survey.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the survey was last updated in ISO 8601 format.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the survey.
    """

    web_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID used in the Mailchimp web application. View this survey report in your Mailchimp account at `https://{dc}.admin.mailchimp.com/lists/surveys/results?survey_id={web_id}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
