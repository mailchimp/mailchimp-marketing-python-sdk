# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountExportsClient, RawAccountExportsClient
from .types.create_account_exports_request_include_stages_item import CreateAccountExportsRequestIncludeStagesItem
from .types.create_account_exports_response import CreateAccountExportsResponse
from .types.get_account_exports_response import GetAccountExportsResponse
from .types.list_account_exports_response import ListAccountExportsResponse
from .types.list_account_exports_response_exports_item import ListAccountExportsResponseExportsItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AccountExportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountExportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountExportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountExportsClient
        """
        return self._raw_client

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


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.account_exports.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fields=fields, exclude_fields=exclude_fields, count=count, offset=offset, request_options=request_options
        )

    def create(
        self,
        *,
        include_stages: typing.Sequence[CreateAccountExportsRequestIncludeStagesItem],
        since_timestamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAccountExportsResponse:
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
        CreateAccountExportsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.account_exports.create(
            include_stages=["audiences", "gallery_files"],
        )
        """
        _response = self._raw_client.create(
            include_stages=include_stages, since_timestamp=since_timestamp, request_options=request_options
        )
        return _response.data

    def get(
        self,
        export_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAccountExportsResponse:
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
        GetAccountExportsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.account_exports.get(
            export_id="export_id",
        )
        """
        _response = self._raw_client.get(
            export_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data


class AsyncAccountExportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountExportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountExportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountExportsClient
        """
        return self._raw_client

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


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.account_exports.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fields=fields, exclude_fields=exclude_fields, count=count, offset=offset, request_options=request_options
        )

    async def create(
        self,
        *,
        include_stages: typing.Sequence[CreateAccountExportsRequestIncludeStagesItem],
        since_timestamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAccountExportsResponse:
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
        CreateAccountExportsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_exports.create(
                include_stages=["audiences", "gallery_files"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            include_stages=include_stages, since_timestamp=since_timestamp, request_options=request_options
        )
        return _response.data

    async def get(
        self,
        export_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAccountExportsResponse:
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
        GetAccountExportsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_exports.get(
                export_id="export_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            export_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data
