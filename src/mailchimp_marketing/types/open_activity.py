# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .open_activity_links_item import OpenActivityLinksItem
from .open_activity_merge_fields_value import OpenActivityMergeFieldsValue
from .open_activity_opens_item import OpenActivityOpensItem


class OpenActivity(UniversalBaseModel):
    """
    A list of a member's opens activity in a specific campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[OpenActivityLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the campaign.
    """

    contact_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the member, namely if they are subscribed, unsubscribed, deleted, non-subscribed, transactional, pending, or need reconfirmation.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for a subscriber.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the list.
    """

    list_is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the list used, namely if it's deleted or disabled.
    """

    merge_fields: typing.Optional[typing.Dict[str, OpenActivityMergeFieldsValue]] = pydantic.Field(default=None)
    """
    A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    """

    opens: typing.Optional[typing.List[OpenActivityOpensItem]] = pydantic.Field(default=None)
    """
    An array of timestamps for each time a list member opened the campaign. If a list member opens an email multiple times, this will return a separate timestamp for each open event.
    """

    opens_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of times the this campaign was opened by the list member.
    """

    proxy_excluded_opens_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of times the this campaign was opened by the list member excluding opens from email clients that use proxies .
    """

    vip: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
