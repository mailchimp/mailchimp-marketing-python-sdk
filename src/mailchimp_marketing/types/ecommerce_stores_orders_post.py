# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_stores_orders_post_id import EcommerceStoresOrdersPostId
from .ecommerce_stores_orders_post_images_item import EcommerceStoresOrdersPostImagesItem
from .ecommerce_stores_orders_post_variants_item import EcommerceStoresOrdersPostVariantsItem


class EcommerceStoresOrdersPost(UniversalBaseModel):
    """
    Information about a specific product.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of a product.
    """

    handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The handle of a product.
    """

    id: EcommerceStoresOrdersPostId = pydantic.Field()
    """
    A unique identifier for the product.
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image URL for a product.
    """

    images: typing.Optional[typing.List[EcommerceStoresOrdersPostImagesItem]] = pydantic.Field(default=None)
    """
    An array of the product's images.
    """

    published_at_foreign: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date and time the product was published.
    """

    title: str = pydantic.Field()
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

    variants: typing.List[EcommerceStoresOrdersPostVariantsItem] = pydantic.Field()
    """
    An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.
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
