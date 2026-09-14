# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_activity_lists_response_activity_item_links_item import ListActivityListsResponseActivityItemLinksItem


class ListActivityListsResponseActivityItem(UniversalBaseModel):
    """
    One day's worth of list activity. Doesn't include Automation activity.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListActivityListsResponseActivityItemLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    day: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date for the activity summary.
    """

    emails_sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of emails sent on the date for the activity summary.
    """

    hard_bounce: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of hard bounces.
    """

    other_adds: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribers who may have been added outside of the [double opt-in process](https://mailchimp.com/help/about-double-opt-in/), such as imports or API activity.
    """

    other_removes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribers who may have been removed outside of unsubscribing or reporting an email as spam (for example, deleted subscribers).
    """

    recipient_clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of clicks.
    """

    soft_bounce: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of soft bounces
    """

    subs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribes.
    """

    unique_opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique opens.
    """

    unsubs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unsubscribes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
