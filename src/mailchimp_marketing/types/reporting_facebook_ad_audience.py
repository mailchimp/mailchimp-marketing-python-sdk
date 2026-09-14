# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reporting_facebook_ad_audience_email_source import ReportingFacebookAdAudienceEmailSource
from .reporting_facebook_ad_audience_source_type import ReportingFacebookAdAudienceSourceType
from .reporting_facebook_ad_audience_targeting_specs import ReportingFacebookAdAudienceTargetingSpecs
from .reporting_facebook_ad_audience_type import ReportingFacebookAdAudienceType


class ReportingFacebookAdAudience(UniversalBaseModel):
    """
    Audience settings
    """

    email_source: typing.Optional[ReportingFacebookAdAudienceEmailSource] = None
    include_source_in_target: typing.Optional[bool] = pydantic.Field(default=None)
    """
    To include list contacts as part of audience
    """

    lookalike_country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    To find similar audience in given country
    """

    source_type: typing.Optional[ReportingFacebookAdAudienceSourceType] = pydantic.Field(default=None)
    """
    List or Facebook based audience
    """

    targeting_specs: typing.Optional[ReportingFacebookAdAudienceTargetingSpecs] = None
    type: typing.Optional[ReportingFacebookAdAudienceType] = pydantic.Field(default=None)
    """
    Type of the audience
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
