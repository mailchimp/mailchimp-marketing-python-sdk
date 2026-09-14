# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignReportBounces(UniversalBaseModel):
    """
    An object describing the bounce summary for the campaign.
    """

    hard_bounces: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of hard bounced email addresses.
    """

    soft_bounces: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of soft bounced email addresses.
    """

    syntax_errors: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of addresses that were syntax-related bounces.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
