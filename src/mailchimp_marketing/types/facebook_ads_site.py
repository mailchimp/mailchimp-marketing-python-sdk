# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacebookAdsSite(UniversalBaseModel):
    """
    Connected Site
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of this connected site.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the connected site
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for this connected site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
