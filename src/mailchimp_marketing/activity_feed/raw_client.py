# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.list_activity_feed_response_item import ListActivityFeedResponseItem
from .types.list_chimp_chatter_activity_feed_response import ListChimpChatterActivityFeedResponse
from .types.list_chimp_chatter_activity_feed_response_chimp_chatter_item import (
    ListChimpChatterActivityFeedResponseChimpChatterItem,
)
from pydantic import ValidationError


class RawActivityFeedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListActivityFeedResponseItem]]:
        """
        Get information about the activity feed endpoint's resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListActivityFeedResponseItem]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/activity-feed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListActivityFeedResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListActivityFeedResponseItem],  # type: ignore
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

    def list_chimp_chatter(
        self,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListChimpChatterActivityFeedResponseChimpChatterItem, ListChimpChatterActivityFeedResponse]:
        """
        Return the Chimp Chatter for this account ordered by most recent.

        Parameters
        ----------
        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListChimpChatterActivityFeedResponseChimpChatterItem, ListChimpChatterActivityFeedResponse]
            ChimpChatter Collection
        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/activity-feed/chimp-chatter",
            method="GET",
            params={
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListChimpChatterActivityFeedResponse,
                    parse_obj_as(
                        type_=ListChimpChatterActivityFeedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.chimp_chatter
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_chimp_chatter(
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


class AsyncRawActivityFeedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListActivityFeedResponseItem]]:
        """
        Get information about the activity feed endpoint's resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListActivityFeedResponseItem]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/activity-feed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListActivityFeedResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListActivityFeedResponseItem],  # type: ignore
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

    async def list_chimp_chatter(
        self,
        *,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListChimpChatterActivityFeedResponseChimpChatterItem, ListChimpChatterActivityFeedResponse]:
        """
        Return the Chimp Chatter for this account ordered by most recent.

        Parameters
        ----------
        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListChimpChatterActivityFeedResponseChimpChatterItem, ListChimpChatterActivityFeedResponse]
            ChimpChatter Collection
        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/activity-feed/chimp-chatter",
            method="GET",
            params={
                "count": count,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListChimpChatterActivityFeedResponse,
                    parse_obj_as(
                        type_=ListChimpChatterActivityFeedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.chimp_chatter
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_chimp_chatter(
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
