# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubscriberListContact(UniversalBaseModel):
    """
    [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.
    """

    address1: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street address for the list contact.
    """

    address2: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street address for the list contact.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city for the list contact.
    """

    company: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company name for the list.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    A two-character ISO3166 country code. Defaults to US if invalid.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number for the list contact.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state for the list contact.
    """

    zip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal or zip code for the list contact.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
