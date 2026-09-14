# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .facebook_ad import FacebookAd
from .facebook_ads_audience import FacebookAdsAudience
from .facebook_ads_budget import FacebookAdsBudget
from .facebook_ads_channel import FacebookAdsChannel
from .facebook_ads_content import FacebookAdsContent
from .facebook_ads_feedback import FacebookAdsFeedback
from .facebook_ads_links_item import FacebookAdsLinksItem
from .facebook_ads_site import FacebookAdsSite


class FacebookAds(FacebookAd):
    email_source_name: typing.Optional[str] = None
    end_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the ad was ended in ISO 8601 format.
    """

    needs_attention: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the ad has a problem and needs attention.
    """

    paused_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the ad was paused in ISO 8601 format.
    """

    thumbnail: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the thumbnail for this outreach.
    """

    was_canceled_by_facebook: typing.Optional[bool] = None
    audience: typing.Optional[FacebookAdsAudience] = pydantic.Field(default=None)
    """
    Audience settings
    """

    budget: typing.Optional[FacebookAdsBudget] = None
    channel: typing.Optional[FacebookAdsChannel] = pydantic.Field(default=None)
    """
    Channel settings
    """

    content: typing.Optional[FacebookAdsContent] = None
    feedback: typing.Optional[FacebookAdsFeedback] = pydantic.Field(default=None)
    """
    Check if this ad is connected to a facebook page
    """

    has_audience: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Check if this ad has audience setup
    """

    has_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Check if this ad has content
    """

    is_connected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Check if this ad is connected to a facebook page
    """

    site: typing.Optional[FacebookAdsSite] = pydantic.Field(default=None)
    """
    Connected Site
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[FacebookAdsLinksItem]],
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
