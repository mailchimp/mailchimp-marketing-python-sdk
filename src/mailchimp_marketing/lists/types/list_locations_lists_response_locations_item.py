# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListLocationsListsResponseLocationsItem(UniversalBaseModel):
    cc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 3166 2 digit country code.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the country.
    """

    percent: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percent of subscribers in the country.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of subscribers in the country.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
