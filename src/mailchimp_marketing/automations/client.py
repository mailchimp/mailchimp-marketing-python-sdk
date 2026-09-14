# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.automation_workflow import AutomationWorkflow
from ..types.automation_workflow_email import AutomationWorkflowEmail
from ..types.subscriber_in_automation_queue import SubscriberInAutomationQueue
from ..types.subscriber_removed_from_automation_workflow import SubscriberRemovedFromAutomationWorkflow
from .raw_client import AsyncRawAutomationsClient, RawAutomationsClient
from .types.create_automations_request_recipients import CreateAutomationsRequestRecipients
from .types.create_automations_request_settings import CreateAutomationsRequestSettings
from .types.create_automations_request_trigger_settings import CreateAutomationsRequestTriggerSettings
from .types.list_automations_request_status import ListAutomationsRequestStatus
from .types.list_automations_response import ListAutomationsResponse
from .types.list_email_queue_automations_response import ListEmailQueueAutomationsResponse
from .types.list_emails_automations_response import ListEmailsAutomationsResponse
from .types.list_removed_subscribers_automations_response import ListRemovedSubscribersAutomationsResponse
from .types.update_email_automations_request_delay import UpdateEmailAutomationsRequestDelay
from .types.update_email_automations_request_settings import UpdateEmailAutomationsRequestSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AutomationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAutomationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAutomationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAutomationsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        before_create_time: typing.Optional[dt.datetime] = None,
        since_create_time: typing.Optional[dt.datetime] = None,
        before_start_time: typing.Optional[dt.datetime] = None,
        since_start_time: typing.Optional[dt.datetime] = None,
        status: typing.Optional[ListAutomationsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[AutomationWorkflow, ListAutomationsResponse]:
        """
        Get a summary of an account's classic automations.

        Parameters
        ----------
        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        before_create_time : typing.Optional[dt.datetime]
            Restrict the response to automations created before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_create_time : typing.Optional[dt.datetime]
            Restrict the response to automations created after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_start_time : typing.Optional[dt.datetime]
            Restrict the response to automations started before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_start_time : typing.Optional[dt.datetime]
            Restrict the response to automations started after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        status : typing.Optional[ListAutomationsRequestStatus]
            Restrict the results to automations with the specified status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[AutomationWorkflow, ListAutomationsResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.automations.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            count=count,
            offset=offset,
            fields=fields,
            exclude_fields=exclude_fields,
            before_create_time=before_create_time,
            since_create_time=since_create_time,
            before_start_time=before_start_time,
            since_start_time=since_start_time,
            status=status,
            request_options=request_options,
        )

    def create(
        self,
        *,
        recipients: CreateAutomationsRequestRecipients,
        trigger_settings: CreateAutomationsRequestTriggerSettings,
        settings: typing.Optional[CreateAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflow:
        """
        Create a new classic automation in your Mailchimp account.

        Parameters
        ----------
        recipients : CreateAutomationsRequestRecipients
            List settings for the Automation.

        trigger_settings : CreateAutomationsRequestTriggerSettings
            Trigger settings for the Automation.

        settings : typing.Optional[CreateAutomationsRequestSettings]
            The settings for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflow


        Examples
        --------
        from mailchimp_marketing import MailchimpClient
        from mailchimp_marketing.automations import (
            CreateAutomationsRequestRecipients,
            CreateAutomationsRequestTriggerSettings,
        )

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.create(
            recipients=CreateAutomationsRequestRecipients(),
            trigger_settings=CreateAutomationsRequestTriggerSettings(
                workflow_type="abandonedBrowse",
            ),
        )
        """
        _response = self._raw_client.create(
            recipients=recipients, trigger_settings=trigger_settings, settings=settings, request_options=request_options
        )
        return _response.data

    def get(
        self,
        workflow_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflow:
        """
        Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflow


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.get(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.get(
            workflow_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def create_action_archive(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Archiving will permanently end your automation and keep the report data. You’ll be able to replicate your archived automation, but you can’t restart it.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
        client.automations.create_action_archive(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.create_action_archive(workflow_id, request_options=request_options)
        return _response.data

    def create_action_pause_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Pause all emails in a specific classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
        client.automations.create_action_pause_all_email(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.create_action_pause_all_email(workflow_id, request_options=request_options)
        return _response.data

    def create_action_start_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start all emails in a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
        client.automations.create_action_start_all_email(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.create_action_start_all_email(workflow_id, request_options=request_options)
        return _response.data

    def list_emails(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEmailsAutomationsResponse:
        """
        Get a summary of the emails in a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmailsAutomationsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.list_emails(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.list_emails(workflow_id, request_options=request_options)
        return _response.data

    def get_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AutomationWorkflowEmail:
        """
        Get information about an individual classic automation workflow email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflowEmail


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.get_email(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.get_email(workflow_id, workflow_email_id, request_options=request_options)
        return _response.data

    def delete_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes an individual classic automation workflow email. Emails from certain workflow types, including the Abandoned Cart Email (abandonedCart) and Product Retargeting Email (abandonedBrowse) Workflows, cannot be deleted.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
        client.automations.delete_email(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.delete_email(workflow_id, workflow_email_id, request_options=request_options)
        return _response.data

    def update_email(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        delay: typing.Optional[UpdateEmailAutomationsRequestDelay] = OMIT,
        settings: typing.Optional[UpdateEmailAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflowEmail:
        """
        Update settings for a classic automation workflow email.  Only works with workflows of type: abandonedBrowse, abandonedCart, emailFollowup, or singleWelcome.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        delay : typing.Optional[UpdateEmailAutomationsRequestDelay]
            The delay settings for an automation email.

        settings : typing.Optional[UpdateEmailAutomationsRequestSettings]
            Settings for the campaign including the email subject, from name, and from email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflowEmail


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.update_email(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.update_email(
            workflow_id, workflow_email_id, delay=delay, settings=settings, request_options=request_options
        )
        return _response.data

    def create_email_action_pause(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Pause an automated email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
        client.automations.create_email_action_pause(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.create_email_action_pause(
            workflow_id, workflow_email_id, request_options=request_options
        )
        return _response.data

    def create_email_action_start(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start an automated email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
        client.automations.create_email_action_start(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.create_email_action_start(
            workflow_id, workflow_email_id, request_options=request_options
        )
        return _response.data

    def list_email_queue(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEmailQueueAutomationsResponse:
        """
        Get information about a classic automation email queue.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmailQueueAutomationsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.list_email_queue(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
        )
        """
        _response = self._raw_client.list_email_queue(workflow_id, workflow_email_id, request_options=request_options)
        return _response.data

    def create_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriberInAutomationQueue:
        """
        Manually add a subscriber to a workflow, bypassing the default trigger settings. You can also use this endpoint to trigger a series of automated emails in an API 3.0 workflow type.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        email_address : str
            The list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberInAutomationQueue


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.create_email_queue(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
            email_address="email_address",
        )
        """
        _response = self._raw_client.create_email_queue(
            workflow_id, workflow_email_id, email_address=email_address, request_options=request_options
        )
        return _response.data

    def get_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriberInAutomationQueue:
        """
        Get information about a specific subscriber in a classic automation email queue.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberInAutomationQueue


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.get_email_queue(
            workflow_id="workflow_id",
            workflow_email_id="workflow_email_id",
            subscriber_hash="subscriber_hash",
        )
        """
        _response = self._raw_client.get_email_queue(
            workflow_id, workflow_email_id, subscriber_hash, request_options=request_options
        )
        return _response.data

    def list_removed_subscribers(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRemovedSubscribersAutomationsResponse:
        """
        Get information about subscribers who were removed from a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRemovedSubscribersAutomationsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.list_removed_subscribers(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.list_removed_subscribers(workflow_id, request_options=request_options)
        return _response.data

    def create_removed_subscriber(
        self, workflow_id: str, *, email_address: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriberRemovedFromAutomationWorkflow:
        """
        Remove a subscriber from a specific classic automation workflow. You can remove a subscriber at any point in an automation workflow, regardless of how many emails they've been sent from that workflow. Once they're removed, they can never be added back to the same workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        email_address : str
            The list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberRemovedFromAutomationWorkflow


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.create_removed_subscriber(
            workflow_id="workflow_id",
            email_address="email_address",
        )
        """
        _response = self._raw_client.create_removed_subscriber(
            workflow_id, email_address=email_address, request_options=request_options
        )
        return _response.data

    def get_removed_subscriber(
        self, workflow_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriberRemovedFromAutomationWorkflow:
        """
        Get information about a specific subscriber who was removed from a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberRemovedFromAutomationWorkflow


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.automations.get_removed_subscriber(
            workflow_id="workflow_id",
            subscriber_hash="subscriber_hash",
        )
        """
        _response = self._raw_client.get_removed_subscriber(
            workflow_id, subscriber_hash, request_options=request_options
        )
        return _response.data


class AsyncAutomationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAutomationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAutomationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAutomationsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        before_create_time: typing.Optional[dt.datetime] = None,
        since_create_time: typing.Optional[dt.datetime] = None,
        before_start_time: typing.Optional[dt.datetime] = None,
        since_start_time: typing.Optional[dt.datetime] = None,
        status: typing.Optional[ListAutomationsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[AutomationWorkflow, ListAutomationsResponse]:
        """
        Get a summary of an account's classic automations.

        Parameters
        ----------
        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        before_create_time : typing.Optional[dt.datetime]
            Restrict the response to automations created before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_create_time : typing.Optional[dt.datetime]
            Restrict the response to automations created after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_start_time : typing.Optional[dt.datetime]
            Restrict the response to automations started before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_start_time : typing.Optional[dt.datetime]
            Restrict the response to automations started after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        status : typing.Optional[ListAutomationsRequestStatus]
            Restrict the results to automations with the specified status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[AutomationWorkflow, ListAutomationsResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.automations.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            count=count,
            offset=offset,
            fields=fields,
            exclude_fields=exclude_fields,
            before_create_time=before_create_time,
            since_create_time=since_create_time,
            before_start_time=before_start_time,
            since_start_time=since_start_time,
            status=status,
            request_options=request_options,
        )

    async def create(
        self,
        *,
        recipients: CreateAutomationsRequestRecipients,
        trigger_settings: CreateAutomationsRequestTriggerSettings,
        settings: typing.Optional[CreateAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflow:
        """
        Create a new classic automation in your Mailchimp account.

        Parameters
        ----------
        recipients : CreateAutomationsRequestRecipients
            List settings for the Automation.

        trigger_settings : CreateAutomationsRequestTriggerSettings
            Trigger settings for the Automation.

        settings : typing.Optional[CreateAutomationsRequestSettings]
            The settings for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflow


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient
        from mailchimp_marketing.automations import (
            CreateAutomationsRequestRecipients,
            CreateAutomationsRequestTriggerSettings,
        )

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.create(
                recipients=CreateAutomationsRequestRecipients(),
                trigger_settings=CreateAutomationsRequestTriggerSettings(
                    workflow_type="abandonedBrowse",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            recipients=recipients, trigger_settings=trigger_settings, settings=settings, request_options=request_options
        )
        return _response.data

    async def get(
        self,
        workflow_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflow:
        """
        Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflow


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.get(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            workflow_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def create_action_archive(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Archiving will permanently end your automation and keep the report data. You’ll be able to replicate your archived automation, but you can’t restart it.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
            await client.automations.create_action_archive(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_archive(workflow_id, request_options=request_options)
        return _response.data

    async def create_action_pause_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Pause all emails in a specific classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
            await client.automations.create_action_pause_all_email(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_pause_all_email(workflow_id, request_options=request_options)
        return _response.data

    async def create_action_start_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start all emails in a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

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
            await client.automations.create_action_start_all_email(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_start_all_email(workflow_id, request_options=request_options)
        return _response.data

    async def list_emails(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEmailsAutomationsResponse:
        """
        Get a summary of the emails in a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmailsAutomationsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.list_emails(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_emails(workflow_id, request_options=request_options)
        return _response.data

    async def get_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AutomationWorkflowEmail:
        """
        Get information about an individual classic automation workflow email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflowEmail


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.get_email(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_email(workflow_id, workflow_email_id, request_options=request_options)
        return _response.data

    async def delete_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes an individual classic automation workflow email. Emails from certain workflow types, including the Abandoned Cart Email (abandonedCart) and Product Retargeting Email (abandonedBrowse) Workflows, cannot be deleted.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
            await client.automations.delete_email(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_email(workflow_id, workflow_email_id, request_options=request_options)
        return _response.data

    async def update_email(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        delay: typing.Optional[UpdateEmailAutomationsRequestDelay] = OMIT,
        settings: typing.Optional[UpdateEmailAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationWorkflowEmail:
        """
        Update settings for a classic automation workflow email.  Only works with workflows of type: abandonedBrowse, abandonedCart, emailFollowup, or singleWelcome.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        delay : typing.Optional[UpdateEmailAutomationsRequestDelay]
            The delay settings for an automation email.

        settings : typing.Optional[UpdateEmailAutomationsRequestSettings]
            Settings for the campaign including the email subject, from name, and from email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationWorkflowEmail


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.update_email(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_email(
            workflow_id, workflow_email_id, delay=delay, settings=settings, request_options=request_options
        )
        return _response.data

    async def create_email_action_pause(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Pause an automated email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
            await client.automations.create_email_action_pause(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_email_action_pause(
            workflow_id, workflow_email_id, request_options=request_options
        )
        return _response.data

    async def create_email_action_start(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start an automated email.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

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
            await client.automations.create_email_action_start(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_email_action_start(
            workflow_id, workflow_email_id, request_options=request_options
        )
        return _response.data

    async def list_email_queue(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEmailQueueAutomationsResponse:
        """
        Get information about a classic automation email queue.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmailQueueAutomationsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.list_email_queue(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_email_queue(
            workflow_id, workflow_email_id, request_options=request_options
        )
        return _response.data

    async def create_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriberInAutomationQueue:
        """
        Manually add a subscriber to a workflow, bypassing the default trigger settings. You can also use this endpoint to trigger a series of automated emails in an API 3.0 workflow type.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        email_address : str
            The list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberInAutomationQueue


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.create_email_queue(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
                email_address="email_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_email_queue(
            workflow_id, workflow_email_id, email_address=email_address, request_options=request_options
        )
        return _response.data

    async def get_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriberInAutomationQueue:
        """
        Get information about a specific subscriber in a classic automation email queue.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        workflow_email_id : str
            The unique id for the Automation workflow email.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberInAutomationQueue


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.get_email_queue(
                workflow_id="workflow_id",
                workflow_email_id="workflow_email_id",
                subscriber_hash="subscriber_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_email_queue(
            workflow_id, workflow_email_id, subscriber_hash, request_options=request_options
        )
        return _response.data

    async def list_removed_subscribers(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRemovedSubscribersAutomationsResponse:
        """
        Get information about subscribers who were removed from a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRemovedSubscribersAutomationsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.list_removed_subscribers(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_removed_subscribers(workflow_id, request_options=request_options)
        return _response.data

    async def create_removed_subscriber(
        self, workflow_id: str, *, email_address: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriberRemovedFromAutomationWorkflow:
        """
        Remove a subscriber from a specific classic automation workflow. You can remove a subscriber at any point in an automation workflow, regardless of how many emails they've been sent from that workflow. Once they're removed, they can never be added back to the same workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        email_address : str
            The list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberRemovedFromAutomationWorkflow


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.create_removed_subscriber(
                workflow_id="workflow_id",
                email_address="email_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_removed_subscriber(
            workflow_id, email_address=email_address, request_options=request_options
        )
        return _response.data

    async def get_removed_subscriber(
        self, workflow_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriberRemovedFromAutomationWorkflow:
        """
        Get information about a specific subscriber who was removed from a classic automation workflow.

        Parameters
        ----------
        workflow_id : str
            The unique id for the Automation workflow.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriberRemovedFromAutomationWorkflow


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.automations.get_removed_subscriber(
                workflow_id="workflow_id",
                subscriber_hash="subscriber_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_removed_subscriber(
            workflow_id, subscriber_hash, request_options=request_options
        )
        return _response.data
