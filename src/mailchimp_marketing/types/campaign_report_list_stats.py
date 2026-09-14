# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignReportListStats(UniversalBaseModel):
    """
    The average campaign statistics for your list. This won't be present if we haven't calculated it yet for this list.
    """

    click_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average click rate (a percentage represented as a number between 0 and 100) per campaign for the list.
    """

    open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average unique open rate (a percentage represented as a number between 0 and 100) per campaign for the list.
    """

    proxy_excluded_open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average unique open rate (a percentage represented as a number between 0 and 100) per campaign for the list, excluding opens from email clients that use proxies.
    """

    sub_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average number of subscriptions per month for the list.
    """

    unsub_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average number of unsubscriptions per month for the list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
