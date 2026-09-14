# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceStoresCartsPostAddress(UniversalBaseModel):
    """
    The customer's address.
    """

    address1: typing.Optional[str] = pydantic.Field(default=None)
    """
    The mailing address of the customer.
    """

    address2: typing.Optional[str] = pydantic.Field(default=None)
    """
    An additional field for the customer's mailing address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city the customer is located in.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's country.
    """

    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two-letter code for the customer's country.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's postal or zip code.
    """

    province: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer's state name or normalized province.
    """

    province_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two-letter code for the customer's province or state.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
