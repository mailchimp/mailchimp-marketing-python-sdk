# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .e_commerce_store_automations_abandoned_browse_status import ECommerceStoreAutomationsAbandonedBrowseStatus


class ECommerceStoreAutomationsAbandonedBrowse(UniversalBaseModel):
    """
    abandonedBrowse automation details. abandonedBrowse is also known as Product Retargeting Email or Retarget Site Visitors on the web.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of automation parent campaign.
    """

    is_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this store supports the abandonedBrowse automation.
    """

    status: typing.Optional[ECommerceStoreAutomationsAbandonedBrowseStatus] = pydantic.Field(default=None)
    """
    Status of the abandonedBrowse automation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
