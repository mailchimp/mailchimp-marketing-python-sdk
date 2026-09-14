# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.lists_post import ListsPost
from .batch_subscribe_or_unsubscribe_lists_response_errors_item import (
    BatchSubscribeOrUnsubscribeListsResponseErrorsItem,
)
from .batch_subscribe_or_unsubscribe_lists_response_links_item import BatchSubscribeOrUnsubscribeListsResponseLinksItem


class BatchSubscribeOrUnsubscribeListsResponse(UniversalBaseModel):
    """
    Batch update list members.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[BatchSubscribeOrUnsubscribeListsResponseLinksItem]],
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

    errors: typing.Optional[typing.List[BatchSubscribeOrUnsubscribeListsResponseErrorsItem]] = pydantic.Field(
        default=None
    )
    """
    An array of objects, each representing an email address that could not be added to the list or updated and an error message providing more details.
    """

    new_members: typing.Optional[typing.List[ListsPost]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a new member that was added to the list.
    """

    total_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query, irrespective of pagination.
    """

    total_updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query, irrespective of pagination.
    """

    updated_members: typing.Optional[typing.List[ListsPost]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an existing list member whose subscription status was updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
