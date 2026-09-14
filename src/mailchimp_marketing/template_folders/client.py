# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTemplateFoldersClient, RawTemplateFoldersClient
from .types.create_template_folders_response import CreateTemplateFoldersResponse
from .types.get_template_folders_response import GetTemplateFoldersResponse
from .types.list_template_folders_response import ListTemplateFoldersResponse
from .types.list_template_folders_response_folders_item import ListTemplateFoldersResponseFoldersItem
from .types.update_template_folders_response import UpdateTemplateFoldersResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TemplateFoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTemplateFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTemplateFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTemplateFoldersClient
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
    ) -> SyncPager[ListTemplateFoldersResponseFoldersItem, ListTemplateFoldersResponse]:
        """
        Get all folders used to organize templates.

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
        SyncPager[ListTemplateFoldersResponseFoldersItem, ListTemplateFoldersResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.template_folders.list()
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
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTemplateFoldersResponse:
        """
        Create a new template folder.

        Parameters
        ----------
        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTemplateFoldersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.template_folders.create(
            name="name",
        )
        """
        _response = self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    def get(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTemplateFoldersResponse:
        """
        Get information about a specific folder used to organize templates.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTemplateFoldersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.template_folders.get(
            folder_id="folder_id",
        )
        """
        _response = self._raw_client.get(
            folder_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete(self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific template folder, and mark all the templates in the folder as 'unfiled'.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

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
        client.template_folders.delete(
            folder_id="folder_id",
        )
        """
        _response = self._raw_client.delete(folder_id, request_options=request_options)
        return _response.data

    def update(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateTemplateFoldersResponse:
        """
        Update a specific folder used to organize templates.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTemplateFoldersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.template_folders.update(
            folder_id="folder_id",
            name="name",
        )
        """
        _response = self._raw_client.update(folder_id, name=name, request_options=request_options)
        return _response.data


class AsyncTemplateFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTemplateFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTemplateFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTemplateFoldersClient
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
    ) -> AsyncPager[ListTemplateFoldersResponseFoldersItem, ListTemplateFoldersResponse]:
        """
        Get all folders used to organize templates.

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
        AsyncPager[ListTemplateFoldersResponseFoldersItem, ListTemplateFoldersResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.template_folders.list()
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
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTemplateFoldersResponse:
        """
        Create a new template folder.

        Parameters
        ----------
        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTemplateFoldersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.template_folders.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    async def get(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTemplateFoldersResponse:
        """
        Get information about a specific folder used to organize templates.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTemplateFoldersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.template_folders.get(
                folder_id="folder_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            folder_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete(self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific template folder, and mark all the templates in the folder as 'unfiled'.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

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
            await client.template_folders.delete(
                folder_id="folder_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(folder_id, request_options=request_options)
        return _response.data

    async def update(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateTemplateFoldersResponse:
        """
        Update a specific folder used to organize templates.

        Parameters
        ----------
        folder_id : str
            The unique id for the template folder.

        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTemplateFoldersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.template_folders.update(
                folder_id="folder_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(folder_id, name=name, request_options=request_options)
        return _response.data
