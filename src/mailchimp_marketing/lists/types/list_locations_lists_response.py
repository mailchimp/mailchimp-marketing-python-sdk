# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_locations_lists_response_links_item import ListLocationsListsResponseLinksItem
from .list_locations_lists_response_locations_item import ListLocationsListsResponseLocationsItem


class ListLocationsListsResponse(UniversalBaseModel):
    """
    A summary of List's locations.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListLocationsListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the list.
    """

    locations: typing.Optional[typing.List[ListLocationsListsResponseLocationsItem]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a list's top subscriber locations.
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
