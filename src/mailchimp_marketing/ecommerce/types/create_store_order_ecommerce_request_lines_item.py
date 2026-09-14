# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ecommerce_stores_orders_post import EcommerceStoresOrdersPost
from .create_store_order_ecommerce_request_lines_item_discount import CreateStoreOrderEcommerceRequestLinesItemDiscount
from .create_store_order_ecommerce_request_lines_item_price import CreateStoreOrderEcommerceRequestLinesItemPrice


class CreateStoreOrderEcommerceRequestLinesItem(UniversalBaseModel):
    """
    Information about a specific order line.
    """

    discount: typing.Optional[CreateStoreOrderEcommerceRequestLinesItemDiscount] = None
    id: str = pydantic.Field()
    """
    A unique identifier for the order line item.
    """

    price: CreateStoreOrderEcommerceRequestLinesItemPrice
    product: typing.Optional[EcommerceStoresOrdersPost] = None
    product_id: str = pydantic.Field()
    """
    A unique identifier for the product associated with the order line item.
    """

    product_variant_id: str = pydantic.Field()
    """
    A unique identifier for the product variant associated with the order line item.
    """

    quantity: int = pydantic.Field()
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
