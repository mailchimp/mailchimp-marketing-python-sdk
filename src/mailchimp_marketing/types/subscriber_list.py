# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .subscriber_list_campaign_defaults import SubscriberListCampaignDefaults
from .subscriber_list_contact import SubscriberListContact
from .subscriber_list_links_item import SubscriberListLinksItem
from .subscriber_list_stats import SubscriberListStats
from .subscriber_list_visibility import SubscriberListVisibility


class SubscriberList(UniversalBaseModel):
    """
    Information about a specific list.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[SubscriberListLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    beamer_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list's [Email Beamer](https://mailchimp.com/help/use-email-beamer-to-create-a-campaign/) address.
    """

    campaign_defaults: typing.Optional[SubscriberListCampaignDefaults] = pydantic.Field(default=None)
    """
    [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.
    """

    contact: typing.Optional[SubscriberListContact] = pydantic.Field(default=None)
    """
    [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time that this list was created in ISO 8601 format.
    """

    double_optin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not to require the subscriber to confirm subscription via email.
    """

    email_type_option: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.
    """

    has_welcome: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this list has a welcome automation connected. Welcome Automations: welcomeSeries, singleWelcome, emailFollowup.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this list.
    """

    list_rating: typing.Optional[int] = pydantic.Field(default=None)
    """
    An auto-generated activity score for the list (0-5).
    """

    marketing_permissions: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the list has marketing permissions (eg. GDPR) enabled.
    """

    modules: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Any list-specific modules installed for this list.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the list.
    """

    notify_on_subscribe: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    """

    notify_on_unsubscribe: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    """

    permission_reminder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.
    """

    stats: typing.Optional[SubscriberListStats] = pydantic.Field(default=None)
    """
    Stats for the list. Many of these are cached for at least five minutes.
    """

    subscribe_url_long: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full version of this list's subscribe form (host will vary).
    """

    subscribe_url_short: typing.Optional[str] = pydantic.Field(default=None)
    """
    Our [url shortened](https://mailchimp.com/help/share-your-signup-form/) version of this list's subscribe form.
    """

    use_archive_bar: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.
    """

    visibility: typing.Optional[SubscriberListVisibility] = pydantic.Field(default=None)
    """
    Legacy - visibility settings are no longer used
    """

    web_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https://{dc}.admin.mailchimp.com/lists/members/?id={web_id}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
