# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_authorized_apps_response_apps_item import ListAuthorizedAppsResponseAppsItem
from .list_authorized_apps_response_links_item import ListAuthorizedAppsResponseLinksItem


class ListAuthorizedAppsResponse(UniversalBaseModel):
    """
    An array of objects, each representing an authorized application.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListAuthorizedAppsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    apps: typing.Optional[typing.List[ListAuthorizedAppsResponseAppsItem]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an authorized application.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
