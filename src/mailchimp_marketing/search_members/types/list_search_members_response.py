# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_search_members_response_exact_matches import ListSearchMembersResponseExactMatches
from .list_search_members_response_full_search import ListSearchMembersResponseFullSearch
from .list_search_members_response_links_item import ListSearchMembersResponseLinksItem


class ListSearchMembersResponse(UniversalBaseModel):
    """
    Members found for given search term
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSearchMembersResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    exact_matches: typing.Optional[ListSearchMembersResponseExactMatches] = pydantic.Field(default=None)
    """
    Exact matches of the provided search query.
    """

    full_search: typing.Optional[ListSearchMembersResponseFullSearch] = pydantic.Field(default=None)
    """
    Partial matches of the provided search query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
