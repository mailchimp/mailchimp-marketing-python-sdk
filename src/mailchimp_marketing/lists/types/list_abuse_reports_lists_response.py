# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.lists_abuse_reports import ListsAbuseReports
from .list_abuse_reports_lists_response_links_item import ListAbuseReportsListsResponseLinksItem


class ListAbuseReportsListsResponse(UniversalBaseModel):
    """
    A collection of abuse complaints for a specific list. An abuse complaint occurs when your recipient clicks to 'report spam' in their email program.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListAbuseReportsListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    abuse_reports: typing.Optional[typing.List[ListsAbuseReports]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an abuse report resource.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id for the abuse report.
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
