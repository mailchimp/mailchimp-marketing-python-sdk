# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .click_detail_report_ab_split import ClickDetailReportAbSplit
from .click_detail_report_links_item import ClickDetailReportLinksItem


class ClickDetailReport(UniversalBaseModel):
    """
    A report of links clicked in a specific campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ClickDetailReportLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    ab_split: typing.Optional[ClickDetailReportAbSplit] = pydantic.Field(default=None)
    """
    A breakdown of clicks by different groups of an A/B Split campaign. Does not return information about Multivariate Campaigns.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The campaign id.
    """

    click_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total clicks a link generated for a campaign.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the link.
    """

    last_click: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time for the last recorded click for a link in ISO 8601 format.
    """

    total_clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of total clicks for a link.
    """

    unique_click_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of unique clicks a link generated for a campaign.
    """

    unique_clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of unique clicks for a link.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the link in the campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
