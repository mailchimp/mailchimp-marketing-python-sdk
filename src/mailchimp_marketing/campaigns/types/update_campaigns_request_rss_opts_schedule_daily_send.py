# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateCampaignsRequestRssOptsScheduleDailySend(UniversalBaseModel):
    """
    The days of the week to send a daily RSS Campaign.
    """

    friday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Fridays.
    """

    monday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Mondays.
    """

    saturday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Saturdays.
    """

    sunday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Sundays.
    """

    thursday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Thursdays.
    """

    tuesday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Tuesdays.
    """

    wednesday: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sends the daily RSS Campaign on Wednesdays.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
