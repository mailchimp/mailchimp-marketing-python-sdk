# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_store_order_ecommerce_request_promos_item_amount_discounted import (
    UpdateStoreOrderEcommerceRequestPromosItemAmountDiscounted,
)
from .update_store_order_ecommerce_request_promos_item_type import UpdateStoreOrderEcommerceRequestPromosItemType


class UpdateStoreOrderEcommerceRequestPromosItem(UniversalBaseModel):
    amount_discounted: UpdateStoreOrderEcommerceRequestPromosItemAmountDiscounted
    code: str = pydantic.Field()
    """
    The Promo Code
    """

    type: UpdateStoreOrderEcommerceRequestPromosItemType = pydantic.Field()
    """
    Type of discount. For free shipping set type to fixed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
