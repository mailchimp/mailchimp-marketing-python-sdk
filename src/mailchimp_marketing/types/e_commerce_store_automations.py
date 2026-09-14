# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .e_commerce_store_automations_abandoned_browse import ECommerceStoreAutomationsAbandonedBrowse
from .e_commerce_store_automations_abandoned_cart import ECommerceStoreAutomationsAbandonedCart


class ECommerceStoreAutomations(UniversalBaseModel):
    """
    Details for the automations attached to this store.
    """

    abandoned_browse: typing.Optional[ECommerceStoreAutomationsAbandonedBrowse] = pydantic.Field(default=None)
    """
    abandonedBrowse automation details. abandonedBrowse is also known as Product Retargeting Email or Retarget Site Visitors on the web.
    """

    abandoned_cart: typing.Optional[ECommerceStoreAutomationsAbandonedCart] = pydantic.Field(default=None)
    """
    abandonedCart automation details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
