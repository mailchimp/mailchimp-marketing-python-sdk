# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_ip_geo_in_zip_field import SegmentTypeItemIpGeoInZipField
from .segment_type_item_ip_geo_in_zip_op import SegmentTypeItemIpGeoInZipOp


class SegmentTypeItemIpGeoInZip(UniversalBaseModel):
    """
    Segment by a specific US ZIP code.
    """

    extra: int = pydantic.Field()
    """
    The zip code to segment against.
    """

    field: SegmentTypeItemIpGeoInZipField = pydantic.Field()
    """
    Segmenting subscribers who are within a specific location.
    """

    op: SegmentTypeItemIpGeoInZipOp = pydantic.Field()
    """
    Segment members who are within a specific US zip code.
    """

    value: int = pydantic.Field()
    """
    The radius of the target location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
