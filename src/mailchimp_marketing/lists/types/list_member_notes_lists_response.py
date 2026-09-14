# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.member_notes import MemberNotes
from .list_member_notes_lists_response_links_item import ListMemberNotesListsResponseLinksItem


class ListMemberNotesListsResponse(UniversalBaseModel):
    """
    The last 10 notes for a specific list member, based on date created.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListMemberNotesListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id.
    """

    notes: typing.Optional[typing.List[MemberNotes]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a note resource.
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
