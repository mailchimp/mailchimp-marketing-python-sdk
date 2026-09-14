# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_ip_geo_unknown_field import SegmentTypeItemIpGeoUnknownField
from .segment_type_item_ip_geo_unknown_op import SegmentTypeItemIpGeoUnknownOp


class SegmentTypeItemIpGeoUnknown(UniversalBaseModel):
    """
    Segment members whose location information is unknown.
    """

    field: SegmentTypeItemIpGeoUnknownField = pydantic.Field()
    """
    Segmenting subscribers who are within a specific location.
    """

    op: SegmentTypeItemIpGeoUnknownOp = pydantic.Field()
    """
    Segment members for which location information is unknown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
