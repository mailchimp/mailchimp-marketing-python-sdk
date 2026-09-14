# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListRootResponseIndustryStats(UniversalBaseModel):
    """
    The [average campaign statistics](https://mailchimp.com/resources/research/email-marketing-benchmarks/?utm_source=mc-api&utm_medium=docs&utm_campaign=apidocs) for all campaigns in the account's specified industry.
    """

    bounce_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average bounce rate for all campaigns in the account's specified industry.
    """

    click_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average unique click rate for all campaigns in the account's specified industry.
    """

    open_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average unique open rate for all campaigns in the account's specified industry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
