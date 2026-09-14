# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListEepurlReportsResponseClicksLocationsItem(UniversalBaseModel):
    """
    An individual click location.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two-digit country code for a recorded click.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    If available, a specific region where the click was recorded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
