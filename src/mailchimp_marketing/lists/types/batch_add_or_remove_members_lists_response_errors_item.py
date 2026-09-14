# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatchAddOrRemoveMembersListsResponseErrorsItem(UniversalBaseModel):
    email_addresses: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Email addresses added to the static segment or removed
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error message indicating why the email addresses could not be added or updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
