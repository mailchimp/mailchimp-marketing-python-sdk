# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListMembersLocation(UniversalBaseModel):
    """
    Subscriber location information.
    """

    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique code for the location country.
    """

    dstoff: typing.Optional[int] = pydantic.Field(default=None)
    """
    The offset for timezones where daylight saving time is observed.
    """

    gmtoff: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time difference in hours from GMT.
    """

    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The location latitude.
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The location longitude.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region for the location.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timezone for the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
