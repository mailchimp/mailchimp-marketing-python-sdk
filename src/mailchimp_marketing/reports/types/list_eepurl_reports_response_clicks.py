# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_eepurl_reports_response_clicks_locations_item import ListEepurlReportsResponseClicksLocationsItem


class ListEepurlReportsResponseClicks(UniversalBaseModel):
    """
    A summary of the click-throughs on the campaign's URL.
    """

    clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of clicks to the campaign's URL.
    """

    first_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp for the first click to the URL.
    """

    last_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp for the last click to the URL.
    """

    locations: typing.Optional[typing.List[ListEepurlReportsResponseClicksLocationsItem]] = pydantic.Field(default=None)
    """
    A summary of the top click locations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
