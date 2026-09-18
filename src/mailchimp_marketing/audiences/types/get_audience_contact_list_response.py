# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.audiences_contact import AudiencesContact
from .get_audience_contact_list_response_links_item import GetAudienceContactListResponseLinksItem


class GetAudienceContactListResponse(UniversalBaseModel):
    """
    An array of objects, each representing a contact record.
    """

    contacts: typing.Optional[typing.List[AudiencesContact]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a contact record.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A cursor pointing to the last item on this page of the collection. Paginate through a collection of records by setting the `cursor` parameter on a subsequent request to this value.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[GetAudienceContactListResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
