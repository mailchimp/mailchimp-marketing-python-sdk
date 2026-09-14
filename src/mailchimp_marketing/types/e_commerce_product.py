# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_commerce_product_images_item import ECommerceProductImagesItem
from .e_commerce_product_links_item import ECommerceProductLinksItem
from .e_commerce_product_variant import ECommerceProductVariant


class ECommerceProduct(UniversalBaseModel):
    """
    Information about a specific product.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ECommerceProductLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency code
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of a product.
    """

    handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The handle of a product.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the product.
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image URL for a product.
    """

    images: typing.Optional[typing.List[ECommerceProductImagesItem]] = pydantic.Field(default=None)
    """
    An array of the product's images.
    """

    published_at_foreign: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the product was published in ISO 8601 format.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of a product.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of product.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for a product.
    """

    variants: typing.Optional[typing.List[ECommerceProductVariant]] = pydantic.Field(default=None)
    """
    Returns up to 50 of the product's variants. To retrieve all variants use [Product Variants](https://mailchimp.com/developer/marketing/api/ecommerce-product-variants/).
    """

    vendor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The vendor for a product.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
