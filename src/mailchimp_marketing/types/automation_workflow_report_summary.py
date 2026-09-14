# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AutomationWorkflowReportSummary(UniversalBaseModel):
    """
    A summary of opens and clicks for sent campaigns.
    """

    click_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of unique clicks, divided by the total number of successful deliveries.
    """

    clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of clicks for an campaign.
    """

    open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of unique opens divided by the total number of successful deliveries.
    """

    opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of opens for a campaign.
    """

    subscriber_clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique clicks.
    """

    unique_opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique opens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
