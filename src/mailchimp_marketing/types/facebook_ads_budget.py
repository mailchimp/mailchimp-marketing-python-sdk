# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacebookAdsBudget(UniversalBaseModel):
    currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency code
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Duration of the ad in seconds
    """

    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total budget of the ad
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
