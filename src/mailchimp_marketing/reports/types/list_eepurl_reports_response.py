# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_eepurl_reports_response_clicks import ListEepurlReportsResponseClicks
from .list_eepurl_reports_response_links_item import ListEepurlReportsResponseLinksItem
from .list_eepurl_reports_response_referrers_item import ListEepurlReportsResponseReferrersItem
from .list_eepurl_reports_response_twitter import ListEepurlReportsResponseTwitter


class ListEepurlReportsResponse(UniversalBaseModel):
    """
    A summary of social activity for the campaign, tracked by EepURL.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListEepurlReportsResponseLinksItem]],
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
    The unique id for the campaign.
    """

    clicks: typing.Optional[ListEepurlReportsResponseClicks] = pydantic.Field(default=None)
    """
    A summary of the click-throughs on the campaign's URL.
    """

    eepurl: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shortened link used for tracking.
    """

    referrers: typing.Optional[typing.List[ListEepurlReportsResponseReferrersItem]] = pydantic.Field(default=None)
    """
    A summary of the top referrers for the campaign.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    twitter: typing.Optional[ListEepurlReportsResponseTwitter] = pydantic.Field(default=None)
    """
    A summary of Twitter activity for a campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
