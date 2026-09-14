# This file was auto-generated from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.automation_workflow import AutomationWorkflow
from ..types.automation_workflow_email import AutomationWorkflowEmail
from ..types.subscriber_in_automation_queue import SubscriberInAutomationQueue
from ..types.subscriber_removed_from_automation_workflow import SubscriberRemovedFromAutomationWorkflow
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
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAutomationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/automations",
            method="GET",
            params={
                "count": count,
                "offset": offset,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "before_create_time": serialize_datetime(before_create_time)
                if before_create_time is not None
                else None,
                "since_create_time": serialize_datetime(since_create_time) if since_create_time is not None else None,
                "before_start_time": serialize_datetime(before_start_time) if before_start_time is not None else None,
                "since_start_time": serialize_datetime(since_start_time) if since_start_time is not None else None,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAutomationsResponse,
                    parse_obj_as(
                        type_=ListAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.automations
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list(
                    count=count,
                    offset=offset + 1,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    before_create_time=before_create_time,
                    since_create_time=since_create_time,
                    before_start_time=before_start_time,
                    since_start_time=since_start_time,
                    status=status,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        recipients: CreateAutomationsRequestRecipients,
        trigger_settings: CreateAutomationsRequestTriggerSettings,
        settings: typing.Optional[CreateAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationWorkflow]:
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
        HttpResponse[AutomationWorkflow]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/automations",
            method="POST",
            json={
                "recipients": convert_and_respect_annotation_metadata(
                    object_=recipients, annotation=CreateAutomationsRequestRecipients, direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=CreateAutomationsRequestSettings, direction="write"
                ),
                "trigger_settings": convert_and_respect_annotation_metadata(
                    object_=trigger_settings, annotation=CreateAutomationsRequestTriggerSettings, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflow,
                    parse_obj_as(
                        type_=AutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self,
        workflow_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationWorkflow]:
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
        HttpResponse[AutomationWorkflow]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflow,
                    parse_obj_as(
                        type_=AutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_action_archive(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/archive",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_action_pause_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/pause-all-emails",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_action_start_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/start-all-emails",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_emails(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListEmailsAutomationsResponse]:
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
        HttpResponse[ListEmailsAutomationsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmailsAutomationsResponse,
                    parse_obj_as(
                        type_=ListEmailsAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AutomationWorkflowEmail]:
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
        HttpResponse[AutomationWorkflowEmail]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflowEmail,
                    parse_obj_as(
                        type_=AutomationWorkflowEmail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_email(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        delay: typing.Optional[UpdateEmailAutomationsRequestDelay] = OMIT,
        settings: typing.Optional[UpdateEmailAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationWorkflowEmail]:
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
        HttpResponse[AutomationWorkflowEmail]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="PATCH",
            json={
                "delay": convert_and_respect_annotation_metadata(
                    object_=delay, annotation=UpdateEmailAutomationsRequestDelay, direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=UpdateEmailAutomationsRequestSettings, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflowEmail,
                    parse_obj_as(
                        type_=AutomationWorkflowEmail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_email_action_pause(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/actions/pause",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_email_action_start(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/actions/start",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_email_queue(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListEmailQueueAutomationsResponse]:
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
        HttpResponse[ListEmailQueueAutomationsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmailQueueAutomationsResponse,
                    parse_obj_as(
                        type_=ListEmailQueueAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriberInAutomationQueue]:
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
        HttpResponse[SubscriberInAutomationQueue]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue",
            method="POST",
            json={
                "email_address": email_address,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberInAutomationQueue,
                    parse_obj_as(
                        type_=SubscriberInAutomationQueue,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriberInAutomationQueue]:
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
        HttpResponse[SubscriberInAutomationQueue]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue/{encode_path_param(subscriber_hash)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberInAutomationQueue,
                    parse_obj_as(
                        type_=SubscriberInAutomationQueue,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_removed_subscribers(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListRemovedSubscribersAutomationsResponse]:
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
        HttpResponse[ListRemovedSubscribersAutomationsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRemovedSubscribersAutomationsResponse,
                    parse_obj_as(
                        type_=ListRemovedSubscribersAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_removed_subscriber(
        self, workflow_id: str, *, email_address: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriberRemovedFromAutomationWorkflow]:
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
        HttpResponse[SubscriberRemovedFromAutomationWorkflow]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers",
            method="POST",
            json={
                "email_address": email_address,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberRemovedFromAutomationWorkflow,
                    parse_obj_as(
                        type_=SubscriberRemovedFromAutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_removed_subscriber(
        self, workflow_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriberRemovedFromAutomationWorkflow]:
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
        HttpResponse[SubscriberRemovedFromAutomationWorkflow]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers/{encode_path_param(subscriber_hash)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberRemovedFromAutomationWorkflow,
                    parse_obj_as(
                        type_=SubscriberRemovedFromAutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAutomationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/automations",
            method="GET",
            params={
                "count": count,
                "offset": offset,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "before_create_time": serialize_datetime(before_create_time)
                if before_create_time is not None
                else None,
                "since_create_time": serialize_datetime(since_create_time) if since_create_time is not None else None,
                "before_start_time": serialize_datetime(before_start_time) if before_start_time is not None else None,
                "since_start_time": serialize_datetime(since_start_time) if since_start_time is not None else None,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAutomationsResponse,
                    parse_obj_as(
                        type_=ListAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.automations
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list(
                        count=count,
                        offset=offset + 1,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        before_create_time=before_create_time,
                        since_create_time=since_create_time,
                        before_start_time=before_start_time,
                        since_start_time=since_start_time,
                        status=status,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        recipients: CreateAutomationsRequestRecipients,
        trigger_settings: CreateAutomationsRequestTriggerSettings,
        settings: typing.Optional[CreateAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationWorkflow]:
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
        AsyncHttpResponse[AutomationWorkflow]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/automations",
            method="POST",
            json={
                "recipients": convert_and_respect_annotation_metadata(
                    object_=recipients, annotation=CreateAutomationsRequestRecipients, direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=CreateAutomationsRequestSettings, direction="write"
                ),
                "trigger_settings": convert_and_respect_annotation_metadata(
                    object_=trigger_settings, annotation=CreateAutomationsRequestTriggerSettings, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflow,
                    parse_obj_as(
                        type_=AutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self,
        workflow_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationWorkflow]:
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
        AsyncHttpResponse[AutomationWorkflow]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflow,
                    parse_obj_as(
                        type_=AutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_action_archive(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/archive",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_action_pause_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/pause-all-emails",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_action_start_all_email(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/actions/start-all-emails",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_emails(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListEmailsAutomationsResponse]:
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
        AsyncHttpResponse[ListEmailsAutomationsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmailsAutomationsResponse,
                    parse_obj_as(
                        type_=ListEmailsAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AutomationWorkflowEmail]:
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
        AsyncHttpResponse[AutomationWorkflowEmail]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflowEmail,
                    parse_obj_as(
                        type_=AutomationWorkflowEmail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_email(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_email(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        delay: typing.Optional[UpdateEmailAutomationsRequestDelay] = OMIT,
        settings: typing.Optional[UpdateEmailAutomationsRequestSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationWorkflowEmail]:
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
        AsyncHttpResponse[AutomationWorkflowEmail]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}",
            method="PATCH",
            json={
                "delay": convert_and_respect_annotation_metadata(
                    object_=delay, annotation=UpdateEmailAutomationsRequestDelay, direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=UpdateEmailAutomationsRequestSettings, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationWorkflowEmail,
                    parse_obj_as(
                        type_=AutomationWorkflowEmail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_email_action_pause(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/actions/pause",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_email_action_start(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/actions/start",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_email_queue(
        self, workflow_id: str, workflow_email_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListEmailQueueAutomationsResponse]:
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
        AsyncHttpResponse[ListEmailQueueAutomationsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmailQueueAutomationsResponse,
                    parse_obj_as(
                        type_=ListEmailQueueAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriberInAutomationQueue]:
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
        AsyncHttpResponse[SubscriberInAutomationQueue]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue",
            method="POST",
            json={
                "email_address": email_address,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberInAutomationQueue,
                    parse_obj_as(
                        type_=SubscriberInAutomationQueue,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_email_queue(
        self,
        workflow_id: str,
        workflow_email_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriberInAutomationQueue]:
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
        AsyncHttpResponse[SubscriberInAutomationQueue]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/emails/{encode_path_param(workflow_email_id)}/queue/{encode_path_param(subscriber_hash)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberInAutomationQueue,
                    parse_obj_as(
                        type_=SubscriberInAutomationQueue,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_removed_subscribers(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListRemovedSubscribersAutomationsResponse]:
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
        AsyncHttpResponse[ListRemovedSubscribersAutomationsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRemovedSubscribersAutomationsResponse,
                    parse_obj_as(
                        type_=ListRemovedSubscribersAutomationsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_removed_subscriber(
        self, workflow_id: str, *, email_address: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriberRemovedFromAutomationWorkflow]:
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
        AsyncHttpResponse[SubscriberRemovedFromAutomationWorkflow]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers",
            method="POST",
            json={
                "email_address": email_address,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberRemovedFromAutomationWorkflow,
                    parse_obj_as(
                        type_=SubscriberRemovedFromAutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_removed_subscriber(
        self, workflow_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriberRemovedFromAutomationWorkflow]:
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
        AsyncHttpResponse[SubscriberRemovedFromAutomationWorkflow]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/automations/{encode_path_param(workflow_id)}/removed-subscribers/{encode_path_param(subscriber_hash)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberRemovedFromAutomationWorkflow,
                    parse_obj_as(
                        type_=SubscriberRemovedFromAutomationWorkflow,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
