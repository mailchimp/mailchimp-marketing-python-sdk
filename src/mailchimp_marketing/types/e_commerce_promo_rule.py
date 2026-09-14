# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_commerce_promo_rule_links_item import ECommercePromoRuleLinksItem
from .e_commerce_promo_rule_target import ECommercePromoRuleTarget
from .e_commerce_promo_rule_type import ECommercePromoRuleType


class ECommercePromoRule(UniversalBaseModel):
    """
    Information about an Ecommerce Store's specific Promo Rule
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ECommercePromoRuleLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the promo code discount. If 'type' is 'fixed', the amount is treated as a monetary value. If 'type' is 'percentage', amount must be a decimal value between 0.0 and 1.0, inclusive.
    """

    created_at_foreign: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the promotion was created in ISO 8601 format.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of a promotion restricted to UTF-8 characters with max length 255.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the promo rule is currently enabled.
    """

    ends_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date and time when the promotion ends. Must be after starts_at and in ISO 8601 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.
    """

    starts_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the promotion is in effect in ISO 8601 format.
    """

    target: typing.Optional[ECommercePromoRuleTarget] = pydantic.Field(default=None)
    """
    The target that the discount applies to.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.
    """

    type: typing.Optional[ECommercePromoRuleType] = pydantic.Field(default=None)
    """
    Type of discount. For free shipping set type to fixed.
    """

    updated_at_foreign: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the promotion was updated in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
