# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.open_activity import OpenActivity
from .list_open_details_reports_response_links_item import ListOpenDetailsReportsResponseLinksItem


class ListOpenDetailsReportsResponse(UniversalBaseModel):
    """
    A detailed report of any campaign emails that were opened by a list member.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListOpenDetailsReportsResponseLinksItem]],
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

    members: typing.Optional[typing.List[OpenActivity]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a list member who opened a campaign email. Each members object will contain information about the number of total opens by a single member, as well as timestamps for each open event.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    total_opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of opens matching the query regardless of pagination.
    """

    total_proxy_excluded_opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of opens excluding opens from email clients that use proxies regardless of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
