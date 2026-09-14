# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacebookAdsAudienceTargetingSpecsLocations(UniversalBaseModel):
    cities: typing.Optional[typing.List[str]] = None
    countries: typing.Optional[typing.List[str]] = None
    regions: typing.Optional[typing.List[str]] = None
    zips: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
