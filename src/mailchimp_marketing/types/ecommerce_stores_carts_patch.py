# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_stores_carts_patch_address import EcommerceStoresCartsPatchAddress
from .ecommerce_stores_carts_patch_total_spent import EcommerceStoresCartsPatchTotalSpent


class EcommerceStoresCartsPatch(UniversalBaseModel):
    """
    Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the customer. Limited to 50 characters.
    """

    address: typing.Optional[EcommerceStoresCartsPatchAddress] = pydantic.Field(default=None)
    """
    The customer's address.
    """

    company: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's company.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's first name.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's last name.
    """

    opt_in_status: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).
    """

    total_spent: typing.Optional[EcommerceStoresCartsPatchTotalSpent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
