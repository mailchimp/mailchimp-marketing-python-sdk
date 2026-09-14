# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_members_last_note import ListMembersLastNote
from .list_members_links_item import ListMembersLinksItem
from .list_members_location import ListMembersLocation
from .list_members_marketing_permissions_item import ListMembersMarketingPermissionsItem
from .list_members_merge_fields_value import ListMembersMergeFieldsValue
from .list_members_sms_subscription_status import ListMembersSmsSubscriptionStatus
from .list_members_stats import ListMembersStats
from .list_members_status import ListMembersStatus
from .list_members_tags_item import ListMembersTagsItem


class ListMembers(UniversalBaseModel):
    """
    Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListMembersLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    consents_to_one_to_one_messaging: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether a contact consents to 1:1 messaging.
    """

    contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    As Mailchimp evolves beyond email, you may eventually have contacts without email addresses. While the `id` is the MD5 hash of their email address, this `contact_id` is agnostic of contact’s inclusion of an email address.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for a subscriber.
    """

    email_client: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list member's email client.
    """

    email_type: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Type of email this member asked to get ('html' or 'text').
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    interests: typing.Optional[typing.Dict[str, bool]] = pydantic.Field(default=None)
    """
    The key of this object's properties is the ID of the interest in question.
    """

    ip_opt: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address the subscriber used to confirm their opt-in status.
    """

    ip_signup: typing.Optional[str] = pydantic.Field(default=None)
    """
    IP address the subscriber signed up from.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).
    """

    last_changed: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the member's info was last changed in ISO 8601 format.
    """

    last_note: typing.Optional[ListMembersLastNote] = pydantic.Field(default=None)
    """
    The most recent Note added about this member.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id.
    """

    location: typing.Optional[ListMembersLocation] = pydantic.Field(default=None)
    """
    Subscriber location information.
    """

    marketing_permissions: typing.Optional[typing.List[ListMembersMarketingPermissionsItem]] = pydantic.Field(
        default=None
    )
    """
    The marketing permissions for the subscriber.
    """

    member_rating: typing.Optional[int] = pydantic.Field(default=None)
    """
    Star rating for this member, between 1 and 5.
    """

    merge_fields: typing.Optional[typing.Dict[str, ListMembersMergeFieldsValue]] = pydantic.Field(default=None)
    """
    A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    """

    sms_phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A US phone number for SMS contact.
    """

    sms_subscription_last_updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The datetime when the SMS subscription was last updated
    """

    sms_subscription_status: typing.Optional[ListMembersSmsSubscriptionStatus] = pydantic.Field(default=None)
    """
    The status of an SMS subscription.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source from which the subscriber was added to this list.
    """

    stats: typing.Optional[ListMembersStats] = pydantic.Field(default=None)
    """
    Open and click rates for this subscriber.
    """

    status: typing.Optional[ListMembersStatus] = pydantic.Field(default=None)
    """
    Subscriber's current status.
    """

    tags: typing.Optional[typing.List[ListMembersTagsItem]] = pydantic.Field(default=None)
    """
    Returns up to 50 tags applied to this member. To retrieve all tags see [Member Tags](https://mailchimp.com/developer/marketing/api/list-member-tags/).
    """

    tags_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of tags applied to this member.
    """

    timestamp_opt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the subscriber confirmed their opt-in status in ISO 8601 format.
    """

    timestamp_signup: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the subscriber signed up for the list in ISO 8601 format.
    """

    unique_email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier for the address across all of Mailchimp.
    """

    unsubscribe_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A subscriber's reason for unsubscribing.
    """

    vip: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    """

    web_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID used in the Mailchimp web application. View this member in your Mailchimp account at `https://{dc}.admin.mailchimp.com/lists/members/view?id={web_id}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
