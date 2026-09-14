# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_ecomm_store_field import SegmentTypeItemEcommStoreField
from .segment_type_item_ecomm_store_op import SegmentTypeItemEcommStoreOp


class SegmentTypeItemEcommStore(UniversalBaseModel):
    """
    Segment by purchases from a specific store.
    """

    field: typing.Optional[SegmentTypeItemEcommStoreField] = pydantic.Field(default=None)
    """
    Segment by purchases from a specific store.
    """

    op: typing.Optional[SegmentTypeItemEcommStoreOp] = pydantic.Field(default=None)
    """
    Members who have or have not purchased from a specific store.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The store id to segment against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
