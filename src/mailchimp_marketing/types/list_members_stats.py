# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_members_stats_ecommerce_data import ListMembersStatsEcommerceData


class ListMembersStats(UniversalBaseModel):
    """
    Open and click rates for this subscriber.
    """

    avg_click_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    A subscriber's average clickthrough rate.
    """

    avg_open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    A subscriber's average open rate.
    """

    ecommerce_data: typing.Optional[ListMembersStatsEcommerceData] = pydantic.Field(default=None)
    """
    Ecommerce stats for the list member if the list is attached to a store.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
