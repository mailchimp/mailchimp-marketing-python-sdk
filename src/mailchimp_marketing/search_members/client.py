# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSearchMembersClient, RawSearchMembersClient
from .types.list_search_members_response import ListSearchMembersResponse


class SearchMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchMembersClient
        """
        return self._raw_client

    def list(
        self,
        *,
        query: str,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        list_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSearchMembersResponse:
        """
        Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.

        Parameters
        ----------
        query : str
            The search query used to filter results. Query should be a valid email, or a string representing a contact's first or last name.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        list_id : typing.Optional[str]
            The unique id for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSearchMembersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.search_members.list(
            query="query",
        )
        """
        _response = self._raw_client.list(
            query=query, fields=fields, exclude_fields=exclude_fields, list_id=list_id, request_options=request_options
        )
        return _response.data


class AsyncSearchMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchMembersClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        query: str,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        list_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSearchMembersResponse:
        """
        Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.

        Parameters
        ----------
        query : str
            The search query used to filter results. Query should be a valid email, or a string representing a contact's first or last name.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        list_id : typing.Optional[str]
            The unique id for the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSearchMembersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search_members.list(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            query=query, fields=fields, exclude_fields=exclude_fields, list_id=list_id, request_options=request_options
        )
        return _response.data
