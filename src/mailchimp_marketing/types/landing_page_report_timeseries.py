# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .landing_page_report_timeseries_daily_stats import LandingPageReportTimeseriesDailyStats
from .landing_page_report_timeseries_weekly_stats import LandingPageReportTimeseriesWeeklyStats


class LandingPageReportTimeseries(UniversalBaseModel):
    daily_stats: typing.Optional[LandingPageReportTimeseriesDailyStats] = pydantic.Field(default=None)
    """
    The clicks and visits data from the last seven days.
    """

    weekly_stats: typing.Optional[LandingPageReportTimeseriesWeeklyStats] = pydantic.Field(default=None)
    """
    The clicks and visits data from the last five weeks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
