# This file was auto-generated from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.add_webhook_events import AddWebhookEvents
from ..types.add_webhook_sources import AddWebhookSources
from ..types.growth_history import GrowthHistory
from ..types.interest import Interest
from ..types.interest_category import InterestCategory
from ..types.list_ import List
from ..types.list_members import ListMembers
from ..types.list_webhooks import ListWebhooks
from ..types.lists_abuse_reports import ListsAbuseReports
from ..types.lists_segments_members import ListsSegmentsMembers
from ..types.member_notes import MemberNotes
from ..types.merge_field import MergeField
from ..types.signup_form import SignupForm
from ..types.subscriber_list import SubscriberList
from ..types.survey_section_request import SurveySectionRequest
from .types.batch_add_or_remove_members_lists_response import BatchAddOrRemoveMembersListsResponse
from .types.batch_subscribe_or_unsubscribe_lists_request_members_item import (
    BatchSubscribeOrUnsubscribeListsRequestMembersItem,
)
from .types.batch_subscribe_or_unsubscribe_lists_response import BatchSubscribeOrUnsubscribeListsResponse
from .types.create_interest_category_lists_request_type import CreateInterestCategoryListsRequestType
from .types.create_lists_request_campaign_defaults import CreateListsRequestCampaignDefaults
from .types.create_lists_request_contact import CreateListsRequestContact
from .types.create_member_lists_request_location import CreateMemberListsRequestLocation
from .types.create_member_lists_request_marketing_permissions_item import (
    CreateMemberListsRequestMarketingPermissionsItem,
)
from .types.create_member_lists_request_merge_fields_value import CreateMemberListsRequestMergeFieldsValue
from .types.create_member_lists_request_status import CreateMemberListsRequestStatus
from .types.create_member_lists_request_timestamp_opt import CreateMemberListsRequestTimestampOpt
from .types.create_member_lists_request_timestamp_signup import CreateMemberListsRequestTimestampSignup
from .types.create_member_tag_lists_request_tags_item import CreateMemberTagListsRequestTagsItem
from .types.create_merge_field_lists_request_options import CreateMergeFieldListsRequestOptions
from .types.create_merge_field_lists_request_type import CreateMergeFieldListsRequestType
from .types.create_segment_lists_request_options import CreateSegmentListsRequestOptions
from .types.create_signup_form_lists_request_contents_item import CreateSignupFormListsRequestContentsItem
from .types.create_signup_form_lists_request_header import CreateSignupFormListsRequestHeader
from .types.create_signup_form_lists_request_styles_item import CreateSignupFormListsRequestStylesItem
from .types.create_webhook_lists_response import CreateWebhookListsResponse
from .types.list_abuse_reports_lists_response import ListAbuseReportsListsResponse
from .types.list_activity_lists_response import ListActivityListsResponse
from .types.list_activity_lists_response_activity_item import ListActivityListsResponseActivityItem
from .types.list_clients_lists_response import ListClientsListsResponse
from .types.list_growth_history_lists_request_sort_dir import ListGrowthHistoryListsRequestSortDir
from .types.list_growth_history_lists_request_sort_field import ListGrowthHistoryListsRequestSortField
from .types.list_growth_history_lists_response import ListGrowthHistoryListsResponse
from .types.list_interest_categories_lists_request_sort_dir import ListInterestCategoriesListsRequestSortDir
from .types.list_interest_categories_lists_request_sort_field import ListInterestCategoriesListsRequestSortField
from .types.list_interest_categories_lists_response import ListInterestCategoriesListsResponse
from .types.list_interest_category_interests_lists_response import ListInterestCategoryInterestsListsResponse
from .types.list_lists_request_sort_dir import ListListsRequestSortDir
from .types.list_lists_request_sort_field import ListListsRequestSortField
from .types.list_lists_response import ListListsResponse
from .types.list_locations_lists_response import ListLocationsListsResponse
from .types.list_member_activity_feed_lists_request_activity_filters_item import (
    ListMemberActivityFeedListsRequestActivityFiltersItem,
)
from .types.list_member_activity_feed_lists_response import ListMemberActivityFeedListsResponse
from .types.list_member_activity_lists_request_action_item import ListMemberActivityListsRequestActionItem
from .types.list_member_activity_lists_response import ListMemberActivityListsResponse
from .types.list_member_events_lists_response import ListMemberEventsListsResponse
from .types.list_member_events_lists_response_events_item import ListMemberEventsListsResponseEventsItem
from .types.list_member_goals_lists_response import ListMemberGoalsListsResponse
from .types.list_member_notes_lists_request_sort_dir import ListMemberNotesListsRequestSortDir
from .types.list_member_notes_lists_request_sort_field import ListMemberNotesListsRequestSortField
from .types.list_member_notes_lists_response import ListMemberNotesListsResponse
from .types.list_member_tags_lists_response import ListMemberTagsListsResponse
from .types.list_member_tags_lists_response_tags_item import ListMemberTagsListsResponseTagsItem
from .types.list_members_lists_request_interest_match import ListMembersListsRequestInterestMatch
from .types.list_members_lists_request_sort_dir import ListMembersListsRequestSortDir
from .types.list_members_lists_request_sort_field import ListMembersListsRequestSortField
from .types.list_members_lists_request_status import ListMembersListsRequestStatus
from .types.list_members_lists_response import ListMembersListsResponse
from .types.list_merge_fields_lists_response import ListMergeFieldsListsResponse
from .types.list_segment_members_lists_response import ListSegmentMembersListsResponse
from .types.list_segments_lists_request_exclude_type import ListSegmentsListsRequestExcludeType
from .types.list_segments_lists_response import ListSegmentsListsResponse
from .types.list_signup_forms_lists_response import ListSignupFormsListsResponse
from .types.list_tag_search_lists_response import ListTagSearchListsResponse
from .types.list_webhooks_lists_response import ListWebhooksListsResponse
from .types.update_interest_category_lists_request_type import UpdateInterestCategoryListsRequestType
from .types.update_lists_request_campaign_defaults import UpdateListsRequestCampaignDefaults
from .types.update_lists_request_contact import UpdateListsRequestContact
from .types.update_member_lists_request_location import UpdateMemberListsRequestLocation
from .types.update_member_lists_request_marketing_permissions_item import (
    UpdateMemberListsRequestMarketingPermissionsItem,
)
from .types.update_member_lists_request_merge_fields_value import UpdateMemberListsRequestMergeFieldsValue
from .types.update_member_lists_request_status import UpdateMemberListsRequestStatus
from .types.update_member_lists_request_timestamp_opt import UpdateMemberListsRequestTimestampOpt
from .types.update_member_lists_request_timestamp_signup import UpdateMemberListsRequestTimestampSignup
from .types.update_merge_field_lists_request_options import UpdateMergeFieldListsRequestOptions
from .types.update_segment_lists_request_options import UpdateSegmentListsRequestOptions
from .types.upsert_member_lists_request_location import UpsertMemberListsRequestLocation
from .types.upsert_member_lists_request_marketing_permissions_item import (
    UpsertMemberListsRequestMarketingPermissionsItem,
)
from .types.upsert_member_lists_request_merge_fields_value import UpsertMemberListsRequestMergeFieldsValue
from .types.upsert_member_lists_request_status import UpsertMemberListsRequestStatus
from .types.upsert_member_lists_request_status_if_new import UpsertMemberListsRequestStatusIfNew
from .types.upsert_member_lists_request_timestamp_opt import UpsertMemberListsRequestTimestampOpt
from .types.upsert_member_lists_request_timestamp_signup import UpsertMemberListsRequestTimestampSignup
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        before_date_created: typing.Optional[str] = None,
        since_date_created: typing.Optional[str] = None,
        before_campaign_last_sent: typing.Optional[str] = None,
        since_campaign_last_sent: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        sort_field: typing.Optional[ListListsRequestSortField] = None,
        sort_dir: typing.Optional[ListListsRequestSortDir] = None,
        has_ecommerce_store: typing.Optional[bool] = None,
        include_total_contacts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[SubscriberList, ListListsResponse]:
        """
        Get information about all lists in the account.

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

        before_date_created : typing.Optional[str]
            Restrict response to lists created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_date_created : typing.Optional[str]
            Restrict results to lists created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_campaign_last_sent : typing.Optional[str]
            Restrict results to lists created before the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_campaign_last_sent : typing.Optional[str]
            Restrict results to lists created after the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        email : typing.Optional[str]
            Restrict results to lists that include a specific subscriber's email address.

        sort_field : typing.Optional[ListListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListListsRequestSortDir]
            Determines the order direction for sorted results.

        has_ecommerce_store : typing.Optional[bool]
            Restrict results to lists that contain an active, connected, undeleted ecommerce store.

        include_total_contacts : typing.Optional[bool]
            Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[SubscriberList, ListListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/lists",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "before_date_created": before_date_created,
                "since_date_created": since_date_created,
                "before_campaign_last_sent": before_campaign_last_sent,
                "since_campaign_last_sent": since_campaign_last_sent,
                "email": email,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "has_ecommerce_store": has_ecommerce_store,
                "include_total_contacts": include_total_contacts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListListsResponse,
                    parse_obj_as(
                        type_=ListListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.lists
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list(
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    before_date_created=before_date_created,
                    since_date_created=since_date_created,
                    before_campaign_last_sent=before_campaign_last_sent,
                    since_campaign_last_sent=since_campaign_last_sent,
                    email=email,
                    sort_field=sort_field,
                    sort_dir=sort_dir,
                    has_ecommerce_store=has_ecommerce_store,
                    include_total_contacts=include_total_contacts,
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
        campaign_defaults: CreateListsRequestCampaignDefaults,
        contact: CreateListsRequestContact,
        email_type_option: bool,
        name: str,
        permission_reminder: str,
        double_optin: typing.Optional[bool] = OMIT,
        marketing_permissions: typing.Optional[bool] = OMIT,
        notify_on_subscribe: typing.Optional[str] = OMIT,
        notify_on_unsubscribe: typing.Optional[str] = OMIT,
        use_archive_bar: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriberList]:
        """
        Create a new list in your Mailchimp account.

        Parameters
        ----------
        campaign_defaults : CreateListsRequestCampaignDefaults
            [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.

        contact : CreateListsRequestContact
            [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.

        email_type_option : bool
            Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.

        name : str
            The name of the list.

        permission_reminder : str
            The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.

        double_optin : typing.Optional[bool]
            Whether or not to require the subscriber to confirm subscription via email.

        marketing_permissions : typing.Optional[bool]
            Whether or not the list has marketing permissions (eg. GDPR) enabled.

        notify_on_subscribe : typing.Optional[str]
            The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        notify_on_unsubscribe : typing.Optional[str]
            The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        use_archive_bar : typing.Optional[bool]
            Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriberList]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/lists",
            method="POST",
            json={
                "campaign_defaults": convert_and_respect_annotation_metadata(
                    object_=campaign_defaults, annotation=CreateListsRequestCampaignDefaults, direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=CreateListsRequestContact, direction="write"
                ),
                "double_optin": double_optin,
                "email_type_option": email_type_option,
                "marketing_permissions": marketing_permissions,
                "name": name,
                "notify_on_subscribe": notify_on_subscribe,
                "notify_on_unsubscribe": notify_on_unsubscribe,
                "permission_reminder": permission_reminder,
                "use_archive_bar": use_archive_bar,
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
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_total_contacts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriberList]:
        """
        Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_total_contacts : typing.Optional[bool]
            Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriberList]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "include_total_contacts": include_total_contacts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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

    def batch_subscribe_or_unsubscribe(
        self,
        list_id: str,
        *,
        members: typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem],
        skip_merge_validation: typing.Optional[bool] = None,
        skip_duplicate_check: typing.Optional[bool] = None,
        sync_tags: typing.Optional[bool] = OMIT,
        update_existing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchSubscribeOrUnsubscribeListsResponse]:
        """
        Batch subscribe or unsubscribe list members.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        members : typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem]
            An array of objects, each representing an email address and the subscription status for a specific list. Up to 500 members may be added or updated with each API call.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        skip_duplicate_check : typing.Optional[bool]
            If skip_duplicate_check is true, we will ignore duplicates sent in the request when using the batch sub/unsub on the lists endpoint. The status of the first appearance in the request will be saved. This defaults to false.

        sync_tags : typing.Optional[bool]
            Whether this batch operation will replace all existing tags with tags in request.

        update_existing : typing.Optional[bool]
            Whether this batch operation will change existing members' subscription status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchSubscribeOrUnsubscribeListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="POST",
            params={
                "skip_merge_validation": skip_merge_validation,
                "skip_duplicate_check": skip_duplicate_check,
            },
            json={
                "members": convert_and_respect_annotation_metadata(
                    object_=members,
                    annotation=typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem],
                    direction="write",
                ),
                "sync_tags": sync_tags,
                "update_existing": update_existing,
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
                    BatchSubscribeOrUnsubscribeListsResponse,
                    parse_obj_as(
                        type_=BatchSubscribeOrUnsubscribeListsResponse,  # type: ignore
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

    def delete(self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete a list from your Mailchimp account. If you delete a list, you'll lose the list history—including subscriber activity, unsubscribes, complaints, and bounces. You’ll also lose subscribers’ email addresses, unless you exported and backed up your list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
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

    def update(
        self,
        list_id: str,
        *,
        campaign_defaults: typing.Optional[UpdateListsRequestCampaignDefaults] = OMIT,
        contact: typing.Optional[UpdateListsRequestContact] = OMIT,
        double_optin: typing.Optional[bool] = OMIT,
        email_type_option: typing.Optional[bool] = OMIT,
        marketing_permissions: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        notify_on_subscribe: typing.Optional[str] = OMIT,
        notify_on_unsubscribe: typing.Optional[str] = OMIT,
        permission_reminder: typing.Optional[str] = OMIT,
        use_archive_bar: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriberList]:
        """
        Update the settings for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        campaign_defaults : typing.Optional[UpdateListsRequestCampaignDefaults]
            [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.

        contact : typing.Optional[UpdateListsRequestContact]
            [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.

        double_optin : typing.Optional[bool]
            Whether or not to require the subscriber to confirm subscription via email.

        email_type_option : typing.Optional[bool]
            Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.

        marketing_permissions : typing.Optional[bool]
            Whether or not the list has marketing permissions (eg. GDPR) enabled.

        name : typing.Optional[str]
            The name of the list.

        notify_on_subscribe : typing.Optional[str]
            The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        notify_on_unsubscribe : typing.Optional[str]
            The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        permission_reminder : typing.Optional[str]
            The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.

        use_archive_bar : typing.Optional[bool]
            Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriberList]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="PATCH",
            json={
                "campaign_defaults": convert_and_respect_annotation_metadata(
                    object_=campaign_defaults, annotation=UpdateListsRequestCampaignDefaults, direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=UpdateListsRequestContact, direction="write"
                ),
                "double_optin": double_optin,
                "email_type_option": email_type_option,
                "marketing_permissions": marketing_permissions,
                "name": name,
                "notify_on_subscribe": notify_on_subscribe,
                "notify_on_unsubscribe": notify_on_unsubscribe,
                "permission_reminder": permission_reminder,
                "use_archive_bar": use_archive_bar,
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
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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

    def list_abuse_reports(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListsAbuseReports, ListAbuseReportsListsResponse]:
        """
        Get all abuse reports for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListsAbuseReports, ListAbuseReportsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/abuse-reports",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAbuseReportsListsResponse,
                    parse_obj_as(
                        type_=ListAbuseReportsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.abuse_reports
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_abuse_reports(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
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

    def get_abuse_report(
        self,
        list_id: str,
        report_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListsAbuseReports]:
        """
        Get details about a specific abuse report.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        report_id : str
            The id for the abuse report.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListsAbuseReports]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/abuse-reports/{encode_path_param(report_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListsAbuseReports,
                    parse_obj_as(
                        type_=ListsAbuseReports,  # type: ignore
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

    def list_activity(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListActivityListsResponseActivityItem, ListActivityListsResponse]:
        """
        Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListActivityListsResponseActivityItem, ListActivityListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/activity",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListActivityListsResponse,
                    parse_obj_as(
                        type_=ListActivityListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.activity
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_activity(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
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

    def list_clients(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListClientsListsResponse]:
        """
        Get a list of the top email clients based on user-agent strings.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListClientsListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/clients",
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
                    ListClientsListsResponse,
                    parse_obj_as(
                        type_=ListClientsListsResponse,  # type: ignore
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

    def list_growth_history(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_field: typing.Optional[ListGrowthHistoryListsRequestSortField] = None,
        sort_dir: typing.Optional[ListGrowthHistoryListsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[GrowthHistory, ListGrowthHistoryListsResponse]:
        """
        Get a month-by-month summary of a specific list's growth activity.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        sort_field : typing.Optional[ListGrowthHistoryListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListGrowthHistoryListsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[GrowthHistory, ListGrowthHistoryListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/growth-history",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListGrowthHistoryListsResponse,
                    parse_obj_as(
                        type_=ListGrowthHistoryListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.history
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_growth_history(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    sort_field=sort_field,
                    sort_dir=sort_dir,
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

    def get_growth_history(
        self,
        list_id: str,
        month: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GrowthHistory]:
        """
        Get a summary of a specific list's growth activity for a specific month and year.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        month : str
            A specific month of list growth history.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GrowthHistory]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/growth-history/{encode_path_param(month)}",
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
                    GrowthHistory,
                    parse_obj_as(
                        type_=GrowthHistory,  # type: ignore
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

    def list_interest_categories(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        sort_field: typing.Optional[ListInterestCategoriesListsRequestSortField] = None,
        sort_dir: typing.Optional[ListInterestCategoriesListsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[InterestCategory, ListInterestCategoriesListsResponse]:
        """
        Get information about a list's interest categories.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            Restrict results a type of interest group

        sort_field : typing.Optional[ListInterestCategoriesListsRequestSortField]
            Returns interest categories sorted by the specified field. Defaults to display_order.

        sort_dir : typing.Optional[ListInterestCategoriesListsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[InterestCategory, ListInterestCategoriesListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListInterestCategoriesListsResponse,
                    parse_obj_as(
                        type_=ListInterestCategoriesListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.categories
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_interest_categories(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    type=type,
                    sort_field=sort_field,
                    sort_dir=sort_dir,
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

    def create_interest_category(
        self,
        list_id: str,
        *,
        title: str,
        type: CreateInterestCategoryListsRequestType,
        display_order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InterestCategory]:
        """
        Create a new interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        title : str
            The text description of this category. This field appears on signup forms and is often phrased as a question.

        type : CreateInterestCategoryListsRequestType
            Determines how this category’s interests appear on signup forms.

        display_order : typing.Optional[int]
            The order that the categories are displayed in the list. Lower numbers display first.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InterestCategory]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories",
            method="POST",
            json={
                "display_order": display_order,
                "title": title,
                "type": type,
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    def get_interest_category(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InterestCategory]:
        """
        Get information about a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InterestCategory]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    def delete_interest_category(
        self, list_id: str, interest_category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
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

    def update_interest_category(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        display_order: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[UpdateInterestCategoryListsRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InterestCategory]:
        """
        Update a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        display_order : typing.Optional[int]
            The order that the categories are displayed in the list. Lower numbers display first.

        title : typing.Optional[str]
            The text description of this category. This field appears on signup forms and is often phrased as a question.

        type : typing.Optional[UpdateInterestCategoryListsRequestType]
            Determines how this category’s interests appear on signup forms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InterestCategory]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
            method="PATCH",
            json={
                "display_order": display_order,
                "title": title,
                "type": type,
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    def list_interest_category_interests(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Interest, ListInterestCategoryInterestsListsResponse]:
        """
        Get a list of this category's interests.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Interest, ListInterestCategoryInterestsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListInterestCategoryInterestsListsResponse,
                    parse_obj_as(
                        type_=ListInterestCategoryInterestsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.interests
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_interest_category_interests(
                    list_id,
                    interest_category_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
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

    def create_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        name: str,
        display_order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Interest]:
        """
        Create a new interest or 'group name' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        name : str
            The name of the interest. This can be shown publicly on a subscription form.

        display_order : typing.Optional[int]
            The display order for interests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Interest]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests",
            method="POST",
            json={
                "display_order": display_order,
                "name": name,
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    def get_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Interest]:
        """
        Get interests or 'group names' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Interest]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    def delete_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete interests or group names in a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
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

    def update_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        display_order: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Interest]:
        """
        Update interests or 'group names' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        display_order : typing.Optional[int]
            The display order for interests.

        name : typing.Optional[str]
            The name of the interest. This can be shown publicly on a subscription form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Interest]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
            method="PATCH",
            json={
                "display_order": display_order,
                "name": name,
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    def list_locations(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListLocationsListsResponse]:
        """
        Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListLocationsListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/locations",
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
                    ListLocationsListsResponse,
                    parse_obj_as(
                        type_=ListLocationsListsResponse,  # type: ignore
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

    def list_members(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        email_type: typing.Optional[str] = None,
        status: typing.Optional[ListMembersListsRequestStatus] = None,
        since_timestamp_opt: typing.Optional[str] = None,
        before_timestamp_opt: typing.Optional[str] = None,
        since_last_changed: typing.Optional[str] = None,
        before_last_changed: typing.Optional[str] = None,
        unique_email_id: typing.Optional[str] = None,
        vip_only: typing.Optional[bool] = None,
        interest_category_id: typing.Optional[str] = None,
        interest_ids: typing.Optional[str] = None,
        interest_match: typing.Optional[ListMembersListsRequestInterestMatch] = None,
        sort_field: typing.Optional[ListMembersListsRequestSortField] = None,
        sort_dir: typing.Optional[ListMembersListsRequestSortDir] = None,
        since_last_campaign: typing.Optional[bool] = None,
        unsubscribed_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListMembers, ListMembersListsResponse]:
        """
        Get information about members in a specific Mailchimp list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        email_type : typing.Optional[str]
            The email type.

        status : typing.Optional[ListMembersListsRequestStatus]
            The subscriber's status.

        since_timestamp_opt : typing.Optional[str]
            Restrict results to subscribers who opted-in after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_timestamp_opt : typing.Optional[str]
            Restrict results to subscribers who opted-in before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_last_changed : typing.Optional[str]
            Restrict results to subscribers whose information changed after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_last_changed : typing.Optional[str]
            Restrict results to subscribers whose information changed before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        unique_email_id : typing.Optional[str]
            A unique identifier for the email address across all Mailchimp lists.

        vip_only : typing.Optional[bool]
            A filter to return only the list's VIP members. Passing `true` will restrict results to VIP list members, passing `false` will return all list members.

        interest_category_id : typing.Optional[str]
            The unique id for the interest category.

        interest_ids : typing.Optional[str]
            Used to filter list members by interests. Must be accompanied by interest_category_id and interest_match. The value must be a comma separated list of interest ids present for any supplied interest categories.

        interest_match : typing.Optional[ListMembersListsRequestInterestMatch]
            Used to filter list members by interests. Must be accompanied by interest_category_id and interest_ids. "any" will match a member with any of the interest supplied, "all" will only match members with every interest supplied, and "none" will match members without any of the interest supplied.

        sort_field : typing.Optional[ListMembersListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListMembersListsRequestSortDir]
            Determines the order direction for sorted results.

        since_last_campaign : typing.Optional[bool]
            Filter subscribers by those subscribed/unsubscribed/pending/cleaned since last email campaign send. Member status is required to use this filter.

        unsubscribed_since : typing.Optional[str]
            Filter subscribers by those unsubscribed since a specific date. Using any status other than unsubscribed with this filter will result in an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListMembers, ListMembersListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "email_type": email_type,
                "status": status,
                "since_timestamp_opt": since_timestamp_opt,
                "before_timestamp_opt": before_timestamp_opt,
                "since_last_changed": since_last_changed,
                "before_last_changed": before_last_changed,
                "unique_email_id": unique_email_id,
                "vip_only": vip_only,
                "interest_category_id": interest_category_id,
                "interest_ids": interest_ids,
                "interest_match": interest_match,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "since_last_campaign": since_last_campaign,
                "unsubscribed_since": unsubscribed_since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMembersListsResponse,
                    parse_obj_as(
                        type_=ListMembersListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.members
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_members(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    email_type=email_type,
                    status=status,
                    since_timestamp_opt=since_timestamp_opt,
                    before_timestamp_opt=before_timestamp_opt,
                    since_last_changed=since_last_changed,
                    before_last_changed=before_last_changed,
                    unique_email_id=unique_email_id,
                    vip_only=vip_only,
                    interest_category_id=interest_category_id,
                    interest_ids=interest_ids,
                    interest_match=interest_match,
                    sort_field=sort_field,
                    sort_dir=sort_dir,
                    since_last_campaign=since_last_campaign,
                    unsubscribed_since=unsubscribed_since,
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

    def create_member(
        self,
        list_id: str,
        *,
        email_address: str,
        status: CreateMemberListsRequestStatus,
        skip_merge_validation: typing.Optional[bool] = None,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[CreateMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, CreateMemberListsRequestMergeFieldsValue]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        timestamp_opt: typing.Optional[CreateMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[CreateMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMembers]:
        """
        Add a new member to the list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        email_address : str
            Email address for a subscriber.

        status : CreateMemberListsRequestStatus
            Subscriber's current status.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[CreateMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, CreateMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        tags : typing.Optional[typing.Sequence[str]]
            The tags that are associated with a member.

        timestamp_opt : typing.Optional[CreateMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[CreateMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMembers]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members",
            method="POST",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, CreateMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "tags": tags,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=CreateMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=CreateMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    def get_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMembers]:
        """
        Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMembers]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    def upsert_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        email_address: str,
        skip_merge_validation: typing.Optional[bool] = None,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[UpsertMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue]] = OMIT,
        status: typing.Optional[UpsertMemberListsRequestStatus] = OMIT,
        status_if_new: typing.Optional[UpsertMemberListsRequestStatusIfNew] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        timestamp_opt: typing.Optional[UpsertMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[UpsertMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMembers]:
        """
        Add or update a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        email_address : str
            Email address for a subscriber. This value is required only if the email address is not already present on the list.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[UpsertMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        status : typing.Optional[UpsertMemberListsRequestStatus]
            Subscriber's current status.

        status_if_new : typing.Optional[UpsertMemberListsRequestStatusIfNew]
            Subscriber's status. This value is required only if the email address is not already present on the list.

        tags : typing.Optional[typing.Sequence[str]]
            The tags that are associated with a member.

        timestamp_opt : typing.Optional[UpsertMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[UpsertMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMembers]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
            method="PUT",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=UpsertMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "status_if_new": status_if_new,
                "tags": tags,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=UpsertMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=UpsertMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    def delete_member(
        self, list_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Archive a list member. To permanently delete, use the delete-permanent action.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
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

    def update_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        skip_merge_validation: typing.Optional[bool] = None,
        email_address: typing.Optional[str] = OMIT,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[UpdateMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue]] = OMIT,
        status: typing.Optional[UpdateMemberListsRequestStatus] = OMIT,
        timestamp_opt: typing.Optional[UpdateMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[UpdateMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMembers]:
        """
        Update information for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_address : typing.Optional[str]
            Email address for a subscriber.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[UpdateMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        status : typing.Optional[UpdateMemberListsRequestStatus]
            Subscriber's current status.

        timestamp_opt : typing.Optional[UpdateMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[UpdateMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMembers]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
            method="PATCH",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=UpdateMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=UpdateMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=UpdateMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    def create_member_action_delete_permanent(
        self, list_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete all personally identifiable information related to a list member, and remove them from a list. This will make it impossible to re-import the list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/actions/delete-permanent",
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

    def list_member_activity(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        action: typing.Optional[
            typing.Union[
                ListMemberActivityListsRequestActionItem, typing.Sequence[ListMemberActivityListsRequestActionItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMemberActivityListsResponse]:
        """
        Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        action : typing.Optional[typing.Union[ListMemberActivityListsRequestActionItem, typing.Sequence[ListMemberActivityListsRequestActionItem]]]
            A comma seperated list of actions to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMemberActivityListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/activity",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "action": ",".join(map(str, action)) if isinstance(action, (list, tuple, set)) else action,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMemberActivityListsResponse,
                    parse_obj_as(
                        type_=ListMemberActivityListsResponse,  # type: ignore
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

    def list_member_activity_feed(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        activity_filters: typing.Optional[
            typing.Union[
                ListMemberActivityFeedListsRequestActivityFiltersItem,
                typing.Sequence[ListMemberActivityFeedListsRequestActivityFiltersItem],
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[typing.Any, ListMemberActivityFeedListsResponse]:
        """
        Get a member's activity on a specific list, including opens, clicks, and unsubscribes.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        activity_filters : typing.Optional[typing.Union[ListMemberActivityFeedListsRequestActivityFiltersItem, typing.Sequence[ListMemberActivityFeedListsRequestActivityFiltersItem]]]
            A comma-separated list of activity filters that correspond to a set of activity types, e.g "?activity_filters=open,bounce,click".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[typing.Any, ListMemberActivityFeedListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/activity-feed",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "activity_filters": ",".join(map(str, activity_filters))
                if isinstance(activity_filters, (list, tuple, set))
                else activity_filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberActivityFeedListsResponse,
                    parse_obj_as(
                        type_=ListMemberActivityFeedListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.activity
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_member_activity_feed(
                    list_id,
                    subscriber_hash,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    activity_filters=activity_filters,
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

    def list_member_events(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListMemberEventsListsResponseEventsItem, ListMemberEventsListsResponse]:
        """
        Get events for a contact.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListMemberEventsListsResponseEventsItem, ListMemberEventsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/events",
            method="GET",
            params={
                "count": count,
                "offset": offset,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberEventsListsResponse,
                    parse_obj_as(
                        type_=ListMemberEventsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.events
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_member_events(
                    list_id,
                    subscriber_hash,
                    count=count,
                    offset=offset + 1,
                    fields=fields,
                    exclude_fields=exclude_fields,
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

    def create_member_event(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        name: str,
        is_syncing: typing.Optional[bool] = OMIT,
        occurred_at: typing.Optional[dt.datetime] = OMIT,
        properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Add an event for a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        name : str
            The name for this type of event ('purchased', 'visited', etc). Must be 2-30 characters in length

        is_syncing : typing.Optional[bool]
            Events created with the is_syncing value set to `true` will not trigger automations.

        occurred_at : typing.Optional[dt.datetime]
            The date and time the event occurred in ISO 8601 format.

        properties : typing.Optional[typing.Dict[str, str]]
            An optional list of properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/events",
            method="POST",
            json={
                "is_syncing": is_syncing,
                "name": name,
                "occurred_at": occurred_at,
                "properties": properties,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def list_member_goals(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMemberGoalsListsResponse]:
        """
        Get the last 50 Goal events for a member on a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMemberGoalsListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/goals",
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
                    ListMemberGoalsListsResponse,
                    parse_obj_as(
                        type_=ListMemberGoalsListsResponse,  # type: ignore
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

    def list_member_notes(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        sort_field: typing.Optional[ListMemberNotesListsRequestSortField] = None,
        sort_dir: typing.Optional[ListMemberNotesListsRequestSortDir] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[MemberNotes, ListMemberNotesListsResponse]:
        """
        Get recent notes for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        sort_field : typing.Optional[ListMemberNotesListsRequestSortField]
            Returns notes sorted by the specified field.

        sort_dir : typing.Optional[ListMemberNotesListsRequestSortDir]
            Determines the order direction for sorted results.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[MemberNotes, ListMemberNotesListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes",
            method="GET",
            params={
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberNotesListsResponse,
                    parse_obj_as(
                        type_=ListMemberNotesListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.notes
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_member_notes(
                    list_id,
                    subscriber_hash,
                    sort_field=sort_field,
                    sort_dir=sort_dir,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
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

    def create_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberNotes]:
        """
        Add a new note for a specific subscriber.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        note : typing.Optional[str]
            The content of the note. Note length is limited to 1,000 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberNotes]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes",
            method="POST",
            json={
                "note": note,
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    def get_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberNotes]:
        """
        Get a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberNotes]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    def delete_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
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

    def update_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberNotes]:
        """
        Update a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        note : typing.Optional[str]
            The content of the note. Note length is limited to 1,000 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberNotes]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
            method="PATCH",
            json={
                "note": note,
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    def list_member_tags(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListMemberTagsListsResponseTagsItem, ListMemberTagsListsResponse]:
        """
        Get the tags on a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListMemberTagsListsResponseTagsItem, ListMemberTagsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/tags",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberTagsListsResponse,
                    parse_obj_as(
                        type_=ListMemberTagsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.tags
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_member_tags(
                    list_id,
                    subscriber_hash,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
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

    def create_member_tag(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        tags: typing.Sequence[CreateMemberTagListsRequestTagsItem],
        is_syncing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Add or remove tags from a list member. If a tag that does not exist is passed in and set as 'active', a new tag will be created.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        tags : typing.Sequence[CreateMemberTagListsRequestTagsItem]
            A list of tags assigned to the list member.

        is_syncing : typing.Optional[bool]
            When is_syncing is true, automations based on the tags in the request will not fire

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/tags",
            method="POST",
            json={
                "is_syncing": is_syncing,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CreateMemberTagListsRequestTagsItem], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_merge_fields(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[MergeField, ListMergeFieldsListsResponse]:
        """
        Get a list of all merge fields for an audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            The merge field type.

        required : typing.Optional[bool]
            Whether it's a required merge field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[MergeField, ListMergeFieldsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "required": required,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMergeFieldsListsResponse,
                    parse_obj_as(
                        type_=ListMergeFieldsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.merge_fields
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_merge_fields(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    type=type,
                    required=required,
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

    def create_merge_field(
        self,
        list_id: str,
        *,
        name: str,
        type: CreateMergeFieldListsRequestType,
        default_value: typing.Optional[str] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        help_text: typing.Optional[str] = OMIT,
        options: typing.Optional[CreateMergeFieldListsRequestOptions] = OMIT,
        public: typing.Optional[bool] = OMIT,
        required: typing.Optional[bool] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MergeField]:
        """
        Add a new merge field for a specific audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : str
            The name of the merge field (audience field).

        type : CreateMergeFieldListsRequestType
            The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.

        default_value : typing.Optional[str]
            The default value for the merge field if `null`.

        display_order : typing.Optional[int]
            The order that the merge field displays on the list signup form.

        help_text : typing.Optional[str]
            Extra text to help the subscriber fill out the form.

        options : typing.Optional[CreateMergeFieldListsRequestOptions]
            Extra options for some merge field types.

        public : typing.Optional[bool]
            Whether the merge field is displayed on the signup form.

        required : typing.Optional[bool]
            Whether the merge field is required to import a contact.

        tag : typing.Optional[str]
            The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MergeField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields",
            method="POST",
            json={
                "default_value": default_value,
                "display_order": display_order,
                "help_text": help_text,
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=CreateMergeFieldListsRequestOptions, direction="write"
                ),
                "public": public,
                "required": required,
                "tag": tag,
                "type": type,
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
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    def get_merge_field(
        self,
        list_id: str,
        merge_id: str,
        *,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MergeField]:
        """
        Get information about a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MergeField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
            method="GET",
            params={
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    def delete_merge_field(
        self, list_id: str, merge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
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

    def update_merge_field(
        self,
        list_id: str,
        merge_id: str,
        *,
        default_value: typing.Optional[str] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        help_text: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[UpdateMergeFieldListsRequestOptions] = OMIT,
        public: typing.Optional[bool] = OMIT,
        required: typing.Optional[bool] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MergeField]:
        """
        Update a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        default_value : typing.Optional[str]
            The default value for the merge field if `null`.

        display_order : typing.Optional[int]
            The order that the merge field displays on the list signup form.

        help_text : typing.Optional[str]
            Extra text to help the subscriber fill out the form.

        name : typing.Optional[str]
            The name of the merge field (audience field).

        options : typing.Optional[UpdateMergeFieldListsRequestOptions]
            Extra options for some merge field types.

        public : typing.Optional[bool]
            Whether the merge field is displayed on the signup form.

        required : typing.Optional[bool]
            Whether the merge field is required to import a contact.

        tag : typing.Optional[str]
            The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MergeField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
            method="PATCH",
            json={
                "default_value": default_value,
                "display_order": display_order,
                "help_text": help_text,
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=UpdateMergeFieldListsRequestOptions, direction="write"
                ),
                "public": public,
                "required": required,
                "tag": tag,
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
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    def list_segments(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        since_updated_at: typing.Optional[str] = None,
        before_updated_at: typing.Optional[str] = None,
        exclude_type: typing.Optional[ListSegmentsListsRequestExcludeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[List, ListSegmentsListsResponse]:
        """
        Get information about all available segments for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            Limit results based on segment type.

        since_created_at : typing.Optional[str]
            Restrict results to segments created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_created_at : typing.Optional[str]
            Restrict results to segments created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        since_updated_at : typing.Optional[str]
            Restrict results to segments update after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_updated_at : typing.Optional[str]
            Restrict results to segments update before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        exclude_type : typing.Optional[ListSegmentsListsRequestExcludeType]
            Exclude results based on segment type. For example, use `exclude_type=static` to exclude tags from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[List, ListSegmentsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "since_created_at": since_created_at,
                "before_created_at": before_created_at,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
                "since_updated_at": since_updated_at,
                "before_updated_at": before_updated_at,
                "exclude_type": exclude_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListSegmentsListsResponse,
                    parse_obj_as(
                        type_=ListSegmentsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.segments
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_segments(
                    list_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    type=type,
                    since_created_at=since_created_at,
                    before_created_at=before_created_at,
                    include_cleaned=include_cleaned,
                    include_transactional=include_transactional,
                    include_unsubscribed=include_unsubscribed,
                    since_updated_at=since_updated_at,
                    before_updated_at=before_updated_at,
                    exclude_type=exclude_type,
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

    def create_segment(
        self,
        list_id: str,
        *,
        name: str,
        options: typing.Optional[CreateSegmentListsRequestOptions] = OMIT,
        static_segment: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[List]:
        """
        Create a new segment in a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : str
            The name of the segment.

        options : typing.Optional[CreateSegmentListsRequestOptions]
            The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.

        static_segment : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array will create a static segment without any subscribers. This field cannot be provided with the options field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[List]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments",
            method="POST",
            json={
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=CreateSegmentListsRequestOptions, direction="write"
                ),
                "static_segment": static_segment,
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
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    def get_segment(
        self,
        list_id: str,
        segment_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[List]:
        """
        Get information about a specific segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[List]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    def batch_add_or_remove_members(
        self,
        list_id: str,
        segment_id: str,
        *,
        members_to_add: typing.Optional[typing.Sequence[str]] = OMIT,
        members_to_remove: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchAddOrRemoveMembersListsResponse]:
        """
        Batch add/remove list members to static segment

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        members_to_add : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.

        members_to_remove : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchAddOrRemoveMembersListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="POST",
            json={
                "members_to_add": members_to_add,
                "members_to_remove": members_to_remove,
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
                    BatchAddOrRemoveMembersListsResponse,
                    parse_obj_as(
                        type_=BatchAddOrRemoveMembersListsResponse,  # type: ignore
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

    def delete_segment(
        self, list_id: str, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific segment in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
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

    def update_segment(
        self,
        list_id: str,
        segment_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[UpdateSegmentListsRequestOptions] = OMIT,
        static_segment: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[List]:
        """
        Update a specific segment in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        name : typing.Optional[str]
            The name of the segment.

        options : typing.Optional[UpdateSegmentListsRequestOptions]
            The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.

        static_segment : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array for an existing static segment will reset that segment and remove all members. This field cannot be provided with the `options` field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[List]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="PATCH",
            json={
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=UpdateSegmentListsRequestOptions, direction="write"
                ),
                "static_segment": static_segment,
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
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    def list_segment_members(
        self,
        list_id: str,
        segment_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListsSegmentsMembers, ListSegmentMembersListsResponse]:
        """
        Get information about members in a saved segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListsSegmentsMembers, ListSegmentMembersListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListSegmentMembersListsResponse,
                    parse_obj_as(
                        type_=ListSegmentMembersListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.members
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_segment_members(
                    list_id,
                    segment_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    include_cleaned=include_cleaned,
                    include_transactional=include_transactional,
                    include_unsubscribed=include_unsubscribed,
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

    def create_segment_member(
        self,
        list_id: str,
        segment_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListsSegmentsMembers]:
        """
        Add a member to a static segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        email_address : str
            Email address for a subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListsSegmentsMembers]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members",
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
                    ListsSegmentsMembers,
                    parse_obj_as(
                        type_=ListsSegmentsMembers,  # type: ignore
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

    def delete_segment_member(
        self,
        list_id: str,
        segment_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Remove a member from the specified static segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members/{encode_path_param(subscriber_hash)}",
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

    def list_signup_forms(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListSignupFormsListsResponse]:
        """
        Get signup forms for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSignupFormsListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/signup-forms",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSignupFormsListsResponse,
                    parse_obj_as(
                        type_=ListSignupFormsListsResponse,  # type: ignore
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

    def create_signup_form(
        self,
        list_id: str,
        *,
        contents: typing.Optional[typing.Sequence[CreateSignupFormListsRequestContentsItem]] = OMIT,
        header: typing.Optional[CreateSignupFormListsRequestHeader] = OMIT,
        styles: typing.Optional[typing.Sequence[CreateSignupFormListsRequestStylesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SignupForm]:
        """
        Customize a list's default signup form.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        contents : typing.Optional[typing.Sequence[CreateSignupFormListsRequestContentsItem]]
            The signup form body content.

        header : typing.Optional[CreateSignupFormListsRequestHeader]
            Options for customizing your signup form header.

        styles : typing.Optional[typing.Sequence[CreateSignupFormListsRequestStylesItem]]
            An array of objects, each representing an element style for the signup form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignupForm]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/signup-forms",
            method="POST",
            json={
                "contents": convert_and_respect_annotation_metadata(
                    object_=contents,
                    annotation=typing.Sequence[CreateSignupFormListsRequestContentsItem],
                    direction="write",
                ),
                "header": convert_and_respect_annotation_metadata(
                    object_=header, annotation=CreateSignupFormListsRequestHeader, direction="write"
                ),
                "styles": convert_and_respect_annotation_metadata(
                    object_=styles,
                    annotation=typing.Sequence[CreateSignupFormListsRequestStylesItem],
                    direction="write",
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
                    SignupForm,
                    parse_obj_as(
                        type_=SignupForm,  # type: ignore
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

    def list_surveys(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Get information about all available surveys for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    def create_survey(
        self,
        list_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        sections: typing.Optional[typing.Sequence[SurveySectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Create a draft survey for an audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        title : typing.Optional[str]
            The title of the survey.

        sections : typing.Optional[typing.Sequence[SurveySectionRequest]]
            Initial survey sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Survey created.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys",
            method="POST",
            json={
                "title": title,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections, annotation=typing.Sequence[SurveySectionRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    def get_survey(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Get details about a specific survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    def delete_survey(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
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

    def update_survey(
        self,
        list_id: str,
        survey_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        is_piped_to_inbox: typing.Optional[bool] = OMIT,
        sections: typing.Optional[typing.Sequence[SurveySectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Update a survey. When sections is provided, send the complete section list in display order. Any existing section not included is deleted.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        title : typing.Optional[str]
            The title of the survey.

        is_piped_to_inbox : typing.Optional[bool]
            Whether responses are sent to Mailchimp Inbox.

        sections : typing.Optional[typing.Sequence[SurveySectionRequest]]
            The complete survey section list in display order. On update, sections omitted from this array are deleted. Include section id to update an existing section; omit section id to add a new section.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Survey updated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
            method="PATCH",
            json={
                "title": title,
                "is_piped_to_inbox": is_piped_to_inbox,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections, annotation=typing.Sequence[SurveySectionRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    def create_list_survey_action_replicate(
        self,
        list_id_path_param: str,
        survey_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Replicate a survey.

        Parameters
        ----------
        list_id_path_param : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        title : typing.Optional[str]
            The title for the replicated survey.

        list_id : typing.Optional[str]
            The unique ID of the audience for the replicated survey. Defaults to the source survey audience.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Survey replicated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id_path_param)}/surveys/{encode_path_param(survey_id)}/actions/replicate",
            method="POST",
            json={
                "title": title,
                "list_id": list_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    def list_tag_search(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTagSearchListsResponse]:
        """
        Search for tags on a list by name. If no name is provided, will return all tags on the list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : typing.Optional[str]
            The search query used to filter tags.  The search query will be compared to each tag as a prefix, so all tags that have a name starting with this field will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTagSearchListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/tag-search",
            method="GET",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTagSearchListsResponse,
                    parse_obj_as(
                        type_=ListTagSearchListsResponse,  # type: ignore
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

    def list_webhooks(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListWebhooksListsResponse]:
        """
        Get information about all webhooks for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhooksListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksListsResponse,
                    parse_obj_as(
                        type_=ListWebhooksListsResponse,  # type: ignore
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

    def create_webhook(
        self,
        list_id: str,
        *,
        events: typing.Optional[AddWebhookEvents] = OMIT,
        sources: typing.Optional[AddWebhookSources] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateWebhookListsResponse]:
        """
        Create a new webhook for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        events : typing.Optional[AddWebhookEvents]
            The events that can trigger the webhook and whether they are enabled.

        sources : typing.Optional[AddWebhookSources]
            The possible sources of any events that can trigger the webhook and whether they are enabled.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateWebhookListsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=AddWebhookEvents, direction="write"
                ),
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=AddWebhookSources, direction="write"
                ),
                "url": url,
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
                    CreateWebhookListsResponse,
                    parse_obj_as(
                        type_=CreateWebhookListsResponse,  # type: ignore
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

    def get_webhook(
        self, list_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListWebhooks]:
        """
        Get information about a specific webhook.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhooks]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooks,
                    parse_obj_as(
                        type_=ListWebhooks,  # type: ignore
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

    def delete_webhook(
        self, list_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific webhook in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
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

    def update_webhook(
        self,
        list_id: str,
        webhook_id: str,
        *,
        events: typing.Optional[AddWebhookEvents] = OMIT,
        sources: typing.Optional[AddWebhookSources] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWebhooks]:
        """
        Update the settings for an existing webhook.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        events : typing.Optional[AddWebhookEvents]
            The events that can trigger the webhook and whether they are enabled.

        sources : typing.Optional[AddWebhookSources]
            The possible sources of any events that can trigger the webhook and whether they are enabled.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhooks]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=AddWebhookEvents, direction="write"
                ),
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=AddWebhookSources, direction="write"
                ),
                "url": url,
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
                    ListWebhooks,
                    parse_obj_as(
                        type_=ListWebhooks,  # type: ignore
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


class AsyncRawListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        before_date_created: typing.Optional[str] = None,
        since_date_created: typing.Optional[str] = None,
        before_campaign_last_sent: typing.Optional[str] = None,
        since_campaign_last_sent: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        sort_field: typing.Optional[ListListsRequestSortField] = None,
        sort_dir: typing.Optional[ListListsRequestSortDir] = None,
        has_ecommerce_store: typing.Optional[bool] = None,
        include_total_contacts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[SubscriberList, ListListsResponse]:
        """
        Get information about all lists in the account.

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

        before_date_created : typing.Optional[str]
            Restrict response to lists created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_date_created : typing.Optional[str]
            Restrict results to lists created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_campaign_last_sent : typing.Optional[str]
            Restrict results to lists created before the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_campaign_last_sent : typing.Optional[str]
            Restrict results to lists created after the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        email : typing.Optional[str]
            Restrict results to lists that include a specific subscriber's email address.

        sort_field : typing.Optional[ListListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListListsRequestSortDir]
            Determines the order direction for sorted results.

        has_ecommerce_store : typing.Optional[bool]
            Restrict results to lists that contain an active, connected, undeleted ecommerce store.

        include_total_contacts : typing.Optional[bool]
            Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[SubscriberList, ListListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/lists",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "before_date_created": before_date_created,
                "since_date_created": since_date_created,
                "before_campaign_last_sent": before_campaign_last_sent,
                "since_campaign_last_sent": since_campaign_last_sent,
                "email": email,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "has_ecommerce_store": has_ecommerce_store,
                "include_total_contacts": include_total_contacts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListListsResponse,
                    parse_obj_as(
                        type_=ListListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.lists
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list(
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        before_date_created=before_date_created,
                        since_date_created=since_date_created,
                        before_campaign_last_sent=before_campaign_last_sent,
                        since_campaign_last_sent=since_campaign_last_sent,
                        email=email,
                        sort_field=sort_field,
                        sort_dir=sort_dir,
                        has_ecommerce_store=has_ecommerce_store,
                        include_total_contacts=include_total_contacts,
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
        campaign_defaults: CreateListsRequestCampaignDefaults,
        contact: CreateListsRequestContact,
        email_type_option: bool,
        name: str,
        permission_reminder: str,
        double_optin: typing.Optional[bool] = OMIT,
        marketing_permissions: typing.Optional[bool] = OMIT,
        notify_on_subscribe: typing.Optional[str] = OMIT,
        notify_on_unsubscribe: typing.Optional[str] = OMIT,
        use_archive_bar: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriberList]:
        """
        Create a new list in your Mailchimp account.

        Parameters
        ----------
        campaign_defaults : CreateListsRequestCampaignDefaults
            [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.

        contact : CreateListsRequestContact
            [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.

        email_type_option : bool
            Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.

        name : str
            The name of the list.

        permission_reminder : str
            The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.

        double_optin : typing.Optional[bool]
            Whether or not to require the subscriber to confirm subscription via email.

        marketing_permissions : typing.Optional[bool]
            Whether or not the list has marketing permissions (eg. GDPR) enabled.

        notify_on_subscribe : typing.Optional[str]
            The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        notify_on_unsubscribe : typing.Optional[str]
            The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        use_archive_bar : typing.Optional[bool]
            Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriberList]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/lists",
            method="POST",
            json={
                "campaign_defaults": convert_and_respect_annotation_metadata(
                    object_=campaign_defaults, annotation=CreateListsRequestCampaignDefaults, direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=CreateListsRequestContact, direction="write"
                ),
                "double_optin": double_optin,
                "email_type_option": email_type_option,
                "marketing_permissions": marketing_permissions,
                "name": name,
                "notify_on_subscribe": notify_on_subscribe,
                "notify_on_unsubscribe": notify_on_unsubscribe,
                "permission_reminder": permission_reminder,
                "use_archive_bar": use_archive_bar,
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
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_total_contacts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriberList]:
        """
        Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_total_contacts : typing.Optional[bool]
            Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriberList]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "include_total_contacts": include_total_contacts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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

    async def batch_subscribe_or_unsubscribe(
        self,
        list_id: str,
        *,
        members: typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem],
        skip_merge_validation: typing.Optional[bool] = None,
        skip_duplicate_check: typing.Optional[bool] = None,
        sync_tags: typing.Optional[bool] = OMIT,
        update_existing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchSubscribeOrUnsubscribeListsResponse]:
        """
        Batch subscribe or unsubscribe list members.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        members : typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem]
            An array of objects, each representing an email address and the subscription status for a specific list. Up to 500 members may be added or updated with each API call.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        skip_duplicate_check : typing.Optional[bool]
            If skip_duplicate_check is true, we will ignore duplicates sent in the request when using the batch sub/unsub on the lists endpoint. The status of the first appearance in the request will be saved. This defaults to false.

        sync_tags : typing.Optional[bool]
            Whether this batch operation will replace all existing tags with tags in request.

        update_existing : typing.Optional[bool]
            Whether this batch operation will change existing members' subscription status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchSubscribeOrUnsubscribeListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="POST",
            params={
                "skip_merge_validation": skip_merge_validation,
                "skip_duplicate_check": skip_duplicate_check,
            },
            json={
                "members": convert_and_respect_annotation_metadata(
                    object_=members,
                    annotation=typing.Sequence[BatchSubscribeOrUnsubscribeListsRequestMembersItem],
                    direction="write",
                ),
                "sync_tags": sync_tags,
                "update_existing": update_existing,
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
                    BatchSubscribeOrUnsubscribeListsResponse,
                    parse_obj_as(
                        type_=BatchSubscribeOrUnsubscribeListsResponse,  # type: ignore
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

    async def delete(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a list from your Mailchimp account. If you delete a list, you'll lose the list history—including subscriber activity, unsubscribes, complaints, and bounces. You’ll also lose subscribers’ email addresses, unless you exported and backed up your list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
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

    async def update(
        self,
        list_id: str,
        *,
        campaign_defaults: typing.Optional[UpdateListsRequestCampaignDefaults] = OMIT,
        contact: typing.Optional[UpdateListsRequestContact] = OMIT,
        double_optin: typing.Optional[bool] = OMIT,
        email_type_option: typing.Optional[bool] = OMIT,
        marketing_permissions: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        notify_on_subscribe: typing.Optional[str] = OMIT,
        notify_on_unsubscribe: typing.Optional[str] = OMIT,
        permission_reminder: typing.Optional[str] = OMIT,
        use_archive_bar: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriberList]:
        """
        Update the settings for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        campaign_defaults : typing.Optional[UpdateListsRequestCampaignDefaults]
            [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.

        contact : typing.Optional[UpdateListsRequestContact]
            [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.

        double_optin : typing.Optional[bool]
            Whether or not to require the subscriber to confirm subscription via email.

        email_type_option : typing.Optional[bool]
            Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.

        marketing_permissions : typing.Optional[bool]
            Whether or not the list has marketing permissions (eg. GDPR) enabled.

        name : typing.Optional[str]
            The name of the list.

        notify_on_subscribe : typing.Optional[str]
            The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        notify_on_unsubscribe : typing.Optional[str]
            The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.

        permission_reminder : typing.Optional[str]
            The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.

        use_archive_bar : typing.Optional[bool]
            Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriberList]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}",
            method="PATCH",
            json={
                "campaign_defaults": convert_and_respect_annotation_metadata(
                    object_=campaign_defaults, annotation=UpdateListsRequestCampaignDefaults, direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=UpdateListsRequestContact, direction="write"
                ),
                "double_optin": double_optin,
                "email_type_option": email_type_option,
                "marketing_permissions": marketing_permissions,
                "name": name,
                "notify_on_subscribe": notify_on_subscribe,
                "notify_on_unsubscribe": notify_on_unsubscribe,
                "permission_reminder": permission_reminder,
                "use_archive_bar": use_archive_bar,
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
                    SubscriberList,
                    parse_obj_as(
                        type_=SubscriberList,  # type: ignore
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

    async def list_abuse_reports(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListsAbuseReports, ListAbuseReportsListsResponse]:
        """
        Get all abuse reports for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListsAbuseReports, ListAbuseReportsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/abuse-reports",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAbuseReportsListsResponse,
                    parse_obj_as(
                        type_=ListAbuseReportsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.abuse_reports
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_abuse_reports(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
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

    async def get_abuse_report(
        self,
        list_id: str,
        report_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListsAbuseReports]:
        """
        Get details about a specific abuse report.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        report_id : str
            The id for the abuse report.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListsAbuseReports]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/abuse-reports/{encode_path_param(report_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListsAbuseReports,
                    parse_obj_as(
                        type_=ListsAbuseReports,  # type: ignore
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

    async def list_activity(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListActivityListsResponseActivityItem, ListActivityListsResponse]:
        """
        Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListActivityListsResponseActivityItem, ListActivityListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/activity",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListActivityListsResponse,
                    parse_obj_as(
                        type_=ListActivityListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.activity
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_activity(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
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

    async def list_clients(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListClientsListsResponse]:
        """
        Get a list of the top email clients based on user-agent strings.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListClientsListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/clients",
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
                    ListClientsListsResponse,
                    parse_obj_as(
                        type_=ListClientsListsResponse,  # type: ignore
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

    async def list_growth_history(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_field: typing.Optional[ListGrowthHistoryListsRequestSortField] = None,
        sort_dir: typing.Optional[ListGrowthHistoryListsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[GrowthHistory, ListGrowthHistoryListsResponse]:
        """
        Get a month-by-month summary of a specific list's growth activity.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        sort_field : typing.Optional[ListGrowthHistoryListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListGrowthHistoryListsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[GrowthHistory, ListGrowthHistoryListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/growth-history",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListGrowthHistoryListsResponse,
                    parse_obj_as(
                        type_=ListGrowthHistoryListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.history
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_growth_history(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        sort_field=sort_field,
                        sort_dir=sort_dir,
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

    async def get_growth_history(
        self,
        list_id: str,
        month: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GrowthHistory]:
        """
        Get a summary of a specific list's growth activity for a specific month and year.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        month : str
            A specific month of list growth history.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GrowthHistory]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/growth-history/{encode_path_param(month)}",
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
                    GrowthHistory,
                    parse_obj_as(
                        type_=GrowthHistory,  # type: ignore
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

    async def list_interest_categories(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        sort_field: typing.Optional[ListInterestCategoriesListsRequestSortField] = None,
        sort_dir: typing.Optional[ListInterestCategoriesListsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[InterestCategory, ListInterestCategoriesListsResponse]:
        """
        Get information about a list's interest categories.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            Restrict results a type of interest group

        sort_field : typing.Optional[ListInterestCategoriesListsRequestSortField]
            Returns interest categories sorted by the specified field. Defaults to display_order.

        sort_dir : typing.Optional[ListInterestCategoriesListsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[InterestCategory, ListInterestCategoriesListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListInterestCategoriesListsResponse,
                    parse_obj_as(
                        type_=ListInterestCategoriesListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.categories
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_interest_categories(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        type=type,
                        sort_field=sort_field,
                        sort_dir=sort_dir,
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

    async def create_interest_category(
        self,
        list_id: str,
        *,
        title: str,
        type: CreateInterestCategoryListsRequestType,
        display_order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InterestCategory]:
        """
        Create a new interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        title : str
            The text description of this category. This field appears on signup forms and is often phrased as a question.

        type : CreateInterestCategoryListsRequestType
            Determines how this category’s interests appear on signup forms.

        display_order : typing.Optional[int]
            The order that the categories are displayed in the list. Lower numbers display first.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InterestCategory]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories",
            method="POST",
            json={
                "display_order": display_order,
                "title": title,
                "type": type,
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    async def get_interest_category(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InterestCategory]:
        """
        Get information about a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InterestCategory]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    async def delete_interest_category(
        self, list_id: str, interest_category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
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

    async def update_interest_category(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        display_order: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[UpdateInterestCategoryListsRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InterestCategory]:
        """
        Update a specific interest category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        display_order : typing.Optional[int]
            The order that the categories are displayed in the list. Lower numbers display first.

        title : typing.Optional[str]
            The text description of this category. This field appears on signup forms and is often phrased as a question.

        type : typing.Optional[UpdateInterestCategoryListsRequestType]
            Determines how this category’s interests appear on signup forms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InterestCategory]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}",
            method="PATCH",
            json={
                "display_order": display_order,
                "title": title,
                "type": type,
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
                    InterestCategory,
                    parse_obj_as(
                        type_=InterestCategory,  # type: ignore
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

    async def list_interest_category_interests(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Interest, ListInterestCategoryInterestsListsResponse]:
        """
        Get a list of this category's interests.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Interest, ListInterestCategoryInterestsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListInterestCategoryInterestsListsResponse,
                    parse_obj_as(
                        type_=ListInterestCategoryInterestsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.interests
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_interest_category_interests(
                        list_id,
                        interest_category_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
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

    async def create_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        *,
        name: str,
        display_order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Interest]:
        """
        Create a new interest or 'group name' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        name : str
            The name of the interest. This can be shown publicly on a subscription form.

        display_order : typing.Optional[int]
            The display order for interests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Interest]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests",
            method="POST",
            json={
                "display_order": display_order,
                "name": name,
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    async def get_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Interest]:
        """
        Get interests or 'group names' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Interest]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    async def delete_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete interests or group names in a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
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

    async def update_interest_category_interest(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        *,
        display_order: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Interest]:
        """
        Update interests or 'group names' for a specific category.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        interest_category_id : str
            The unique ID for the interest category.

        interest_id : str
            The specific interest or 'group name'.

        display_order : typing.Optional[int]
            The display order for interests.

        name : typing.Optional[str]
            The name of the interest. This can be shown publicly on a subscription form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Interest]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/interest-categories/{encode_path_param(interest_category_id)}/interests/{encode_path_param(interest_id)}",
            method="PATCH",
            json={
                "display_order": display_order,
                "name": name,
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
                    Interest,
                    parse_obj_as(
                        type_=Interest,  # type: ignore
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

    async def list_locations(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListLocationsListsResponse]:
        """
        Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListLocationsListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/locations",
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
                    ListLocationsListsResponse,
                    parse_obj_as(
                        type_=ListLocationsListsResponse,  # type: ignore
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

    async def list_members(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        email_type: typing.Optional[str] = None,
        status: typing.Optional[ListMembersListsRequestStatus] = None,
        since_timestamp_opt: typing.Optional[str] = None,
        before_timestamp_opt: typing.Optional[str] = None,
        since_last_changed: typing.Optional[str] = None,
        before_last_changed: typing.Optional[str] = None,
        unique_email_id: typing.Optional[str] = None,
        vip_only: typing.Optional[bool] = None,
        interest_category_id: typing.Optional[str] = None,
        interest_ids: typing.Optional[str] = None,
        interest_match: typing.Optional[ListMembersListsRequestInterestMatch] = None,
        sort_field: typing.Optional[ListMembersListsRequestSortField] = None,
        sort_dir: typing.Optional[ListMembersListsRequestSortDir] = None,
        since_last_campaign: typing.Optional[bool] = None,
        unsubscribed_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListMembers, ListMembersListsResponse]:
        """
        Get information about members in a specific Mailchimp list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        email_type : typing.Optional[str]
            The email type.

        status : typing.Optional[ListMembersListsRequestStatus]
            The subscriber's status.

        since_timestamp_opt : typing.Optional[str]
            Restrict results to subscribers who opted-in after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_timestamp_opt : typing.Optional[str]
            Restrict results to subscribers who opted-in before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_last_changed : typing.Optional[str]
            Restrict results to subscribers whose information changed after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_last_changed : typing.Optional[str]
            Restrict results to subscribers whose information changed before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        unique_email_id : typing.Optional[str]
            A unique identifier for the email address across all Mailchimp lists.

        vip_only : typing.Optional[bool]
            A filter to return only the list's VIP members. Passing `true` will restrict results to VIP list members, passing `false` will return all list members.

        interest_category_id : typing.Optional[str]
            The unique id for the interest category.

        interest_ids : typing.Optional[str]
            Used to filter list members by interests. Must be accompanied by interest_category_id and interest_match. The value must be a comma separated list of interest ids present for any supplied interest categories.

        interest_match : typing.Optional[ListMembersListsRequestInterestMatch]
            Used to filter list members by interests. Must be accompanied by interest_category_id and interest_ids. "any" will match a member with any of the interest supplied, "all" will only match members with every interest supplied, and "none" will match members without any of the interest supplied.

        sort_field : typing.Optional[ListMembersListsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListMembersListsRequestSortDir]
            Determines the order direction for sorted results.

        since_last_campaign : typing.Optional[bool]
            Filter subscribers by those subscribed/unsubscribed/pending/cleaned since last email campaign send. Member status is required to use this filter.

        unsubscribed_since : typing.Optional[str]
            Filter subscribers by those unsubscribed since a specific date. Using any status other than unsubscribed with this filter will result in an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListMembers, ListMembersListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "email_type": email_type,
                "status": status,
                "since_timestamp_opt": since_timestamp_opt,
                "before_timestamp_opt": before_timestamp_opt,
                "since_last_changed": since_last_changed,
                "before_last_changed": before_last_changed,
                "unique_email_id": unique_email_id,
                "vip_only": vip_only,
                "interest_category_id": interest_category_id,
                "interest_ids": interest_ids,
                "interest_match": interest_match,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "since_last_campaign": since_last_campaign,
                "unsubscribed_since": unsubscribed_since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMembersListsResponse,
                    parse_obj_as(
                        type_=ListMembersListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.members
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_members(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        email_type=email_type,
                        status=status,
                        since_timestamp_opt=since_timestamp_opt,
                        before_timestamp_opt=before_timestamp_opt,
                        since_last_changed=since_last_changed,
                        before_last_changed=before_last_changed,
                        unique_email_id=unique_email_id,
                        vip_only=vip_only,
                        interest_category_id=interest_category_id,
                        interest_ids=interest_ids,
                        interest_match=interest_match,
                        sort_field=sort_field,
                        sort_dir=sort_dir,
                        since_last_campaign=since_last_campaign,
                        unsubscribed_since=unsubscribed_since,
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

    async def create_member(
        self,
        list_id: str,
        *,
        email_address: str,
        status: CreateMemberListsRequestStatus,
        skip_merge_validation: typing.Optional[bool] = None,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[CreateMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, CreateMemberListsRequestMergeFieldsValue]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        timestamp_opt: typing.Optional[CreateMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[CreateMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMembers]:
        """
        Add a new member to the list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        email_address : str
            Email address for a subscriber.

        status : CreateMemberListsRequestStatus
            Subscriber's current status.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[CreateMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, CreateMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        tags : typing.Optional[typing.Sequence[str]]
            The tags that are associated with a member.

        timestamp_opt : typing.Optional[CreateMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[CreateMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMembers]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members",
            method="POST",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[CreateMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, CreateMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "tags": tags,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=CreateMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=CreateMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    async def get_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMembers]:
        """
        Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMembers]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    async def upsert_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        email_address: str,
        skip_merge_validation: typing.Optional[bool] = None,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[UpsertMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue]] = OMIT,
        status: typing.Optional[UpsertMemberListsRequestStatus] = OMIT,
        status_if_new: typing.Optional[UpsertMemberListsRequestStatusIfNew] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        timestamp_opt: typing.Optional[UpsertMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[UpsertMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMembers]:
        """
        Add or update a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        email_address : str
            Email address for a subscriber. This value is required only if the email address is not already present on the list.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[UpsertMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        status : typing.Optional[UpsertMemberListsRequestStatus]
            Subscriber's current status.

        status_if_new : typing.Optional[UpsertMemberListsRequestStatusIfNew]
            Subscriber's status. This value is required only if the email address is not already present on the list.

        tags : typing.Optional[typing.Sequence[str]]
            The tags that are associated with a member.

        timestamp_opt : typing.Optional[UpsertMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[UpsertMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMembers]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
            method="PUT",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=UpsertMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[UpsertMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "status_if_new": status_if_new,
                "tags": tags,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=UpsertMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=UpsertMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    async def delete_member(
        self, list_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Archive a list member. To permanently delete, use the delete-permanent action.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
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

    async def update_member(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        skip_merge_validation: typing.Optional[bool] = None,
        email_address: typing.Optional[str] = OMIT,
        email_type: typing.Optional[str] = OMIT,
        interests: typing.Optional[typing.Dict[str, bool]] = OMIT,
        ip_opt: typing.Optional[str] = OMIT,
        ip_signup: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        location: typing.Optional[UpdateMemberListsRequestLocation] = OMIT,
        marketing_permissions: typing.Optional[
            typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem]
        ] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue]] = OMIT,
        status: typing.Optional[UpdateMemberListsRequestStatus] = OMIT,
        timestamp_opt: typing.Optional[UpdateMemberListsRequestTimestampOpt] = OMIT,
        timestamp_signup: typing.Optional[UpdateMemberListsRequestTimestampSignup] = OMIT,
        vip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMembers]:
        """
        Update information for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        skip_merge_validation : typing.Optional[bool]
            If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.

        email_address : typing.Optional[str]
            Email address for a subscriber.

        email_type : typing.Optional[str]
            Type of email this member asked to get ('html' or 'text').

        interests : typing.Optional[typing.Dict[str, bool]]
            The key of this object's properties is the ID of the interest in question.

        ip_opt : typing.Optional[str]
            The IP address the subscriber used to confirm their opt-in status.

        ip_signup : typing.Optional[str]
            IP address the subscriber signed up from.

        language : typing.Optional[str]
            If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).

        location : typing.Optional[UpdateMemberListsRequestLocation]
            Subscriber location information.

        marketing_permissions : typing.Optional[typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem]]
            The marketing permissions for the subscriber.

        merge_fields : typing.Optional[typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        status : typing.Optional[UpdateMemberListsRequestStatus]
            Subscriber's current status.

        timestamp_opt : typing.Optional[UpdateMemberListsRequestTimestampOpt]

        timestamp_signup : typing.Optional[UpdateMemberListsRequestTimestampSignup]

        vip : typing.Optional[bool]
            [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMembers]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}",
            method="PATCH",
            params={
                "skip_merge_validation": skip_merge_validation,
            },
            json={
                "email_address": email_address,
                "email_type": email_type,
                "interests": interests,
                "ip_opt": ip_opt,
                "ip_signup": ip_signup,
                "language": language,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=UpdateMemberListsRequestLocation, direction="write"
                ),
                "marketing_permissions": convert_and_respect_annotation_metadata(
                    object_=marketing_permissions,
                    annotation=typing.Sequence[UpdateMemberListsRequestMarketingPermissionsItem],
                    direction="write",
                ),
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue],
                    direction="write",
                ),
                "status": status,
                "timestamp_opt": convert_and_respect_annotation_metadata(
                    object_=timestamp_opt, annotation=UpdateMemberListsRequestTimestampOpt, direction="write"
                ),
                "timestamp_signup": convert_and_respect_annotation_metadata(
                    object_=timestamp_signup, annotation=UpdateMemberListsRequestTimestampSignup, direction="write"
                ),
                "vip": vip,
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
                    ListMembers,
                    parse_obj_as(
                        type_=ListMembers,  # type: ignore
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

    async def create_member_action_delete_permanent(
        self, list_id: str, subscriber_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete all personally identifiable information related to a list member, and remove them from a list. This will make it impossible to re-import the list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/actions/delete-permanent",
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

    async def list_member_activity(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        action: typing.Optional[
            typing.Union[
                ListMemberActivityListsRequestActionItem, typing.Sequence[ListMemberActivityListsRequestActionItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMemberActivityListsResponse]:
        """
        Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        action : typing.Optional[typing.Union[ListMemberActivityListsRequestActionItem, typing.Sequence[ListMemberActivityListsRequestActionItem]]]
            A comma seperated list of actions to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMemberActivityListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/activity",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "action": ",".join(map(str, action)) if isinstance(action, (list, tuple, set)) else action,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMemberActivityListsResponse,
                    parse_obj_as(
                        type_=ListMemberActivityListsResponse,  # type: ignore
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

    async def list_member_activity_feed(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        activity_filters: typing.Optional[
            typing.Union[
                ListMemberActivityFeedListsRequestActivityFiltersItem,
                typing.Sequence[ListMemberActivityFeedListsRequestActivityFiltersItem],
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[typing.Any, ListMemberActivityFeedListsResponse]:
        """
        Get a member's activity on a specific list, including opens, clicks, and unsubscribes.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        activity_filters : typing.Optional[typing.Union[ListMemberActivityFeedListsRequestActivityFiltersItem, typing.Sequence[ListMemberActivityFeedListsRequestActivityFiltersItem]]]
            A comma-separated list of activity filters that correspond to a set of activity types, e.g "?activity_filters=open,bounce,click".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[typing.Any, ListMemberActivityFeedListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/activity-feed",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "activity_filters": ",".join(map(str, activity_filters))
                if isinstance(activity_filters, (list, tuple, set))
                else activity_filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberActivityFeedListsResponse,
                    parse_obj_as(
                        type_=ListMemberActivityFeedListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.activity
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_member_activity_feed(
                        list_id,
                        subscriber_hash,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        activity_filters=activity_filters,
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

    async def list_member_events(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListMemberEventsListsResponseEventsItem, ListMemberEventsListsResponse]:
        """
        Get events for a contact.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListMemberEventsListsResponseEventsItem, ListMemberEventsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/events",
            method="GET",
            params={
                "count": count,
                "offset": offset,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberEventsListsResponse,
                    parse_obj_as(
                        type_=ListMemberEventsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.events
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_member_events(
                        list_id,
                        subscriber_hash,
                        count=count,
                        offset=offset + 1,
                        fields=fields,
                        exclude_fields=exclude_fields,
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

    async def create_member_event(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        name: str,
        is_syncing: typing.Optional[bool] = OMIT,
        occurred_at: typing.Optional[dt.datetime] = OMIT,
        properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Add an event for a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        name : str
            The name for this type of event ('purchased', 'visited', etc). Must be 2-30 characters in length

        is_syncing : typing.Optional[bool]
            Events created with the is_syncing value set to `true` will not trigger automations.

        occurred_at : typing.Optional[dt.datetime]
            The date and time the event occurred in ISO 8601 format.

        properties : typing.Optional[typing.Dict[str, str]]
            An optional list of properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/events",
            method="POST",
            json={
                "is_syncing": is_syncing,
                "name": name,
                "occurred_at": occurred_at,
                "properties": properties,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def list_member_goals(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMemberGoalsListsResponse]:
        """
        Get the last 50 Goal events for a member on a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMemberGoalsListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/goals",
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
                    ListMemberGoalsListsResponse,
                    parse_obj_as(
                        type_=ListMemberGoalsListsResponse,  # type: ignore
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

    async def list_member_notes(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        sort_field: typing.Optional[ListMemberNotesListsRequestSortField] = None,
        sort_dir: typing.Optional[ListMemberNotesListsRequestSortDir] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[MemberNotes, ListMemberNotesListsResponse]:
        """
        Get recent notes for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        sort_field : typing.Optional[ListMemberNotesListsRequestSortField]
            Returns notes sorted by the specified field.

        sort_dir : typing.Optional[ListMemberNotesListsRequestSortDir]
            Determines the order direction for sorted results.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[MemberNotes, ListMemberNotesListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes",
            method="GET",
            params={
                "sort_field": sort_field,
                "sort_dir": sort_dir,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberNotesListsResponse,
                    parse_obj_as(
                        type_=ListMemberNotesListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.notes
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_member_notes(
                        list_id,
                        subscriber_hash,
                        sort_field=sort_field,
                        sort_dir=sort_dir,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
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

    async def create_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberNotes]:
        """
        Add a new note for a specific subscriber.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        note : typing.Optional[str]
            The content of the note. Note length is limited to 1,000 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberNotes]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes",
            method="POST",
            json={
                "note": note,
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    async def get_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberNotes]:
        """
        Get a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberNotes]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    async def delete_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
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

    async def update_member_note(
        self,
        list_id: str,
        subscriber_hash: str,
        note_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberNotes]:
        """
        Update a specific note for a specific list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        note_id : str
            The id for the note.

        note : typing.Optional[str]
            The content of the note. Note length is limited to 1,000 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberNotes]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/notes/{encode_path_param(note_id)}",
            method="PATCH",
            json={
                "note": note,
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
                    MemberNotes,
                    parse_obj_as(
                        type_=MemberNotes,  # type: ignore
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

    async def list_member_tags(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListMemberTagsListsResponseTagsItem, ListMemberTagsListsResponse]:
        """
        Get the tags on a list member.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListMemberTagsListsResponseTagsItem, ListMemberTagsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/tags",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMemberTagsListsResponse,
                    parse_obj_as(
                        type_=ListMemberTagsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.tags
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_member_tags(
                        list_id,
                        subscriber_hash,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
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

    async def create_member_tag(
        self,
        list_id: str,
        subscriber_hash: str,
        *,
        tags: typing.Sequence[CreateMemberTagListsRequestTagsItem],
        is_syncing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Add or remove tags from a list member. If a tag that does not exist is passed in and set as 'active', a new tag will be created.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        tags : typing.Sequence[CreateMemberTagListsRequestTagsItem]
            A list of tags assigned to the list member.

        is_syncing : typing.Optional[bool]
            When is_syncing is true, automations based on the tags in the request will not fire

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/members/{encode_path_param(subscriber_hash)}/tags",
            method="POST",
            json={
                "is_syncing": is_syncing,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CreateMemberTagListsRequestTagsItem], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_merge_fields(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[MergeField, ListMergeFieldsListsResponse]:
        """
        Get a list of all merge fields for an audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            The merge field type.

        required : typing.Optional[bool]
            Whether it's a required merge field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[MergeField, ListMergeFieldsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "required": required,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMergeFieldsListsResponse,
                    parse_obj_as(
                        type_=ListMergeFieldsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.merge_fields
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_merge_fields(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        type=type,
                        required=required,
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

    async def create_merge_field(
        self,
        list_id: str,
        *,
        name: str,
        type: CreateMergeFieldListsRequestType,
        default_value: typing.Optional[str] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        help_text: typing.Optional[str] = OMIT,
        options: typing.Optional[CreateMergeFieldListsRequestOptions] = OMIT,
        public: typing.Optional[bool] = OMIT,
        required: typing.Optional[bool] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MergeField]:
        """
        Add a new merge field for a specific audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : str
            The name of the merge field (audience field).

        type : CreateMergeFieldListsRequestType
            The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.

        default_value : typing.Optional[str]
            The default value for the merge field if `null`.

        display_order : typing.Optional[int]
            The order that the merge field displays on the list signup form.

        help_text : typing.Optional[str]
            Extra text to help the subscriber fill out the form.

        options : typing.Optional[CreateMergeFieldListsRequestOptions]
            Extra options for some merge field types.

        public : typing.Optional[bool]
            Whether the merge field is displayed on the signup form.

        required : typing.Optional[bool]
            Whether the merge field is required to import a contact.

        tag : typing.Optional[str]
            The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MergeField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields",
            method="POST",
            json={
                "default_value": default_value,
                "display_order": display_order,
                "help_text": help_text,
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=CreateMergeFieldListsRequestOptions, direction="write"
                ),
                "public": public,
                "required": required,
                "tag": tag,
                "type": type,
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
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    async def get_merge_field(
        self,
        list_id: str,
        merge_id: str,
        *,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MergeField]:
        """
        Get information about a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MergeField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
            method="GET",
            params={
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    async def delete_merge_field(
        self, list_id: str, merge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
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

    async def update_merge_field(
        self,
        list_id: str,
        merge_id: str,
        *,
        default_value: typing.Optional[str] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        help_text: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[UpdateMergeFieldListsRequestOptions] = OMIT,
        public: typing.Optional[bool] = OMIT,
        required: typing.Optional[bool] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MergeField]:
        """
        Update a specific merge field.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        merge_id : str
            The id for the merge field.

        default_value : typing.Optional[str]
            The default value for the merge field if `null`.

        display_order : typing.Optional[int]
            The order that the merge field displays on the list signup form.

        help_text : typing.Optional[str]
            Extra text to help the subscriber fill out the form.

        name : typing.Optional[str]
            The name of the merge field (audience field).

        options : typing.Optional[UpdateMergeFieldListsRequestOptions]
            Extra options for some merge field types.

        public : typing.Optional[bool]
            Whether the merge field is displayed on the signup form.

        required : typing.Optional[bool]
            Whether the merge field is required to import a contact.

        tag : typing.Optional[str]
            The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MergeField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/merge-fields/{encode_path_param(merge_id)}",
            method="PATCH",
            json={
                "default_value": default_value,
                "display_order": display_order,
                "help_text": help_text,
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=UpdateMergeFieldListsRequestOptions, direction="write"
                ),
                "public": public,
                "required": required,
                "tag": tag,
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
                    MergeField,
                    parse_obj_as(
                        type_=MergeField,  # type: ignore
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

    async def list_segments(
        self,
        list_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        since_updated_at: typing.Optional[str] = None,
        before_updated_at: typing.Optional[str] = None,
        exclude_type: typing.Optional[ListSegmentsListsRequestExcludeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[List, ListSegmentsListsResponse]:
        """
        Get information about all available segments for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            Limit results based on segment type.

        since_created_at : typing.Optional[str]
            Restrict results to segments created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_created_at : typing.Optional[str]
            Restrict results to segments created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        since_updated_at : typing.Optional[str]
            Restrict results to segments update after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_updated_at : typing.Optional[str]
            Restrict results to segments update before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        exclude_type : typing.Optional[ListSegmentsListsRequestExcludeType]
            Exclude results based on segment type. For example, use `exclude_type=static` to exclude tags from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[List, ListSegmentsListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "since_created_at": since_created_at,
                "before_created_at": before_created_at,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
                "since_updated_at": since_updated_at,
                "before_updated_at": before_updated_at,
                "exclude_type": exclude_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListSegmentsListsResponse,
                    parse_obj_as(
                        type_=ListSegmentsListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.segments
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_segments(
                        list_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        type=type,
                        since_created_at=since_created_at,
                        before_created_at=before_created_at,
                        include_cleaned=include_cleaned,
                        include_transactional=include_transactional,
                        include_unsubscribed=include_unsubscribed,
                        since_updated_at=since_updated_at,
                        before_updated_at=before_updated_at,
                        exclude_type=exclude_type,
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

    async def create_segment(
        self,
        list_id: str,
        *,
        name: str,
        options: typing.Optional[CreateSegmentListsRequestOptions] = OMIT,
        static_segment: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[List]:
        """
        Create a new segment in a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : str
            The name of the segment.

        options : typing.Optional[CreateSegmentListsRequestOptions]
            The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.

        static_segment : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array will create a static segment without any subscribers. This field cannot be provided with the options field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[List]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments",
            method="POST",
            json={
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=CreateSegmentListsRequestOptions, direction="write"
                ),
                "static_segment": static_segment,
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
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    async def get_segment(
        self,
        list_id: str,
        segment_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[List]:
        """
        Get information about a specific segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[List]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    async def batch_add_or_remove_members(
        self,
        list_id: str,
        segment_id: str,
        *,
        members_to_add: typing.Optional[typing.Sequence[str]] = OMIT,
        members_to_remove: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchAddOrRemoveMembersListsResponse]:
        """
        Batch add/remove list members to static segment

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        members_to_add : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.

        members_to_remove : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchAddOrRemoveMembersListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="POST",
            json={
                "members_to_add": members_to_add,
                "members_to_remove": members_to_remove,
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
                    BatchAddOrRemoveMembersListsResponse,
                    parse_obj_as(
                        type_=BatchAddOrRemoveMembersListsResponse,  # type: ignore
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

    async def delete_segment(
        self, list_id: str, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific segment in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
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

    async def update_segment(
        self,
        list_id: str,
        segment_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[UpdateSegmentListsRequestOptions] = OMIT,
        static_segment: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[List]:
        """
        Update a specific segment in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        name : typing.Optional[str]
            The name of the segment.

        options : typing.Optional[UpdateSegmentListsRequestOptions]
            The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.

        static_segment : typing.Optional[typing.Sequence[str]]
            An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array for an existing static segment will reset that segment and remove all members. This field cannot be provided with the `options` field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[List]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}",
            method="PATCH",
            json={
                "name": name,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=UpdateSegmentListsRequestOptions, direction="write"
                ),
                "static_segment": static_segment,
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
                    List,
                    parse_obj_as(
                        type_=List,  # type: ignore
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

    async def list_segment_members(
        self,
        list_id: str,
        segment_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_cleaned: typing.Optional[bool] = None,
        include_transactional: typing.Optional[bool] = None,
        include_unsubscribed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListsSegmentsMembers, ListSegmentMembersListsResponse]:
        """
        Get information about members in a saved segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        include_cleaned : typing.Optional[bool]
            Include cleaned members in response

        include_transactional : typing.Optional[bool]
            Include transactional members in response

        include_unsubscribed : typing.Optional[bool]
            Include unsubscribed members in response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListsSegmentsMembers, ListSegmentMembersListsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "include_cleaned": include_cleaned,
                "include_transactional": include_transactional,
                "include_unsubscribed": include_unsubscribed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListSegmentMembersListsResponse,
                    parse_obj_as(
                        type_=ListSegmentMembersListsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.members
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_segment_members(
                        list_id,
                        segment_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        include_cleaned=include_cleaned,
                        include_transactional=include_transactional,
                        include_unsubscribed=include_unsubscribed,
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

    async def create_segment_member(
        self,
        list_id: str,
        segment_id: str,
        *,
        email_address: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListsSegmentsMembers]:
        """
        Add a member to a static segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        email_address : str
            Email address for a subscriber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListsSegmentsMembers]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members",
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
                    ListsSegmentsMembers,
                    parse_obj_as(
                        type_=ListsSegmentsMembers,  # type: ignore
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

    async def delete_segment_member(
        self,
        list_id: str,
        segment_id: str,
        subscriber_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Remove a member from the specified static segment.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        segment_id : str
            The unique id for the segment.

        subscriber_hash : str
            The MD5 hash of the lowercase version of the list member's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/segments/{encode_path_param(segment_id)}/members/{encode_path_param(subscriber_hash)}",
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

    async def list_signup_forms(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListSignupFormsListsResponse]:
        """
        Get signup forms for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSignupFormsListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/signup-forms",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSignupFormsListsResponse,
                    parse_obj_as(
                        type_=ListSignupFormsListsResponse,  # type: ignore
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

    async def create_signup_form(
        self,
        list_id: str,
        *,
        contents: typing.Optional[typing.Sequence[CreateSignupFormListsRequestContentsItem]] = OMIT,
        header: typing.Optional[CreateSignupFormListsRequestHeader] = OMIT,
        styles: typing.Optional[typing.Sequence[CreateSignupFormListsRequestStylesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SignupForm]:
        """
        Customize a list's default signup form.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        contents : typing.Optional[typing.Sequence[CreateSignupFormListsRequestContentsItem]]
            The signup form body content.

        header : typing.Optional[CreateSignupFormListsRequestHeader]
            Options for customizing your signup form header.

        styles : typing.Optional[typing.Sequence[CreateSignupFormListsRequestStylesItem]]
            An array of objects, each representing an element style for the signup form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignupForm]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/signup-forms",
            method="POST",
            json={
                "contents": convert_and_respect_annotation_metadata(
                    object_=contents,
                    annotation=typing.Sequence[CreateSignupFormListsRequestContentsItem],
                    direction="write",
                ),
                "header": convert_and_respect_annotation_metadata(
                    object_=header, annotation=CreateSignupFormListsRequestHeader, direction="write"
                ),
                "styles": convert_and_respect_annotation_metadata(
                    object_=styles,
                    annotation=typing.Sequence[CreateSignupFormListsRequestStylesItem],
                    direction="write",
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
                    SignupForm,
                    parse_obj_as(
                        type_=SignupForm,  # type: ignore
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

    async def list_surveys(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Get information about all available surveys for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    async def create_survey(
        self,
        list_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        sections: typing.Optional[typing.Sequence[SurveySectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Create a draft survey for an audience.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        title : typing.Optional[str]
            The title of the survey.

        sections : typing.Optional[typing.Sequence[SurveySectionRequest]]
            Initial survey sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Survey created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys",
            method="POST",
            json={
                "title": title,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections, annotation=typing.Sequence[SurveySectionRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    async def get_survey(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Get details about a specific survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    async def delete_survey(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
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

    async def update_survey(
        self,
        list_id: str,
        survey_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        is_piped_to_inbox: typing.Optional[bool] = OMIT,
        sections: typing.Optional[typing.Sequence[SurveySectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Update a survey. When sections is provided, send the complete section list in display order. Any existing section not included is deleted.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        title : typing.Optional[str]
            The title of the survey.

        is_piped_to_inbox : typing.Optional[bool]
            Whether responses are sent to Mailchimp Inbox.

        sections : typing.Optional[typing.Sequence[SurveySectionRequest]]
            The complete survey section list in display order. On update, sections omitted from this array are deleted. Include section id to update an existing section; omit section id to add a new section.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Survey updated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/surveys/{encode_path_param(survey_id)}",
            method="PATCH",
            json={
                "title": title,
                "is_piped_to_inbox": is_piped_to_inbox,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections, annotation=typing.Sequence[SurveySectionRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    async def create_list_survey_action_replicate(
        self,
        list_id_path_param: str,
        survey_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Replicate a survey.

        Parameters
        ----------
        list_id_path_param : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        title : typing.Optional[str]
            The title for the replicated survey.

        list_id : typing.Optional[str]
            The unique ID of the audience for the replicated survey. Defaults to the source survey audience.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Survey replicated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id_path_param)}/surveys/{encode_path_param(survey_id)}/actions/replicate",
            method="POST",
            json={
                "title": title,
                "list_id": list_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,  # type: ignore
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

    async def list_tag_search(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTagSearchListsResponse]:
        """
        Search for tags on a list by name. If no name is provided, will return all tags on the list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        name : typing.Optional[str]
            The search query used to filter tags.  The search query will be compared to each tag as a prefix, so all tags that have a name starting with this field will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTagSearchListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/tag-search",
            method="GET",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTagSearchListsResponse,
                    parse_obj_as(
                        type_=ListTagSearchListsResponse,  # type: ignore
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

    async def list_webhooks(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListWebhooksListsResponse]:
        """
        Get information about all webhooks for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhooksListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksListsResponse,
                    parse_obj_as(
                        type_=ListWebhooksListsResponse,  # type: ignore
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

    async def create_webhook(
        self,
        list_id: str,
        *,
        events: typing.Optional[AddWebhookEvents] = OMIT,
        sources: typing.Optional[AddWebhookSources] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateWebhookListsResponse]:
        """
        Create a new webhook for a specific list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        events : typing.Optional[AddWebhookEvents]
            The events that can trigger the webhook and whether they are enabled.

        sources : typing.Optional[AddWebhookSources]
            The possible sources of any events that can trigger the webhook and whether they are enabled.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateWebhookListsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=AddWebhookEvents, direction="write"
                ),
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=AddWebhookSources, direction="write"
                ),
                "url": url,
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
                    CreateWebhookListsResponse,
                    parse_obj_as(
                        type_=CreateWebhookListsResponse,  # type: ignore
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

    async def get_webhook(
        self, list_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListWebhooks]:
        """
        Get information about a specific webhook.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhooks]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooks,
                    parse_obj_as(
                        type_=ListWebhooks,  # type: ignore
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

    async def delete_webhook(
        self, list_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific webhook in a list.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
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

    async def update_webhook(
        self,
        list_id: str,
        webhook_id: str,
        *,
        events: typing.Optional[AddWebhookEvents] = OMIT,
        sources: typing.Optional[AddWebhookSources] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWebhooks]:
        """
        Update the settings for an existing webhook.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        webhook_id : str
            The webhook's id.

        events : typing.Optional[AddWebhookEvents]
            The events that can trigger the webhook and whether they are enabled.

        sources : typing.Optional[AddWebhookSources]
            The possible sources of any events that can trigger the webhook and whether they are enabled.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhooks]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/lists/{encode_path_param(list_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=AddWebhookEvents, direction="write"
                ),
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=AddWebhookSources, direction="write"
                ),
                "url": url,
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
                    ListWebhooks,
                    parse_obj_as(
                        type_=ListWebhooks,  # type: ignore
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
