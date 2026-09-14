# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_campaigns_request_rss_opts_frequency import CreateCampaignsRequestRssOptsFrequency
from .create_campaigns_request_rss_opts_schedule import CreateCampaignsRequestRssOptsSchedule


class CreateCampaignsRequestRssOpts(UniversalBaseModel):
    """
    [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options, specific to an RSS campaign.
    """

    constrain_rss_img: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to add CSS to images in the RSS feed to constrain their width in campaigns.
    """

    feed_url: str = pydantic.Field()
    """
    The URL for the RSS feed.
    """

    frequency: CreateCampaignsRequestRssOptsFrequency = pydantic.Field()
    """
    The frequency of the RSS Campaign.
    """

    schedule: typing.Optional[CreateCampaignsRequestRssOptsSchedule] = pydantic.Field(default=None)
    """
    The schedule for sending the RSS Campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
