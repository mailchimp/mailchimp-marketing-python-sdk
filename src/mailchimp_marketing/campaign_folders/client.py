# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.campaign_folders import CampaignFolders
from ..types.campaign_folders_folders_item import CampaignFoldersFoldersItem
from .raw_client import AsyncRawCampaignFoldersClient, RawCampaignFoldersClient
from .types.get_campaign_folders_response import GetCampaignFoldersResponse
from .types.update_campaign_folders_response import UpdateCampaignFoldersResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CampaignFoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCampaignFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCampaignFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCampaignFoldersClient
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
    ) -> SyncPager[CampaignFoldersFoldersItem, CampaignFolders]:
        """
        Get all folders used to organize campaigns.

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
        SyncPager[CampaignFoldersFoldersItem, CampaignFolders]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.campaign_folders.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fields=fields, exclude_fields=exclude_fields, count=count, offset=offset, request_options=request_options
        )

    def create(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> CampaignFolders:
        """
        Create a new campaign folder.

        Parameters
        ----------
        name : str
            Name to associate with the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFolders


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaign_folders.create(
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
    ) -> GetCampaignFoldersResponse:
        """
        Get information about a specific folder used to organize campaigns.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCampaignFoldersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaign_folders.get(
            folder_id="folder_id",
        )
        """
        _response = self._raw_client.get(
            folder_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete(self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific campaign folder, and mark all the campaigns in the folder as 'unfiled'.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

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
        client.campaign_folders.delete(
            folder_id="folder_id",
        )
        """
        _response = self._raw_client.delete(folder_id, request_options=request_options)
        return _response.data

    def update(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCampaignFoldersResponse:
        """
        Update a specific folder used to organize campaigns.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

        name : str
            Name to associate with the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCampaignFoldersResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.campaign_folders.update(
            folder_id="folder_id",
            name="name",
        )
        """
        _response = self._raw_client.update(folder_id, name=name, request_options=request_options)
        return _response.data


class AsyncCampaignFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCampaignFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCampaignFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCampaignFoldersClient
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
    ) -> AsyncPager[CampaignFoldersFoldersItem, CampaignFolders]:
        """
        Get all folders used to organize campaigns.

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
        AsyncPager[CampaignFoldersFoldersItem, CampaignFolders]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.campaign_folders.list()
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

    async def create(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> CampaignFolders:
        """
        Create a new campaign folder.

        Parameters
        ----------
        name : str
            Name to associate with the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignFolders


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaign_folders.create(
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
    ) -> GetCampaignFoldersResponse:
        """
        Get information about a specific folder used to organize campaigns.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCampaignFoldersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaign_folders.get(
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
        Delete a specific campaign folder, and mark all the campaigns in the folder as 'unfiled'.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

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
            await client.campaign_folders.delete(
                folder_id="folder_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(folder_id, request_options=request_options)
        return _response.data

    async def update(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCampaignFoldersResponse:
        """
        Update a specific folder used to organize campaigns.

        Parameters
        ----------
        folder_id : str
            The unique id for the campaign folder.

        name : str
            Name to associate with the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCampaignFoldersResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.campaign_folders.update(
                folder_id="folder_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(folder_id, name=name, request_options=request_options)
        return _response.data
