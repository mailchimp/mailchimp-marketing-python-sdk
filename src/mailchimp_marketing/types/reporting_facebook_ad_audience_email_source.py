# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReportingFacebookAdAudienceEmailSource(UniversalBaseModel):
    is_segment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the source reference a segment
    """

    list_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Associated list name to the source
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email source name
    """

    segment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Segment type if this source is tied to a segment
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the email source
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
