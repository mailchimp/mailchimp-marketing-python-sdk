# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_chimp_chatter_activity_feed_response_chimp_chatter_item_type import (
    ListChimpChatterActivityFeedResponseChimpChatterItemType,
)


class ListChimpChatterActivityFeedResponseChimpChatterItem(UniversalBaseModel):
    """
    A Chimp Chatter message
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If it exists, campaign ID for the associated campaign
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If it exists, list ID for the associated list
    """

    message: typing.Optional[str] = None
    title: typing.Optional[str] = None
    type: typing.Optional[ListChimpChatterActivityFeedResponseChimpChatterItemType] = pydantic.Field(default=None)
    """
    The type of activity
    """

    update_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time this activity was updated.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to a report that includes this activity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
