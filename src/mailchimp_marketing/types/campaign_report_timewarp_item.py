# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignReportTimewarpItem(UniversalBaseModel):
    bounces: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of bounces.
    """

    clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of clicks.
    """

    gmt_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    For campaigns sent with timewarp, the time zone group the member is apart of.
    """

    last_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the last click in ISO 8601 format.
    """

    last_open: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the last open in ISO 8601 format.
    """

    opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of opens.
    """

    unique_clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique clicks.
    """

    unique_opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique opens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
