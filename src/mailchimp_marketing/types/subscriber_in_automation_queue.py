# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .subscriber_in_automation_queue_links_item_item import SubscriberInAutomationQueueLinksItemItem


class SubscriberInAutomationQueue(UniversalBaseModel):
    """
    Information about subscribers in an Automation email queue.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[SubscriberInAutomationQueueLinksItemItem]]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list member's email address.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies an email in an Automation workflow.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies a list.
    """

    list_is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the list used, namely if it's deleted or disabled.
    """

    next_send: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the next send for the workflow email in ISO 8601 format.
    """

    workflow_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies an Automation workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
