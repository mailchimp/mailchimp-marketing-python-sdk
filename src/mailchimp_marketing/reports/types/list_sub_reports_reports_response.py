# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.campaign_report import CampaignReport
from .list_sub_reports_reports_response_links_item import ListSubReportsReportsResponseLinksItem


class ListSubReportsReportsResponse(UniversalBaseModel):
    """
    A list of reports containing child campaigns for a specific campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSubReportsReportsResponseLinksItem]],
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
    Unique identifier of the parent campaign
    """

    reports: typing.Optional[typing.List[CampaignReport]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a report resource.
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
