# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upsert_store_product_ecommerce_request_images_item_variant_ids_item import (
    UpsertStoreProductEcommerceRequestImagesItemVariantIdsItem,
)


class UpsertStoreProductEcommerceRequestImagesItem(UniversalBaseModel):
    """
    Information about a specific product image.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the product image.
    """

    url: str = pydantic.Field()
    """
    The URL for a product image.
    """

    variant_ids: typing.Optional[typing.List[UpsertStoreProductEcommerceRequestImagesItemVariantIdsItem]] = (
        pydantic.Field(default=None)
    )
    """
    The list of product variants using the image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
