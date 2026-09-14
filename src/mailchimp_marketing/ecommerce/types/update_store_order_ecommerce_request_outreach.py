# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateStoreOrderEcommerceRequestOutreach(UniversalBaseModel):
    """
    The outreach associated with this order. For example, an email campaign or Facebook ad.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the outreach. Can be an email campaign ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
