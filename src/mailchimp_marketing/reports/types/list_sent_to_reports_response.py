# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.sent_to import SentTo
from .list_sent_to_reports_response_links_item import ListSentToReportsResponseLinksItem


class ListSentToReportsResponse(UniversalBaseModel):
    """
    A list of subscribers who were sent a specific campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSentToReportsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The campaign id.
    """

    sent_to: typing.Optional[typing.List[SentTo]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a campaign recipient.
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
