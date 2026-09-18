# This file was auto-generated from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.audiences_contact import AudiencesContact
from .types.create_audience_contact_request_data_mode import CreateAudienceContactRequestDataMode
from .types.create_audience_contact_request_email_channel import CreateAudienceContactRequestEmailChannel
from .types.create_audience_contact_request_merge_field_validation_mode import (
    CreateAudienceContactRequestMergeFieldValidationMode,
)
from .types.create_audience_contact_request_merge_fields_value import CreateAudienceContactRequestMergeFieldsValue
from .types.create_audience_contact_request_sms_channel import CreateAudienceContactRequestSmsChannel
from .types.create_audience_contact_request_tags_item import CreateAudienceContactRequestTagsItem
from .types.get_audience_contact_list_request_sort_dir import GetAudienceContactListRequestSortDir
from .types.get_audience_contact_list_request_sort_field import GetAudienceContactListRequestSortField
from .types.get_audience_contact_list_response import GetAudienceContactListResponse
from .types.patch_audience_contact_request_data_mode import PatchAudienceContactRequestDataMode
from .types.patch_audience_contact_request_email_channel import PatchAudienceContactRequestEmailChannel
from .types.patch_audience_contact_request_merge_field_validation_mode import (
    PatchAudienceContactRequestMergeFieldValidationMode,
)
from .types.patch_audience_contact_request_merge_fields_value import PatchAudienceContactRequestMergeFieldsValue
from .types.patch_audience_contact_request_sms_channel import PatchAudienceContactRequestSmsChannel
from .types.patch_audience_contact_request_tags_item import PatchAudienceContactRequestTagsItem
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAudiencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_audience_contact_list(
        self,
        audience_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_since: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        sort_field: typing.Optional[GetAudienceContactListRequestSortField] = None,
        sort_dir: typing.Optional[GetAudienceContactListRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAudienceContactListResponse]:
        """
        Get a list of omni-channel contacts for a given audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        cursor : typing.Optional[str]
            Paginate through a collection of records by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request. Default value fetches the first "page" of results.

        created_before : typing.Optional[dt.datetime]
            Restricts the response to contacts created at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        created_since : typing.Optional[dt.datetime]
            Restricts the response to contacts created after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        updated_before : typing.Optional[dt.datetime]
            Restricts the response to contacts updated at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        updated_since : typing.Optional[dt.datetime]
            Restricts the response to contacts updated after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        sort_field : typing.Optional[GetAudienceContactListRequestSortField]
            Specifies the field to sort the returned contacts by.

        sort_dir : typing.Optional[GetAudienceContactListRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAudienceContactListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "cursor": cursor,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "created_since": serialize_datetime(created_since) if created_since is not None else None,
                "updated_before": serialize_datetime(updated_before) if updated_before is not None else None,
                "updated_since": serialize_datetime(updated_since) if updated_since is not None else None,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudienceContactListResponse,
                    parse_obj_as(
                        type_=GetAudienceContactListResponse,  # type: ignore
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

    def create_audience_contact(
        self,
        audience_id: str,
        *,
        merge_field_validation_mode: typing.Optional[CreateAudienceContactRequestMergeFieldValidationMode] = None,
        data_mode: typing.Optional[CreateAudienceContactRequestDataMode] = None,
        email_channel: typing.Optional[CreateAudienceContactRequestEmailChannel] = OMIT,
        language: typing.Optional[str] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue]] = OMIT,
        sms_channel: typing.Optional[CreateAudienceContactRequestSmsChannel] = OMIT,
        tags: typing.Optional[typing.Sequence[CreateAudienceContactRequestTagsItem]] = OMIT,
        update_existing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AudiencesContact]:
        """
        Create a new omni-channel contact for an audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        merge_field_validation_mode : typing.Optional[CreateAudienceContactRequestMergeFieldValidationMode]
            Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.

        data_mode : typing.Optional[CreateAudienceContactRequestDataMode]
            Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.

        email_channel : typing.Optional[CreateAudienceContactRequestEmailChannel]

        language : typing.Optional[str]
            The contact's detected language.

        merge_fields : typing.Optional[typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        sms_channel : typing.Optional[CreateAudienceContactRequestSmsChannel]

        tags : typing.Optional[typing.Sequence[CreateAudienceContactRequestTagsItem]]
            An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.

        update_existing : typing.Optional[bool]
            If a contact already exists, update them instead of returning a conflict error. When `true` and a matching contact is found (by email or phone), the existing contact is updated with the provided channel data. Defaults to `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AudiencesContact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts",
            method="POST",
            params={
                "merge_field_validation_mode": merge_field_validation_mode,
                "data_mode": data_mode,
            },
            json={
                "email_channel": convert_and_respect_annotation_metadata(
                    object_=email_channel, annotation=CreateAudienceContactRequestEmailChannel, direction="write"
                ),
                "language": language,
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue],
                    direction="write",
                ),
                "sms_channel": convert_and_respect_annotation_metadata(
                    object_=sms_channel, annotation=CreateAudienceContactRequestSmsChannel, direction="write"
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CreateAudienceContactRequestTagsItem], direction="write"
                ),
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    def get_audience_contact(
        self,
        audience_id: str,
        contact_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AudiencesContact]:
        """
        Retrieve a specific omni-channel contact in an audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            A unique identifier for the contact, which can be a Mailchimp contact ID or a channel hash. A channel hash must follow the format email:[md5_hash] (where the hash is the MD5 of the lowercased email address) or sms:[sha256_hash] (where the hash is the SHA256 of the E.164-formatted phone number).

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AudiencesContact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}",
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    def patch_audience_contact(
        self,
        audience_id: str,
        contact_id: str,
        *,
        merge_field_validation_mode: typing.Optional[PatchAudienceContactRequestMergeFieldValidationMode] = None,
        data_mode: typing.Optional[PatchAudienceContactRequestDataMode] = None,
        email_channel: typing.Optional[PatchAudienceContactRequestEmailChannel] = OMIT,
        language: typing.Optional[str] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue]] = OMIT,
        sms_channel: typing.Optional[PatchAudienceContactRequestSmsChannel] = OMIT,
        tags: typing.Optional[typing.Sequence[PatchAudienceContactRequestTagsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AudiencesContact]:
        """
        Update an existing omni-channel contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        merge_field_validation_mode : typing.Optional[PatchAudienceContactRequestMergeFieldValidationMode]
            Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.

        data_mode : typing.Optional[PatchAudienceContactRequestDataMode]
            Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.

        email_channel : typing.Optional[PatchAudienceContactRequestEmailChannel]

        language : typing.Optional[str]
            The contact's detected language.

        merge_fields : typing.Optional[typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        sms_channel : typing.Optional[PatchAudienceContactRequestSmsChannel]

        tags : typing.Optional[typing.Sequence[PatchAudienceContactRequestTagsItem]]
            An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AudiencesContact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}",
            method="PATCH",
            params={
                "merge_field_validation_mode": merge_field_validation_mode,
                "data_mode": data_mode,
            },
            json={
                "email_channel": convert_and_respect_annotation_metadata(
                    object_=email_channel, annotation=PatchAudienceContactRequestEmailChannel, direction="write"
                ),
                "language": language,
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue],
                    direction="write",
                ),
                "sms_channel": convert_and_respect_annotation_metadata(
                    object_=sms_channel, annotation=PatchAudienceContactRequestSmsChannel, direction="write"
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[PatchAudienceContactRequestTagsItem], direction="write"
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    def post_audiences_contacts_actions_archive(
        self, audience_id: str, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Archives a Contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}/actions/archive",
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

    def post_audiences_contacts_actions_forget(
        self, audience_id: str, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Forgets a Contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}/actions/forget",
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


class AsyncRawAudiencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_audience_contact_list(
        self,
        audience_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_since: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        sort_field: typing.Optional[GetAudienceContactListRequestSortField] = None,
        sort_dir: typing.Optional[GetAudienceContactListRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAudienceContactListResponse]:
        """
        Get a list of omni-channel contacts for a given audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        cursor : typing.Optional[str]
            Paginate through a collection of records by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request. Default value fetches the first "page" of results.

        created_before : typing.Optional[dt.datetime]
            Restricts the response to contacts created at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        created_since : typing.Optional[dt.datetime]
            Restricts the response to contacts created after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        updated_before : typing.Optional[dt.datetime]
            Restricts the response to contacts updated at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        updated_since : typing.Optional[dt.datetime]
            Restricts the response to contacts updated after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.

        sort_field : typing.Optional[GetAudienceContactListRequestSortField]
            Specifies the field to sort the returned contacts by.

        sort_dir : typing.Optional[GetAudienceContactListRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAudienceContactListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "cursor": cursor,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "created_since": serialize_datetime(created_since) if created_since is not None else None,
                "updated_before": serialize_datetime(updated_before) if updated_before is not None else None,
                "updated_since": serialize_datetime(updated_since) if updated_since is not None else None,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudienceContactListResponse,
                    parse_obj_as(
                        type_=GetAudienceContactListResponse,  # type: ignore
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

    async def create_audience_contact(
        self,
        audience_id: str,
        *,
        merge_field_validation_mode: typing.Optional[CreateAudienceContactRequestMergeFieldValidationMode] = None,
        data_mode: typing.Optional[CreateAudienceContactRequestDataMode] = None,
        email_channel: typing.Optional[CreateAudienceContactRequestEmailChannel] = OMIT,
        language: typing.Optional[str] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue]] = OMIT,
        sms_channel: typing.Optional[CreateAudienceContactRequestSmsChannel] = OMIT,
        tags: typing.Optional[typing.Sequence[CreateAudienceContactRequestTagsItem]] = OMIT,
        update_existing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AudiencesContact]:
        """
        Create a new omni-channel contact for an audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        merge_field_validation_mode : typing.Optional[CreateAudienceContactRequestMergeFieldValidationMode]
            Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.

        data_mode : typing.Optional[CreateAudienceContactRequestDataMode]
            Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.

        email_channel : typing.Optional[CreateAudienceContactRequestEmailChannel]

        language : typing.Optional[str]
            The contact's detected language.

        merge_fields : typing.Optional[typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        sms_channel : typing.Optional[CreateAudienceContactRequestSmsChannel]

        tags : typing.Optional[typing.Sequence[CreateAudienceContactRequestTagsItem]]
            An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.

        update_existing : typing.Optional[bool]
            If a contact already exists, update them instead of returning a conflict error. When `true` and a matching contact is found (by email or phone), the existing contact is updated with the provided channel data. Defaults to `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AudiencesContact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts",
            method="POST",
            params={
                "merge_field_validation_mode": merge_field_validation_mode,
                "data_mode": data_mode,
            },
            json={
                "email_channel": convert_and_respect_annotation_metadata(
                    object_=email_channel, annotation=CreateAudienceContactRequestEmailChannel, direction="write"
                ),
                "language": language,
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue],
                    direction="write",
                ),
                "sms_channel": convert_and_respect_annotation_metadata(
                    object_=sms_channel, annotation=CreateAudienceContactRequestSmsChannel, direction="write"
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CreateAudienceContactRequestTagsItem], direction="write"
                ),
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    async def get_audience_contact(
        self,
        audience_id: str,
        contact_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AudiencesContact]:
        """
        Retrieve a specific omni-channel contact in an audience.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            A unique identifier for the contact, which can be a Mailchimp contact ID or a channel hash. A channel hash must follow the format email:[md5_hash] (where the hash is the MD5 of the lowercased email address) or sms:[sha256_hash] (where the hash is the SHA256 of the E.164-formatted phone number).

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AudiencesContact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}",
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    async def patch_audience_contact(
        self,
        audience_id: str,
        contact_id: str,
        *,
        merge_field_validation_mode: typing.Optional[PatchAudienceContactRequestMergeFieldValidationMode] = None,
        data_mode: typing.Optional[PatchAudienceContactRequestDataMode] = None,
        email_channel: typing.Optional[PatchAudienceContactRequestEmailChannel] = OMIT,
        language: typing.Optional[str] = OMIT,
        merge_fields: typing.Optional[typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue]] = OMIT,
        sms_channel: typing.Optional[PatchAudienceContactRequestSmsChannel] = OMIT,
        tags: typing.Optional[typing.Sequence[PatchAudienceContactRequestTagsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AudiencesContact]:
        """
        Update an existing omni-channel contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        merge_field_validation_mode : typing.Optional[PatchAudienceContactRequestMergeFieldValidationMode]
            Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.

        data_mode : typing.Optional[PatchAudienceContactRequestDataMode]
            Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.

        email_channel : typing.Optional[PatchAudienceContactRequestEmailChannel]

        language : typing.Optional[str]
            The contact's detected language.

        merge_fields : typing.Optional[typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue]]
            A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.

        sms_channel : typing.Optional[PatchAudienceContactRequestSmsChannel]

        tags : typing.Optional[typing.Sequence[PatchAudienceContactRequestTagsItem]]
            An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AudiencesContact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}",
            method="PATCH",
            params={
                "merge_field_validation_mode": merge_field_validation_mode,
                "data_mode": data_mode,
            },
            json={
                "email_channel": convert_and_respect_annotation_metadata(
                    object_=email_channel, annotation=PatchAudienceContactRequestEmailChannel, direction="write"
                ),
                "language": language,
                "merge_fields": convert_and_respect_annotation_metadata(
                    object_=merge_fields,
                    annotation=typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue],
                    direction="write",
                ),
                "sms_channel": convert_and_respect_annotation_metadata(
                    object_=sms_channel, annotation=PatchAudienceContactRequestSmsChannel, direction="write"
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[PatchAudienceContactRequestTagsItem], direction="write"
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
                    AudiencesContact,
                    parse_obj_as(
                        type_=AudiencesContact,  # type: ignore
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

    async def post_audiences_contacts_actions_archive(
        self, audience_id: str, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Archives a Contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}/actions/archive",
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

    async def post_audiences_contacts_actions_forget(
        self, audience_id: str, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Forgets a Contact.

        Parameters
        ----------
        audience_id : str
            The unique ID for the audience.

        contact_id : str
            The unique id for the contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/audiences/{encode_path_param(audience_id)}/contacts/{encode_path_param(contact_id)}/actions/forget",
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
