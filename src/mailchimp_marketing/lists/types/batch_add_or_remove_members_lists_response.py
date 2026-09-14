# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.lists_post import ListsPost
from .batch_add_or_remove_members_lists_response_errors_item import BatchAddOrRemoveMembersListsResponseErrorsItem
from .batch_add_or_remove_members_lists_response_links_item import BatchAddOrRemoveMembersListsResponseLinksItem


class BatchAddOrRemoveMembersListsResponse(UniversalBaseModel):
    """
    Batch add/remove List members to/from static segment
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[BatchAddOrRemoveMembersListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    error_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query, irrespective of pagination.
    """

    errors: typing.Optional[typing.List[BatchAddOrRemoveMembersListsResponseErrorsItem]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an array of email addresses that could not be added to the segment or removed and an error message providing more details.
    """

    members_added: typing.Optional[typing.List[ListsPost]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a new member that was added to the static segment.
    """

    members_removed: typing.Optional[typing.List[ListsPost]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an existing list member that got deleted from the static segment.
    """

    total_added: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query, irrespective of pagination.
    """

    total_removed: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query, irrespective of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
