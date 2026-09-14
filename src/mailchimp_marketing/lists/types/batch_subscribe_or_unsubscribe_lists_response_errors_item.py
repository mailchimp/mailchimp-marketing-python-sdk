# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_subscribe_or_unsubscribe_lists_response_errors_item_error_code import (
    BatchSubscribeOrUnsubscribeListsResponseErrorsItemErrorCode,
)


class BatchSubscribeOrUnsubscribeListsResponseErrorsItem(UniversalBaseModel):
    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address that could not be added or updated.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error message indicating why the email address could not be added or updated.
    """

    error_code: typing.Optional[BatchSubscribeOrUnsubscribeListsResponseErrorsItemErrorCode] = pydantic.Field(
        default=None
    )
    """
    A unique code that identifies this specifc error.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the error is field-related, information about which field is at issue.
    """

    field_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Message indicating how to resolve a field-related error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
