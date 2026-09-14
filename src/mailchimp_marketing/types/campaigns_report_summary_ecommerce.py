# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignsReportSummaryEcommerce(UniversalBaseModel):
    """
    E-Commerce stats for a campaign.
    """

    total_orders: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total orders for a campaign.
    """

    total_revenue: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total revenue for a campaign. Calculated as the sum of all order totals minus shipping and tax totals.
    """

    total_spent: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total spent for a campaign. Calculated as the sum of all order totals with no deductions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
