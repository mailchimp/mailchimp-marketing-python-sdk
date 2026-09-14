# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectedSiteSiteScript(UniversalBaseModel):
    """
    The script used to connect your site with Mailchimp.
    """

    fragment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pre-built script that you can copy-and-paste into your site to integrate it with Mailchimp.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL used for any integrations that offer built-in support for connected sites.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
