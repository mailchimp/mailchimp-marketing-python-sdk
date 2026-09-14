# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.campaign import Campaign
from ..types.campaign_content import CampaignContent
from ..types.campaign_content_links_item import CampaignContentLinksItem
from ..types.campaign_content_variate_contents_item import CampaignContentVariateContentsItem
from ..types.campaign_feedback import CampaignFeedback
from ..types.campaign_tracking_options import CampaignTrackingOptions
from ..types.campaigns import Campaigns
from .raw_client import AsyncRawCampaignsClient, RawCampaignsClient
from .types.create_action_create_resend_campaigns_request_shortcut_type import (
    CreateActionCreateResendCampaignsRequestShortcutType,
)
from .types.create_action_schedule_campaigns_request_batch_delivery import (
    CreateActionScheduleCampaignsRequestBatchDelivery,
)
from .types.create_action_test_campaigns_request_send_type import CreateActionTestCampaignsRequestSendType
from .types.create_campaigns_request_content_type import CreateCampaignsRequestContentType
from .types.create_campaigns_request_recipients import CreateCampaignsRequestRecipients
from .types.create_campaigns_request_rss_opts import CreateCampaignsRequestRssOpts
from .types.create_campaigns_request_settings import CreateCampaignsRequestSettings
from .types.create_campaigns_request_social_card import CreateCampaignsRequestSocialCard
from .types.create_campaigns_request_type import CreateCampaignsRequestType
from .types.create_campaigns_request_variate_settings import CreateCampaignsRequestVariateSettings
from .types.create_feedback_campaigns_response import CreateFeedbackCampaignsResponse
from .types.list_campaigns_request_sort_dir import ListCampaignsRequestSortDir
from .types.list_campaigns_request_sort_field import ListCampaignsRequestSortField
from .types.list_campaigns_request_status import ListCampaignsRequestStatus
from .types.list_campaigns_request_type import ListCampaignsRequestType
from .types.list_campaigns_response import ListCampaignsResponse
from .types.list_feedback_campaigns_response import ListFeedbackCampaignsResponse
from .types.list_send_checklist_campaigns_response import ListSendChecklistCampaignsResponse
from .types.update_campaigns_request_recipients import UpdateCampaignsRequestRecipients
from .types.update_campaigns_request_rss_opts import UpdateCampaignsRequestRssOpts
from .types.update_campaigns_request_settings import UpdateCampaignsRequestSettings
from .types.update_campaigns_request_social_card import UpdateCampaignsRequestSocialCard
from .types.update_campaigns_request_variate_settings import UpdateCampaignsRequestVariateSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CampaignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCampaignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCampaignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCampaignsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ListCampaignsRequestType] = None,
        status: typing.Optional[ListCampaignsRequestStatus] = None,
        before_send_time: typing.Optional[dt.datetime] = None,
        since_send_time: typing.Optional[dt.datetime] = None,
        before_create_time: typing.Optional[dt.datetime] = None,
        since_create_time: typing.Optional[dt.datetime] = None,
        list_id: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        member_id: typing.Optional[str] = None,
        sort_field: typing.Optional[ListCampaignsRequestSortField] = None,
        sort_dir: typing.Optional[ListCampaignsRequestSortDir] = None,
        include_resend_shortcut_eligibility: typing.Optional[bool] = None,
        include_resend_shortcut_usage: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Campaigns, ListCampaignsResponse]:
        """
        Get all campaigns in an account.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[ListCampaignsRequestType]
            The campaign type.

        status : typing.Optional[ListCampaignsRequestStatus]
            The status of the campaign.

        before_send_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_send_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_create_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_create_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        list_id : typing.Optional[str]
            The unique id for the list.

        folder_id : typing.Optional[str]
            The unique folder id.

        member_id : typing.Optional[str]
            Retrieve campaigns sent to a particular list member. Member ID is The MD5 hash of the lowercase version of the list member’s email address.

        sort_field : typing.Optional[ListCampaignsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListCampaignsRequestSortDir]
            Determines the order direction for sorted results.

        include_resend_shortcut_eligibility : typing.Optional[bool]
            Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.

        include_resend_shortcut_usage : typing.Optional[bool]
            Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Campaigns, ListCampaignsResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.campaigns.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            type=type,
            status=status,
            before_send_time=before_send_time,
            since_send_time=since_send_time,
            before_create_time=before_create_time,
            since_create_time=since_create_time,
            list_id=list_id,
            folder_id=folder_id,
            member_id=member_id,
            sort_field=sort_field,
            sort_dir=sort_dir,
            include_resend_shortcut_eligibility=include_resend_shortcut_eligibility,
            include_resend_shortcut_usage=include_resend_shortcut_usage,
            request_options=request_options,
        )

    def create(
        self,
        *,
        type: CreateCampaignsRequestType,
        content_type: typing.Optional[CreateCampaignsRequestContentType] = OMIT,
        recipients: typing.Optional[CreateCampaignsRequestRecipients] = OMIT,
        rss_opts: typing.Optional[CreateCampaignsRequestRssOpts] = OMIT,
        settings: typing.Optional[CreateCampaignsRequestSettings] = OMIT,
        social_card: typing.Optional[CreateCampaignsRequestSocialCard] = OMIT,
        tracking: typing.Optional[CampaignTrackingOptions] = OMIT,
        variate_settings: typing.Optional[CreateCampaignsRequestVariateSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Create a new Mailchimp campaign.

        Parameters
        ----------
        type : CreateCampaignsRequestType
            There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) you can create in Mailchimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.

        content_type : typing.Optional[CreateCampaignsRequestContentType]
            How the campaign's content is put together. The old drag and drop editor uses 'template' while the new editor uses 'multichannel'. Defaults to template.

        recipients : typing.Optional[CreateCampaignsRequestRecipients]
            List settings for the campaign.

        rss_opts : typing.Optional[CreateCampaignsRequestRssOpts]
            [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options, specific to an RSS campaign.

        settings : typing.Optional[CreateCampaignsRequestSettings]
            The settings for your campaign, including subject, from name, reply-to address, and more.

        social_card : typing.Optional[CreateCampaignsRequestSocialCard]
            The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).

        tracking : typing.Optional[CampaignTrackingOptions]

        variate_settings : typing.Optional[CreateCampaignsRequestVariateSettings]
            The settings specific to A/B test campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create(
            type="regular",
        )
        """
        _response = self._raw_client.create(
            type=type,
            content_type=content_type,
            recipients=recipients,
            rss_opts=rss_opts,
            settings=settings,
            social_card=social_card,
            tracking=tracking,
            variate_settings=variate_settings,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_resend_shortcut_eligibility: typing.Optional[bool] = None,
        include_resend_shortcut_usage: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Get information about a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_resend_shortcut_eligibility : typing.Optional[bool]
            Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.

        include_resend_shortcut_usage : typing.Optional[bool]
            Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.get(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.get(
            campaign_id,
            fields=fields,
            exclude_fields=exclude_fields,
            include_resend_shortcut_eligibility=include_resend_shortcut_eligibility,
            include_resend_shortcut_usage=include_resend_shortcut_usage,
            request_options=request_options,
        )
        return _response.data

    def delete(self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a campaign from your Mailchimp account.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.delete(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.delete(campaign_id, request_options=request_options)
        return _response.data

    def update(
        self,
        campaign_id: str,
        *,
        recipients: typing.Optional[UpdateCampaignsRequestRecipients] = OMIT,
        rss_opts: typing.Optional[UpdateCampaignsRequestRssOpts] = OMIT,
        settings: typing.Optional[UpdateCampaignsRequestSettings] = OMIT,
        social_card: typing.Optional[UpdateCampaignsRequestSocialCard] = OMIT,
        tracking: typing.Optional[CampaignTrackingOptions] = OMIT,
        variate_settings: typing.Optional[UpdateCampaignsRequestVariateSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Update some or all of the settings for a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        recipients : typing.Optional[UpdateCampaignsRequestRecipients]
            List settings for the campaign.

        rss_opts : typing.Optional[UpdateCampaignsRequestRssOpts]
            [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign.

        settings : typing.Optional[UpdateCampaignsRequestSettings]
            The settings for your campaign, including subject, from name, reply-to address, and more.

        social_card : typing.Optional[UpdateCampaignsRequestSocialCard]
            The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).

        tracking : typing.Optional[CampaignTrackingOptions]

        variate_settings : typing.Optional[UpdateCampaignsRequestVariateSettings]
            The settings specific to A/B test campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.update(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.update(
            campaign_id,
            recipients=recipients,
            rss_opts=rss_opts,
            settings=settings,
            social_card=social_card,
            tracking=tracking,
            variate_settings=variate_settings,
            request_options=request_options,
        )
        return _response.data

    def create_action_cancel_send(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancel a Regular or Plain-Text Campaign after you send, before all of your recipients receive it. This feature is included with Mailchimp Pro.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_cancel_send(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_cancel_send(campaign_id, request_options=request_options)
        return _response.data

    def create_action_create_resend(
        self,
        campaign_id: str,
        *,
        shortcut_type: typing.Optional[CreateActionCreateResendCampaignsRequestShortcutType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Remove the guesswork for resending a campaign to certain segments. You can use this endpoint as a shortcut to replicate a campaign and resend it to common segments, such as those who didn't open the campaign, or any new subscribers since it was sent.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        shortcut_type : typing.Optional[CreateActionCreateResendCampaignsRequestShortcutType]
            Which campaign resend shortcut to use. Default is `to_non_openers`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_create_resend(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_create_resend(
            campaign_id, shortcut_type=shortcut_type, request_options=request_options
        )
        return _response.data

    def create_action_pause(self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Pause an RSS-Driven campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_pause(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_pause(campaign_id, request_options=request_options)
        return _response.data

    def create_action_replicate(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Campaign:
        """
        Replicate a campaign in saved or send status.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_replicate(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_replicate(campaign_id, request_options=request_options)
        return _response.data

    def create_action_resume(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Resume an RSS-Driven campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_resume(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_resume(campaign_id, request_options=request_options)
        return _response.data

    def create_action_schedule(
        self,
        campaign_id: str,
        *,
        schedule_time: dt.datetime,
        batch_delivery: typing.Optional[CreateActionScheduleCampaignsRequestBatchDelivery] = OMIT,
        timewarp: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Schedule a campaign for delivery. If you're using Multivariate Campaigns to test send times or sending RSS Campaigns, use the send action instead.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        schedule_time : dt.datetime
            The UTC date and time to schedule the campaign for delivery in ISO 8601 format. Campaigns may only be scheduled to send on the quarter-hour (:00, :15, :30, :45).

        batch_delivery : typing.Optional[CreateActionScheduleCampaignsRequestBatchDelivery]
            Choose whether the campaign should use [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/). Cannot be set to `true` for campaigns using [Timewarp](https://mailchimp.com/help/use-timewarp/).

        timewarp : typing.Optional[bool]
            Choose whether the campaign should use [Timewarp](https://mailchimp.com/help/use-timewarp/) when sending. Campaigns scheduled with Timewarp are localized based on the recipients' time zones. For example, a Timewarp campaign with a `schedule_time` of 13:00 will be sent to each recipient at 1:00pm in their local time. Cannot be set to `true` for campaigns using [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_schedule(
            campaign_id="campaign_id",
            schedule_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_action_schedule(
            campaign_id,
            schedule_time=schedule_time,
            batch_delivery=batch_delivery,
            timewarp=timewarp,
            request_options=request_options,
        )
        return _response.data

    def create_action_send(self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Send a Mailchimp campaign. For RSS Campaigns, the campaign will send according to its schedule. All other campaigns will send immediately.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_send(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_send(campaign_id, request_options=request_options)
        return _response.data

    def create_action_test(
        self,
        campaign_id: str,
        *,
        send_type: CreateActionTestCampaignsRequestSendType,
        test_emails: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a test email.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        send_type : CreateActionTestCampaignsRequestSendType
            Choose the type of test email to send.

        test_emails : typing.Sequence[str]
            An array of email addresses to send the test email to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_test(
            campaign_id="campaign_id",
            send_type="html",
            test_emails=["test_emails"],
        )
        """
        _response = self._raw_client.create_action_test(
            campaign_id, send_type=send_type, test_emails=test_emails, request_options=request_options
        )
        return _response.data

    def create_action_unschedule(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unschedule a scheduled campaign that hasn't started sending.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_action_unschedule(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.create_action_unschedule(campaign_id, request_options=request_options)
        return _response.data

    def get_content(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Get the the HTML and plain-text content for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.get_content(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.get_content(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def upsert_content(
        self,
        campaign_id: str,
        *,
        links: typing.Optional[typing.Sequence[CampaignContentLinksItem]] = OMIT,
        archive_html: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        plain_text: typing.Optional[str] = OMIT,
        variate_contents: typing.Optional[typing.Sequence[CampaignContentVariateContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Set the content for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        links : typing.Optional[typing.Sequence[CampaignContentLinksItem]]
            A list of link types and descriptions for the API schema documents.

        archive_html : typing.Optional[str]
            The Archive HTML for the campaign.

        html : typing.Optional[str]
            The raw HTML for the campaign.

        plain_text : typing.Optional[str]
            The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.

        variate_contents : typing.Optional[typing.Sequence[CampaignContentVariateContentsItem]]
            Content options for multivariate campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.upsert_content(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.upsert_content(
            campaign_id,
            links=links,
            archive_html=archive_html,
            html=html,
            plain_text=plain_text,
            variate_contents=variate_contents,
            request_options=request_options,
        )
        return _response.data

    def list_feedback(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFeedbackCampaignsResponse:
        """
        Get team feedback while you're working together on a Mailchimp campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFeedbackCampaignsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.list_feedback(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.list_feedback(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def create_feedback(
        self,
        campaign_id: str,
        *,
        message: str,
        block_id: typing.Optional[int] = OMIT,
        is_complete: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFeedbackCampaignsResponse:
        """
        Add feedback on a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        message : str
            The content of the feedback.

        block_id : typing.Optional[int]
            The block id for the editable block that the feedback addresses.

        is_complete : typing.Optional[bool]
            The status of feedback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFeedbackCampaignsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.create_feedback(
            campaign_id="campaign_id",
            message="message",
        )
        """
        _response = self._raw_client.create_feedback(
            campaign_id, message=message, block_id=block_id, is_complete=is_complete, request_options=request_options
        )
        return _response.data

    def get_feedback(
        self,
        campaign_id: str,
        feedback_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignFeedback:
        """
        Get a specific feedback message from a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFeedback


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.get_feedback(
            campaign_id="campaign_id",
            feedback_id="feedback_id",
        )
        """
        _response = self._raw_client.get_feedback(
            campaign_id, feedback_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_feedback(
        self, campaign_id: str, feedback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a specific feedback message for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.delete_feedback(
            campaign_id="campaign_id",
            feedback_id="feedback_id",
        )
        """
        _response = self._raw_client.delete_feedback(campaign_id, feedback_id, request_options=request_options)
        return _response.data

    def update_feedback(
        self,
        campaign_id: str,
        feedback_id: str,
        *,
        block_id: typing.Optional[int] = OMIT,
        is_complete: typing.Optional[bool] = OMIT,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignFeedback:
        """
        Update a specific feedback message for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        block_id : typing.Optional[int]
            The block id for the editable block that the feedback addresses.

        is_complete : typing.Optional[bool]
            The status of feedback.

        message : typing.Optional[str]
            The content of the feedback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFeedback


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.update_feedback(
            campaign_id="campaign_id",
            feedback_id="feedback_id",
        )
        """
        _response = self._raw_client.update_feedback(
            campaign_id,
            feedback_id,
            block_id=block_id,
            is_complete=is_complete,
            message=message,
            request_options=request_options,
        )
        return _response.data

    def list_send_checklist(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSendChecklistCampaignsResponse:
        """
        Review the send checklist for a campaign, and resolve any issues before sending.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSendChecklistCampaignsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaigns.list_send_checklist(
            campaign_id="campaign_id",
        )
        """
        _response = self._raw_client.list_send_checklist(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data


class AsyncCampaignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCampaignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCampaignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCampaignsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ListCampaignsRequestType] = None,
        status: typing.Optional[ListCampaignsRequestStatus] = None,
        before_send_time: typing.Optional[dt.datetime] = None,
        since_send_time: typing.Optional[dt.datetime] = None,
        before_create_time: typing.Optional[dt.datetime] = None,
        since_create_time: typing.Optional[dt.datetime] = None,
        list_id: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        member_id: typing.Optional[str] = None,
        sort_field: typing.Optional[ListCampaignsRequestSortField] = None,
        sort_dir: typing.Optional[ListCampaignsRequestSortDir] = None,
        include_resend_shortcut_eligibility: typing.Optional[bool] = None,
        include_resend_shortcut_usage: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Campaigns, ListCampaignsResponse]:
        """
        Get all campaigns in an account.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[ListCampaignsRequestType]
            The campaign type.

        status : typing.Optional[ListCampaignsRequestStatus]
            The status of the campaign.

        before_send_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_send_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_create_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_create_time : typing.Optional[dt.datetime]
            Restrict the response to campaigns created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        list_id : typing.Optional[str]
            The unique id for the list.

        folder_id : typing.Optional[str]
            The unique folder id.

        member_id : typing.Optional[str]
            Retrieve campaigns sent to a particular list member. Member ID is The MD5 hash of the lowercase version of the list member’s email address.

        sort_field : typing.Optional[ListCampaignsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListCampaignsRequestSortDir]
            Determines the order direction for sorted results.

        include_resend_shortcut_eligibility : typing.Optional[bool]
            Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.

        include_resend_shortcut_usage : typing.Optional[bool]
            Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Campaigns, ListCampaignsResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.campaigns.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            type=type,
            status=status,
            before_send_time=before_send_time,
            since_send_time=since_send_time,
            before_create_time=before_create_time,
            since_create_time=since_create_time,
            list_id=list_id,
            folder_id=folder_id,
            member_id=member_id,
            sort_field=sort_field,
            sort_dir=sort_dir,
            include_resend_shortcut_eligibility=include_resend_shortcut_eligibility,
            include_resend_shortcut_usage=include_resend_shortcut_usage,
            request_options=request_options,
        )

    async def create(
        self,
        *,
        type: CreateCampaignsRequestType,
        content_type: typing.Optional[CreateCampaignsRequestContentType] = OMIT,
        recipients: typing.Optional[CreateCampaignsRequestRecipients] = OMIT,
        rss_opts: typing.Optional[CreateCampaignsRequestRssOpts] = OMIT,
        settings: typing.Optional[CreateCampaignsRequestSettings] = OMIT,
        social_card: typing.Optional[CreateCampaignsRequestSocialCard] = OMIT,
        tracking: typing.Optional[CampaignTrackingOptions] = OMIT,
        variate_settings: typing.Optional[CreateCampaignsRequestVariateSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Create a new Mailchimp campaign.

        Parameters
        ----------
        type : CreateCampaignsRequestType
            There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) you can create in Mailchimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.

        content_type : typing.Optional[CreateCampaignsRequestContentType]
            How the campaign's content is put together. The old drag and drop editor uses 'template' while the new editor uses 'multichannel'. Defaults to template.

        recipients : typing.Optional[CreateCampaignsRequestRecipients]
            List settings for the campaign.

        rss_opts : typing.Optional[CreateCampaignsRequestRssOpts]
            [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options, specific to an RSS campaign.

        settings : typing.Optional[CreateCampaignsRequestSettings]
            The settings for your campaign, including subject, from name, reply-to address, and more.

        social_card : typing.Optional[CreateCampaignsRequestSocialCard]
            The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).

        tracking : typing.Optional[CampaignTrackingOptions]

        variate_settings : typing.Optional[CreateCampaignsRequestVariateSettings]
            The settings specific to A/B test campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create(
                type="regular",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            type=type,
            content_type=content_type,
            recipients=recipients,
            rss_opts=rss_opts,
            settings=settings,
            social_card=social_card,
            tracking=tracking,
            variate_settings=variate_settings,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_resend_shortcut_eligibility: typing.Optional[bool] = None,
        include_resend_shortcut_usage: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Get information about a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_resend_shortcut_eligibility : typing.Optional[bool]
            Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.

        include_resend_shortcut_usage : typing.Optional[bool]
            Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.get(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            campaign_id,
            fields=fields,
            exclude_fields=exclude_fields,
            include_resend_shortcut_eligibility=include_resend_shortcut_eligibility,
            include_resend_shortcut_usage=include_resend_shortcut_usage,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a campaign from your Mailchimp account.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.delete(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(campaign_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        campaign_id: str,
        *,
        recipients: typing.Optional[UpdateCampaignsRequestRecipients] = OMIT,
        rss_opts: typing.Optional[UpdateCampaignsRequestRssOpts] = OMIT,
        settings: typing.Optional[UpdateCampaignsRequestSettings] = OMIT,
        social_card: typing.Optional[UpdateCampaignsRequestSocialCard] = OMIT,
        tracking: typing.Optional[CampaignTrackingOptions] = OMIT,
        variate_settings: typing.Optional[UpdateCampaignsRequestVariateSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Update some or all of the settings for a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        recipients : typing.Optional[UpdateCampaignsRequestRecipients]
            List settings for the campaign.

        rss_opts : typing.Optional[UpdateCampaignsRequestRssOpts]
            [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign.

        settings : typing.Optional[UpdateCampaignsRequestSettings]
            The settings for your campaign, including subject, from name, reply-to address, and more.

        social_card : typing.Optional[UpdateCampaignsRequestSocialCard]
            The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).

        tracking : typing.Optional[CampaignTrackingOptions]

        variate_settings : typing.Optional[UpdateCampaignsRequestVariateSettings]
            The settings specific to A/B test campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.update(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            campaign_id,
            recipients=recipients,
            rss_opts=rss_opts,
            settings=settings,
            social_card=social_card,
            tracking=tracking,
            variate_settings=variate_settings,
            request_options=request_options,
        )
        return _response.data

    async def create_action_cancel_send(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancel a Regular or Plain-Text Campaign after you send, before all of your recipients receive it. This feature is included with Mailchimp Pro.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_cancel_send(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_cancel_send(campaign_id, request_options=request_options)
        return _response.data

    async def create_action_create_resend(
        self,
        campaign_id: str,
        *,
        shortcut_type: typing.Optional[CreateActionCreateResendCampaignsRequestShortcutType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Campaign:
        """
        Remove the guesswork for resending a campaign to certain segments. You can use this endpoint as a shortcut to replicate a campaign and resend it to common segments, such as those who didn't open the campaign, or any new subscribers since it was sent.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        shortcut_type : typing.Optional[CreateActionCreateResendCampaignsRequestShortcutType]
            Which campaign resend shortcut to use. Default is `to_non_openers`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_create_resend(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_create_resend(
            campaign_id, shortcut_type=shortcut_type, request_options=request_options
        )
        return _response.data

    async def create_action_pause(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Pause an RSS-Driven campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_pause(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_pause(campaign_id, request_options=request_options)
        return _response.data

    async def create_action_replicate(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Campaign:
        """
        Replicate a campaign in saved or send status.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_replicate(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_replicate(campaign_id, request_options=request_options)
        return _response.data

    async def create_action_resume(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Resume an RSS-Driven campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_resume(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_resume(campaign_id, request_options=request_options)
        return _response.data

    async def create_action_schedule(
        self,
        campaign_id: str,
        *,
        schedule_time: dt.datetime,
        batch_delivery: typing.Optional[CreateActionScheduleCampaignsRequestBatchDelivery] = OMIT,
        timewarp: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Schedule a campaign for delivery. If you're using Multivariate Campaigns to test send times or sending RSS Campaigns, use the send action instead.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        schedule_time : dt.datetime
            The UTC date and time to schedule the campaign for delivery in ISO 8601 format. Campaigns may only be scheduled to send on the quarter-hour (:00, :15, :30, :45).

        batch_delivery : typing.Optional[CreateActionScheduleCampaignsRequestBatchDelivery]
            Choose whether the campaign should use [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/). Cannot be set to `true` for campaigns using [Timewarp](https://mailchimp.com/help/use-timewarp/).

        timewarp : typing.Optional[bool]
            Choose whether the campaign should use [Timewarp](https://mailchimp.com/help/use-timewarp/) when sending. Campaigns scheduled with Timewarp are localized based on the recipients' time zones. For example, a Timewarp campaign with a `schedule_time` of 13:00 will be sent to each recipient at 1:00pm in their local time. Cannot be set to `true` for campaigns using [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_schedule(
                campaign_id="campaign_id",
                schedule_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_schedule(
            campaign_id,
            schedule_time=schedule_time,
            batch_delivery=batch_delivery,
            timewarp=timewarp,
            request_options=request_options,
        )
        return _response.data

    async def create_action_send(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Send a Mailchimp campaign. For RSS Campaigns, the campaign will send according to its schedule. All other campaigns will send immediately.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_send(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_send(campaign_id, request_options=request_options)
        return _response.data

    async def create_action_test(
        self,
        campaign_id: str,
        *,
        send_type: CreateActionTestCampaignsRequestSendType,
        test_emails: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a test email.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        send_type : CreateActionTestCampaignsRequestSendType
            Choose the type of test email to send.

        test_emails : typing.Sequence[str]
            An array of email addresses to send the test email to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_test(
                campaign_id="campaign_id",
                send_type="html",
                test_emails=["test_emails"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_test(
            campaign_id, send_type=send_type, test_emails=test_emails, request_options=request_options
        )
        return _response.data

    async def create_action_unschedule(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unschedule a scheduled campaign that hasn't started sending.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_action_unschedule(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_unschedule(campaign_id, request_options=request_options)
        return _response.data

    async def get_content(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Get the the HTML and plain-text content for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.get_content(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_content(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def upsert_content(
        self,
        campaign_id: str,
        *,
        links: typing.Optional[typing.Sequence[CampaignContentLinksItem]] = OMIT,
        archive_html: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        plain_text: typing.Optional[str] = OMIT,
        variate_contents: typing.Optional[typing.Sequence[CampaignContentVariateContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Set the content for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        links : typing.Optional[typing.Sequence[CampaignContentLinksItem]]
            A list of link types and descriptions for the API schema documents.

        archive_html : typing.Optional[str]
            The Archive HTML for the campaign.

        html : typing.Optional[str]
            The raw HTML for the campaign.

        plain_text : typing.Optional[str]
            The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.

        variate_contents : typing.Optional[typing.Sequence[CampaignContentVariateContentsItem]]
            Content options for multivariate campaigns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.upsert_content(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_content(
            campaign_id,
            links=links,
            archive_html=archive_html,
            html=html,
            plain_text=plain_text,
            variate_contents=variate_contents,
            request_options=request_options,
        )
        return _response.data

    async def list_feedback(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFeedbackCampaignsResponse:
        """
        Get team feedback while you're working together on a Mailchimp campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFeedbackCampaignsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.list_feedback(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_feedback(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def create_feedback(
        self,
        campaign_id: str,
        *,
        message: str,
        block_id: typing.Optional[int] = OMIT,
        is_complete: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFeedbackCampaignsResponse:
        """
        Add feedback on a specific campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        message : str
            The content of the feedback.

        block_id : typing.Optional[int]
            The block id for the editable block that the feedback addresses.

        is_complete : typing.Optional[bool]
            The status of feedback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFeedbackCampaignsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.create_feedback(
                campaign_id="campaign_id",
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_feedback(
            campaign_id, message=message, block_id=block_id, is_complete=is_complete, request_options=request_options
        )
        return _response.data

    async def get_feedback(
        self,
        campaign_id: str,
        feedback_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignFeedback:
        """
        Get a specific feedback message from a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFeedback


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.get_feedback(
                campaign_id="campaign_id",
                feedback_id="feedback_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feedback(
            campaign_id, feedback_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_feedback(
        self, campaign_id: str, feedback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a specific feedback message for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.delete_feedback(
                campaign_id="campaign_id",
                feedback_id="feedback_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_feedback(campaign_id, feedback_id, request_options=request_options)
        return _response.data

    async def update_feedback(
        self,
        campaign_id: str,
        feedback_id: str,
        *,
        block_id: typing.Optional[int] = OMIT,
        is_complete: typing.Optional[bool] = OMIT,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignFeedback:
        """
        Update a specific feedback message for a campaign.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        feedback_id : str
            The unique id for the feedback message.

        block_id : typing.Optional[int]
            The block id for the editable block that the feedback addresses.

        is_complete : typing.Optional[bool]
            The status of feedback.

        message : typing.Optional[str]
            The content of the feedback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFeedback


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.update_feedback(
                campaign_id="campaign_id",
                feedback_id="feedback_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_feedback(
            campaign_id,
            feedback_id,
            block_id=block_id,
            is_complete=is_complete,
            message=message,
            request_options=request_options,
        )
        return _response.data

    async def list_send_checklist(
        self,
        campaign_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSendChecklistCampaignsResponse:
        """
        Review the send checklist for a campaign, and resolve any issues before sending.

        Parameters
        ----------
        campaign_id : str
            The unique id for the campaign.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSendChecklistCampaignsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaigns.list_send_checklist(
                campaign_id="campaign_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_send_checklist(
            campaign_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data
