# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListMemberActivityListsResponseActivityItem(UniversalBaseModel):
    """
    Member activity events.
    """

    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of action recorded for the subscriber.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The web-based ID for the campaign.
    """

    parent_campaign: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the parent campaign.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time recorded for the action.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    If set, the campaign's title.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of campaign that was sent.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    For clicks, the URL the subscriber clicked on.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
