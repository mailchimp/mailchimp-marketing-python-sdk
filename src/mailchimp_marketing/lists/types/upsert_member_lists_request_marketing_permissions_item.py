# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpsertMemberListsRequestMarketingPermissionsItem(UniversalBaseModel):
    """
    A single marketing permission a subscriber has either opted-in to or opted-out of.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the subscriber has opted-in to the marketing permission.
    """

    marketing_permission_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id for the marketing permission on the list
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
