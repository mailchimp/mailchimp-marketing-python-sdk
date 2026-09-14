# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListEepurlReportsResponseReferrersItem(UniversalBaseModel):
    """
    A single instance of a campaign referral.
    """

    clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of clicks a single referrer generated.
    """

    first_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp for the first click from this referrer.
    """

    last_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp for the last click from this referrer.
    """

    referrer: typing.Optional[str] = pydantic.Field(default=None)
    """
    A referrer (truncated to 100 bytes).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
