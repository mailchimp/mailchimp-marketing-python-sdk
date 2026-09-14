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
from .types.create_account_exports_request_include_stages_item import CreateAccountExportsRequestIncludeStagesItem
from .types.create_account_exports_response import CreateAccountExportsResponse
from .types.get_account_exports_response import GetAccountExportsResponse
from .types.list_account_exports_response import ListAccountExportsResponse
from .types.list_account_exports_response_exports_item import ListAccountExportsResponseExportsItem
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAccountExportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListAccountExportsResponseExportsItem, ListAccountExportsResponse]:
        """
        Get a list of account exports for a given account.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListAccountExportsResponseExportsItem, ListAccountExportsResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/account-exports",
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
                    ListAccountExportsResponse,
                    parse_obj_as(
                        type_=ListAccountExportsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.exports
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list(
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

    def create(
        self,
        *,
        include_stages: typing.Sequence[CreateAccountExportsRequestIncludeStagesItem],
        since_timestamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAccountExportsResponse]:
        """
        Create a new account export in your Mailchimp account.

        Parameters
        ----------
        include_stages : typing.Sequence[CreateAccountExportsRequestIncludeStagesItem]
            The stages of an account export to include.

        since_timestamp : typing.Optional[dt.datetime]
            An ISO 8601 date that will limit the export to only records created after a given time. For instance, the reports stage will contain any campaign sent after the given timestamp. Audiences, however, are excluded from this limit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAccountExportsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/account-exports",
            method="POST",
            json={
                "include_stages": include_stages,
                "since_timestamp": since_timestamp,
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
                    CreateAccountExportsResponse,
                    parse_obj_as(
                        type_=CreateAccountExportsResponse,  # type: ignore
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
        export_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAccountExportsResponse]:
        """
        Get information about a specific account export.

        Parameters
        ----------
        export_id : str
            The unique id for the account export.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAccountExportsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/account-exports/{encode_path_param(export_id)}",
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
                    GetAccountExportsResponse,
                    parse_obj_as(
                        type_=GetAccountExportsResponse,  # type: ignore
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


class AsyncRawAccountExportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListAccountExportsResponseExportsItem, ListAccountExportsResponse]:
        """
        Get a list of account exports for a given account.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListAccountExportsResponseExportsItem, ListAccountExportsResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/account-exports",
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
                    ListAccountExportsResponse,
                    parse_obj_as(
                        type_=ListAccountExportsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.exports
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list(
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

    async def create(
        self,
        *,
        include_stages: typing.Sequence[CreateAccountExportsRequestIncludeStagesItem],
        since_timestamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAccountExportsResponse]:
        """
        Create a new account export in your Mailchimp account.

        Parameters
        ----------
        include_stages : typing.Sequence[CreateAccountExportsRequestIncludeStagesItem]
            The stages of an account export to include.

        since_timestamp : typing.Optional[dt.datetime]
            An ISO 8601 date that will limit the export to only records created after a given time. For instance, the reports stage will contain any campaign sent after the given timestamp. Audiences, however, are excluded from this limit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAccountExportsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/account-exports",
            method="POST",
            json={
                "include_stages": include_stages,
                "since_timestamp": since_timestamp,
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
                    CreateAccountExportsResponse,
                    parse_obj_as(
                        type_=CreateAccountExportsResponse,  # type: ignore
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
        export_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAccountExportsResponse]:
        """
        Get information about a specific account export.

        Parameters
        ----------
        export_id : str
            The unique id for the account export.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAccountExportsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/account-exports/{encode_path_param(export_id)}",
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
                    GetAccountExportsResponse,
                    parse_obj_as(
                        type_=GetAccountExportsResponse,  # type: ignore
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
