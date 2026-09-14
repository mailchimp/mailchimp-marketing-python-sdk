# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_store_cart_ecommerce_request_lines_item_price import CreateStoreCartEcommerceRequestLinesItemPrice


class CreateStoreCartEcommerceRequestLinesItem(UniversalBaseModel):
    """
    Information about a specific cart line item.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the cart line item.
    """

    price: CreateStoreCartEcommerceRequestLinesItemPrice
    product_id: str = pydantic.Field()
    """
    A unique identifier for the product associated with the cart line item.
    """

    product_variant_id: str = pydantic.Field()
    """
    A unique identifier for the product variant associated with the cart line item.
    """

    quantity: int = pydantic.Field()
    """
    The quantity of a cart line item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
