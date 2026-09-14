# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.e_commerce_order import ECommerceOrder
from .list_store_orders_ecommerce_response_links_item import ListStoreOrdersEcommerceResponseLinksItem


class ListStoreOrdersEcommerceResponse(UniversalBaseModel):
    """
    A collection of orders in a store.
    """

    store_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The store id.
    """

    orders: typing.Optional[typing.List[ECommerceOrder]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an order in a store.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListStoreOrdersEcommerceResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
