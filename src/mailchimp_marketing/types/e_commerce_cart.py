# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_commerce_cart_line_item import ECommerceCartLineItem
from .e_commerce_cart_links_item import ECommerceCartLinksItem
from .e_commerce_customer import ECommerceCustomer


class ECommerceCart(UniversalBaseModel):
    """
    Information about a specific cart.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ECommerceCartLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies the campaign associated with a cart.
    """

    checkout_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the cart was created in ISO 8601 format.
    """

    currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The three-letter ISO 4217 code for the currency that the cart uses.
    """

    customer: typing.Optional[ECommerceCustomer] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the cart.
    """

    lines: typing.Optional[typing.List[ECommerceCartLineItem]] = pydantic.Field(default=None)
    """
    An array of the cart's line items.
    """

    order_total: typing.Optional[float] = pydantic.Field(default=None)
    """
    The order total for the cart.
    """

    tax_total: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total tax for the cart.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the cart was last updated in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
