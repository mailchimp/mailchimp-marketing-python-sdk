# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_ecomm_purchased_field import SegmentTypeItemEcommPurchasedField
from .segment_type_item_ecomm_purchased_op import SegmentTypeItemEcommPurchasedOp


class SegmentTypeItemEcommPurchased(UniversalBaseModel):
    """
    Segment by whether someone has purchased anything.
    """

    field: typing.Optional[SegmentTypeItemEcommPurchasedField] = pydantic.Field(default=None)
    """
    Segment by whether someone has purchased anything.
    """

    op: typing.Optional[SegmentTypeItemEcommPurchasedOp] = pydantic.Field(default=None)
    """
    Members who have have ('member') or have not ('notmember') purchased.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
