# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .landing_page_report_timeseries_weekly_stats_clicks_item import LandingPageReportTimeseriesWeeklyStatsClicksItem
from .landing_page_report_timeseries_weekly_stats_unique_visits_item import (
    LandingPageReportTimeseriesWeeklyStatsUniqueVisitsItem,
)
from .landing_page_report_timeseries_weekly_stats_visits_item import LandingPageReportTimeseriesWeeklyStatsVisitsItem


class LandingPageReportTimeseriesWeeklyStats(UniversalBaseModel):
    """
    The clicks and visits data from the last five weeks.
    """

    clicks: typing.Optional[typing.List[LandingPageReportTimeseriesWeeklyStatsClicksItem]] = pydantic.Field(
        default=None
    )
    """
    The total number of clicks in a week.
    """

    unique_visits: typing.Optional[typing.List[LandingPageReportTimeseriesWeeklyStatsUniqueVisitsItem]] = None
    visits: typing.Optional[typing.List[LandingPageReportTimeseriesWeeklyStatsVisitsItem]] = pydantic.Field(
        default=None
    )
    """
    The total number of visits in a week.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
