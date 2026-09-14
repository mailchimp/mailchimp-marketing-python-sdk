# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_commerce_product_images_item_links_item import ECommerceProductImagesItemLinksItem


class ECommerceProductImagesItem(UniversalBaseModel):
    """
    Information about a specific product image.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ECommerceProductImagesItemLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the product image.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for a product image.
    """

    variant_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
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
