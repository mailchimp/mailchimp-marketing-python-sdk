# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_campaigns_request_rss_opts_schedule_daily_send import CreateCampaignsRequestRssOptsScheduleDailySend
from .create_campaigns_request_rss_opts_schedule_weekly_send_day import (
    CreateCampaignsRequestRssOptsScheduleWeeklySendDay,
)


class CreateCampaignsRequestRssOptsSchedule(UniversalBaseModel):
    """
    The schedule for sending the RSS Campaign.
    """

    daily_send: typing.Optional[CreateCampaignsRequestRssOptsScheduleDailySend] = pydantic.Field(default=None)
    """
    The days of the week to send a daily RSS Campaign.
    """

    hour: typing.Optional[int] = pydantic.Field(default=None)
    """
    The hour to send the campaign in local time. Acceptable hours are 0-23. For example, '4' would be 4am in [your account's default time zone](https://mailchimp.com/help/set-account-details/).
    """

    monthly_send_date: typing.Optional[float] = pydantic.Field(default=None)
    """
    The day of the month to send a monthly RSS Campaign. Acceptable days are 0-31, where '0' is always the last day of a month. Months with fewer than the selected number of days will not have an RSS campaign sent out that day. For example, RSS Campaigns set to send on the 30th will not go out in February.
    """

    weekly_send_day: typing.Optional[CreateCampaignsRequestRssOptsScheduleWeeklySendDay] = pydantic.Field(default=None)
    """
    The day of the week to send a weekly RSS Campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
