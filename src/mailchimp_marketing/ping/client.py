# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPingClient, RawPingClient
from .types.list_ping_response import ListPingResponse


class PingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPingClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPingResponse:
        """
        A health check for the API that won't return any account-specific information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPingResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ping.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncPingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPingClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPingResponse:
        """
        A health check for the API that won't return any account-specific information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPingResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ping.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
