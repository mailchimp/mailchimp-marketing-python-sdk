# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_clients_lists_response_clients_item import ListClientsListsResponseClientsItem
from .list_clients_lists_response_links_item import ListClientsListsResponseLinksItem


class ListClientsListsResponse(UniversalBaseModel):
    """
    The top email clients based on user-agent strings.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListClientsListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    clients: typing.Optional[typing.List[ListClientsListsResponseClientsItem]] = pydantic.Field(default=None)
    """
    An array of top email clients.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id.
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
