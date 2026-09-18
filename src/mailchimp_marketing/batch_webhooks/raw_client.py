# This file was auto-generated from our API Definition.

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
from ..types.batch_webhook import BatchWebhook
from .types.create_batch_webhooks_response import CreateBatchWebhooksResponse
from .types.list_batch_webhooks_response import ListBatchWebhooksResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawBatchWebhooksClient:
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
    ) -> SyncPager[BatchWebhook, ListBatchWebhooksResponse]:
        """
        Get all webhooks that have been configured for batches.

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
        SyncPager[BatchWebhook, ListBatchWebhooksResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/batch-webhooks",
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
                    ListBatchWebhooksResponse,
                    parse_obj_as(
                        type_=ListBatchWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.webhooks
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
        url: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateBatchWebhooksResponse]:
        """
        Configure a webhook that will fire whenever any batch request completes processing.  You may only have a maximum of 20 batch webhooks.

        Parameters
        ----------
        url : str
            A valid URL for the Webhook.

        enabled : typing.Optional[bool]
            Whether the webhook receives requests or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBatchWebhooksResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/batch-webhooks",
            method="POST",
            json={
                "enabled": enabled,
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
                    CreateBatchWebhooksResponse,
                    parse_obj_as(
                        type_=CreateBatchWebhooksResponse,  # type: ignore
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
        batch_webhook_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchWebhook]:
        """
        Get information about a specific batch webhook.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchWebhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
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
                    BatchWebhook,
                    parse_obj_as(
                        type_=BatchWebhook,  # type: ignore
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

    def delete(
        self, batch_webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Remove a batch webhook. Webhooks will no longer be sent to the given URL.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
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
        batch_webhook_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchWebhook]:
        """
        Update a webhook that will fire whenever any batch request completes processing.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        enabled : typing.Optional[bool]
            Whether the webhook receives requests or not.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchWebhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
            method="PATCH",
            json={
                "enabled": enabled,
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
                    BatchWebhook,
                    parse_obj_as(
                        type_=BatchWebhook,  # type: ignore
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


class AsyncRawBatchWebhooksClient:
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
    ) -> AsyncPager[BatchWebhook, ListBatchWebhooksResponse]:
        """
        Get all webhooks that have been configured for batches.

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
        AsyncPager[BatchWebhook, ListBatchWebhooksResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/batch-webhooks",
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
                    ListBatchWebhooksResponse,
                    parse_obj_as(
                        type_=ListBatchWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.webhooks
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
        url: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateBatchWebhooksResponse]:
        """
        Configure a webhook that will fire whenever any batch request completes processing.  You may only have a maximum of 20 batch webhooks.

        Parameters
        ----------
        url : str
            A valid URL for the Webhook.

        enabled : typing.Optional[bool]
            Whether the webhook receives requests or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBatchWebhooksResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/batch-webhooks",
            method="POST",
            json={
                "enabled": enabled,
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
                    CreateBatchWebhooksResponse,
                    parse_obj_as(
                        type_=CreateBatchWebhooksResponse,  # type: ignore
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
        batch_webhook_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchWebhook]:
        """
        Get information about a specific batch webhook.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchWebhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
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
                    BatchWebhook,
                    parse_obj_as(
                        type_=BatchWebhook,  # type: ignore
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
        self, batch_webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Remove a batch webhook. Webhooks will no longer be sent to the given URL.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
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
        batch_webhook_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchWebhook]:
        """
        Update a webhook that will fire whenever any batch request completes processing.

        Parameters
        ----------
        batch_webhook_id : str
            The unique id for the batch webhook.

        enabled : typing.Optional[bool]
            Whether the webhook receives requests or not.

        url : typing.Optional[str]
            A valid URL for the Webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchWebhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/batch-webhooks/{encode_path_param(batch_webhook_id)}",
            method="PATCH",
            json={
                "enabled": enabled,
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
                    BatchWebhook,
                    parse_obj_as(
                        type_=BatchWebhook,  # type: ignore
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
