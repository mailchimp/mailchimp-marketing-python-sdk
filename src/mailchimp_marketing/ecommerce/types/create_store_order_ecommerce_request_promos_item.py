# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_store_order_ecommerce_request_promos_item_amount_discounted import (
    CreateStoreOrderEcommerceRequestPromosItemAmountDiscounted,
)
from .create_store_order_ecommerce_request_promos_item_type import CreateStoreOrderEcommerceRequestPromosItemType


class CreateStoreOrderEcommerceRequestPromosItem(UniversalBaseModel):
    amount_discounted: CreateStoreOrderEcommerceRequestPromosItemAmountDiscounted
    code: str = pydantic.Field()
    """
    The Promo Code
    """

    type: CreateStoreOrderEcommerceRequestPromosItemType = pydantic.Field()
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
