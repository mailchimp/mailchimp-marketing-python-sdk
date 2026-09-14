# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_report_ab_split import CampaignReportAbSplit
from .campaign_report_bounces import CampaignReportBounces
from .campaign_report_clicks import CampaignReportClicks
from .campaign_report_delivery_status import CampaignReportDeliveryStatus
from .campaign_report_ecommerce import CampaignReportEcommerce
from .campaign_report_facebook_likes import CampaignReportFacebookLikes
from .campaign_report_forwards import CampaignReportForwards
from .campaign_report_industry_stats import CampaignReportIndustryStats
from .campaign_report_links_item import CampaignReportLinksItem
from .campaign_report_list_stats import CampaignReportListStats
from .campaign_report_opens import CampaignReportOpens
from .campaign_report_share_report import CampaignReportShareReport
from .campaign_report_timeseries_item import CampaignReportTimeseriesItem
from .campaign_report_timewarp_item import CampaignReportTimewarpItem


class CampaignReport(UniversalBaseModel):
    """
    Report details about a sent campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[CampaignReportLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    ab_split: typing.Optional[CampaignReportAbSplit] = pydantic.Field(default=None)
    """
    General stats about different groups of an A/B Split campaign. Does not return information about Multivariate Campaigns.
    """

    abuse_reports: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of abuse reports generated for this campaign.
    """

    bounces: typing.Optional[CampaignReportBounces] = pydantic.Field(default=None)
    """
    An object describing the bounce summary for the campaign.
    """

    campaign_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the campaign.
    """

    clicks: typing.Optional[CampaignReportClicks] = pydantic.Field(default=None)
    """
    An object describing the click activity for the campaign.
    """

    delivery_status: typing.Optional[CampaignReportDeliveryStatus] = pydantic.Field(default=None)
    """
    Updates on campaigns in the process of sending.
    """

    ecommerce: typing.Optional[CampaignReportEcommerce] = pydantic.Field(default=None)
    """
    E-Commerce stats for a campaign.
    """

    emails_sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of emails sent for this campaign.
    """

    facebook_likes: typing.Optional[CampaignReportFacebookLikes] = pydantic.Field(default=None)
    """
    An object describing campaign engagement on Facebook.
    """

    forwards: typing.Optional[CampaignReportForwards] = pydantic.Field(default=None)
    """
    An object describing the forwards and forward activity for the campaign.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this campaign.
    """

    industry_stats: typing.Optional[CampaignReportIndustryStats] = pydantic.Field(default=None)
    """
    The average campaign statistics for your industry.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique list id.
    """

    list_is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the list used, namely if it's deleted or disabled.
    """

    list_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the list.
    """

    list_stats: typing.Optional[CampaignReportListStats] = pydantic.Field(default=None)
    """
    The average campaign statistics for your list. This won't be present if we haven't calculated it yet for this list.
    """

    opens: typing.Optional[CampaignReportOpens] = pydantic.Field(default=None)
    """
    An object describing the open activity for the campaign.
    """

    preview_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preview text for the campaign.
    """

    rss_last_send: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    For RSS campaigns, the date and time of the last send in ISO 8601 format.
    """

    send_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time a campaign was sent in ISO 8601 format.
    """

    share_report: typing.Optional[CampaignReportShareReport] = pydantic.Field(default=None)
    """
    The url and password for the [VIP report](https://mailchimp.com/help/share-a-campaign-report/).
    """

    subject_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subject line for the campaign.
    """

    timeseries: typing.Optional[typing.List[CampaignReportTimeseriesItem]] = pydantic.Field(default=None)
    """
    An hourly breakdown of the performance of the campaign over the first 24 hours.
    """

    timewarp: typing.Optional[typing.List[CampaignReportTimewarpItem]] = pydantic.Field(default=None)
    """
    An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto).
    """

    unsubscribed: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of unsubscribed members for this campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
