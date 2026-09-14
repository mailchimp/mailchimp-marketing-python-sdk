# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reporting_facebook_ad_audience_targeting_specs_interests_item import (
    ReportingFacebookAdAudienceTargetingSpecsInterestsItem,
)
from .reporting_facebook_ad_audience_targeting_specs_locations import ReportingFacebookAdAudienceTargetingSpecsLocations


class ReportingFacebookAdAudienceTargetingSpecs(UniversalBaseModel):
    gender: typing.Optional[int] = None
    interests: typing.Optional[typing.List[ReportingFacebookAdAudienceTargetingSpecsInterestsItem]] = None
    locations: typing.Optional[ReportingFacebookAdAudienceTargetingSpecsLocations] = None
    max_age: typing.Optional[int] = None
    min_age: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
