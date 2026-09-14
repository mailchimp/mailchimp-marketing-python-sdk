# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConversationLastMessage(UniversalBaseModel):
    """
    The most recent message in the conversation.
    """

    from_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    A label representing the email of the sender of this message.
    """

    from_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A label representing the sender of this message.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The plain-text content of the message.
    """

    read: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this message has been marked as read.
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subject of this message.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the message was either sent or received in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
