# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmailActivityActivityItem(UniversalBaseModel):
    """
    A summary of the interaction with the campaign.
    """

    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    One of the following actions: 'open', 'click', or 'bounce'
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address recorded for the action.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time recorded for the action in ISO 8601 format.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the action is a 'bounce', the type of bounce received: 'hard', 'soft'.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the action is a 'click', the URL on which the member clicked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
