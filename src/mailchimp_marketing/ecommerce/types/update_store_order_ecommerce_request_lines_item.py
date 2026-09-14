# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_store_order_ecommerce_request_lines_item_discount import UpdateStoreOrderEcommerceRequestLinesItemDiscount
from .update_store_order_ecommerce_request_lines_item_price import UpdateStoreOrderEcommerceRequestLinesItemPrice


class UpdateStoreOrderEcommerceRequestLinesItem(UniversalBaseModel):
    """
    Information about a specific order line.
    """

    discount: typing.Optional[UpdateStoreOrderEcommerceRequestLinesItemDiscount] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the order line item.
    """

    price: typing.Optional[UpdateStoreOrderEcommerceRequestLinesItemPrice] = None
    product_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the product associated with the order line item.
    """

    product_variant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the product variant associated with the order line item.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The quantity of an order line item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
