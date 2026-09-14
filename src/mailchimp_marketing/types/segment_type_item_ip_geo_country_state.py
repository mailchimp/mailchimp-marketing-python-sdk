# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_ip_geo_country_state_field import SegmentTypeItemIpGeoCountryStateField
from .segment_type_item_ip_geo_country_state_op import SegmentTypeItemIpGeoCountryStateOp


class SegmentTypeItemIpGeoCountryState(UniversalBaseModel):
    """
    Segment by a specific country or US state.
    """

    field: SegmentTypeItemIpGeoCountryStateField = pydantic.Field()
    """
    Segmenting subscribers who are within a specific location.
    """

    op: SegmentTypeItemIpGeoCountryStateOp = pydantic.Field()
    """
    Segment members who are within a specific country or US state.
    """

    value: str = pydantic.Field()
    """
    The two-letter country code or US state abbreviation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
