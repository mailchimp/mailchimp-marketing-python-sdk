# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .member_notes_links_item import MemberNotesLinksItem


class MemberNotes(UniversalBaseModel):
    """
    A specific note for a specific member.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[MemberNotesLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    As Mailchimp evolves beyond email, you may eventually have contacts without email addresses. While the `email_id` is the MD5 hash of their email address, this `contact_id` is agnostic of contact’s inclusion of an email address.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the note was created in ISO 8601 format.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The author of the note.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The note id.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the list.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the note.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the note was last updated in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
