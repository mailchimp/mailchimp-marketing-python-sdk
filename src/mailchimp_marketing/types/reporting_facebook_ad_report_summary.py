# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reporting_facebook_ad_report_summary_average_daily_budget import (
    ReportingFacebookAdReportSummaryAverageDailyBudget,
)
from .reporting_facebook_ad_report_summary_average_order_amount import (
    ReportingFacebookAdReportSummaryAverageOrderAmount,
)
from .reporting_facebook_ad_report_summary_cost_per_click import ReportingFacebookAdReportSummaryCostPerClick
from .reporting_facebook_ad_report_summary_ecommerce import ReportingFacebookAdReportSummaryEcommerce
from .reporting_facebook_ad_report_summary_extended_at import ReportingFacebookAdReportSummaryExtendedAt


class ReportingFacebookAdReportSummary(UniversalBaseModel):
    """
    Report summary of facebook ad
    """

    average_daily_budget: typing.Optional[ReportingFacebookAdReportSummaryAverageDailyBudget] = None
    average_order_amount: typing.Optional[ReportingFacebookAdReportSummaryAverageOrderAmount] = None
    click_rate: typing.Optional[float] = None
    clicks: typing.Optional[int] = None
    comments: typing.Optional[int] = None
    cost_per_click: typing.Optional[ReportingFacebookAdReportSummaryCostPerClick] = None
    ecommerce: typing.Optional[ReportingFacebookAdReportSummaryEcommerce] = None
    extended_at: typing.Optional[ReportingFacebookAdReportSummaryExtendedAt] = None
    first_time_buyers: typing.Optional[int] = None
    has_extended_ad_duration: typing.Optional[bool] = None
    impressions: typing.Optional[int] = None
    likes: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    return_on_investment: typing.Optional[float] = None
    shares: typing.Optional[int] = None
    total_orders: typing.Optional[int] = None
    total_products_sold: typing.Optional[int] = None
    unique_clicks: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
