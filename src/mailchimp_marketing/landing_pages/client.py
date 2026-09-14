# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.landing_page import LandingPage
from .raw_client import AsyncRawLandingPagesClient, RawLandingPagesClient
from .types.create_landing_pages_request_tracking import CreateLandingPagesRequestTracking
from .types.create_landing_pages_request_type import CreateLandingPagesRequestType
from .types.list_content_landing_pages_response import ListContentLandingPagesResponse
from .types.list_landing_pages_request_sort_dir import ListLandingPagesRequestSortDir
from .types.list_landing_pages_request_sort_field import ListLandingPagesRequestSortField
from .types.list_landing_pages_response import ListLandingPagesResponse
from .types.update_landing_pages_request_tracking import UpdateLandingPagesRequestTracking

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LandingPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLandingPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLandingPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLandingPagesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        sort_dir: typing.Optional[ListLandingPagesRequestSortDir] = None,
        sort_field: typing.Optional[ListLandingPagesRequestSortField] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListLandingPagesResponse:
        """
        Get all landing pages.

        Parameters
        ----------
        sort_dir : typing.Optional[ListLandingPagesRequestSortDir]
            Determines the order direction for sorted results.

        sort_field : typing.Optional[ListLandingPagesRequestSortField]
            Returns files sorted by the specified field.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLandingPagesResponse
            Landing Pages Collection

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.landing_pages.list()
        """
        _response = self._raw_client.list(
            sort_dir=sort_dir,
            sort_field=sort_field,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        use_default_list: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        tracking: typing.Optional[CreateLandingPagesRequestTracking] = OMIT,
        type: typing.Optional[CreateLandingPagesRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Create an unpublished and contentless Mailchimp landing page.

        Parameters
        ----------
        use_default_list : typing.Optional[bool]
            Will create the Landing Page using the account's Default List instead of requiring a list_id.

        description : typing.Optional[str]
            The description of this landing page.

        list_id : typing.Optional[str]
            The list's ID associated with this landing page.

        name : typing.Optional[str]
            The name of this landing page.

        store_id : typing.Optional[str]
            The ID of the store associated with this landing page.

        template_id : typing.Optional[int]
            The template_id of this landing page.

        title : typing.Optional[str]
            The title of this landing page seen in the browser's title bar.

        tracking : typing.Optional[CreateLandingPagesRequestTracking]
            The tracking settings applied to this landing page.

        type : typing.Optional[CreateLandingPagesRequestType]
            The type of template the landing page has.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.landing_pages.create()
        """
        _response = self._raw_client.create(
            use_default_list=use_default_list,
            description=description,
            list_id=list_id,
            name=name,
            store_id=store_id,
            template_id=template_id,
            title=title,
            tracking=tracking,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        page_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Get information about a specific page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
            Landing Pages Instance

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.landing_pages.get(
            page_id="page_id",
        )
        """
        _response = self._raw_client.get(
            page_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete(self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
        client.landing_pages.delete(
            page_id="page_id",
        )
        """
        _response = self._raw_client.delete(page_id, request_options=request_options)
        return _response.data

    def update(
        self,
        page_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tracking: typing.Optional[UpdateLandingPagesRequestTracking] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Update a landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        description : typing.Optional[str]
            The description of this landing page.

        list_id : typing.Optional[str]
            The list's ID associated with this landing page.

        name : typing.Optional[str]
            The name of this landing page.

        store_id : typing.Optional[str]
            The ID of the store associated with this landing page.

        title : typing.Optional[str]
            The title of this landing page seen in the browser's title bar.

        tracking : typing.Optional[UpdateLandingPagesRequestTracking]
            The tracking settings applied to this landing page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.landing_pages.update(
            page_id="page_id",
        )
        """
        _response = self._raw_client.update(
            page_id,
            description=description,
            list_id=list_id,
            name=name,
            store_id=store_id,
            title=title,
            tracking=tracking,
            request_options=request_options,
        )
        return _response.data

    def create_action_publish(self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Publish a landing page that is in draft, unpublished, or has been previously published and edited.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
        client.landing_pages.create_action_publish(
            page_id="page_id",
        )
        """
        _response = self._raw_client.create_action_publish(page_id, request_options=request_options)
        return _response.data

    def create_action_unpublish(self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unpublish a landing page that is in draft or has been published.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
        client.landing_pages.create_action_unpublish(
            page_id="page_id",
        )
        """
        _response = self._raw_client.create_action_unpublish(page_id, request_options=request_options)
        return _response.data

    def list_content(
        self,
        page_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListContentLandingPagesResponse:
        """
        Get the the HTML for your landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListContentLandingPagesResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.landing_pages.list_content(
            page_id="page_id",
        )
        """
        _response = self._raw_client.list_content(
            page_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data


class AsyncLandingPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLandingPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLandingPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLandingPagesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        sort_dir: typing.Optional[ListLandingPagesRequestSortDir] = None,
        sort_field: typing.Optional[ListLandingPagesRequestSortField] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListLandingPagesResponse:
        """
        Get all landing pages.

        Parameters
        ----------
        sort_dir : typing.Optional[ListLandingPagesRequestSortDir]
            Determines the order direction for sorted results.

        sort_field : typing.Optional[ListLandingPagesRequestSortField]
            Returns files sorted by the specified field.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLandingPagesResponse
            Landing Pages Collection

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.landing_pages.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            sort_dir=sort_dir,
            sort_field=sort_field,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        use_default_list: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        tracking: typing.Optional[CreateLandingPagesRequestTracking] = OMIT,
        type: typing.Optional[CreateLandingPagesRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Create an unpublished and contentless Mailchimp landing page.

        Parameters
        ----------
        use_default_list : typing.Optional[bool]
            Will create the Landing Page using the account's Default List instead of requiring a list_id.

        description : typing.Optional[str]
            The description of this landing page.

        list_id : typing.Optional[str]
            The list's ID associated with this landing page.

        name : typing.Optional[str]
            The name of this landing page.

        store_id : typing.Optional[str]
            The ID of the store associated with this landing page.

        template_id : typing.Optional[int]
            The template_id of this landing page.

        title : typing.Optional[str]
            The title of this landing page seen in the browser's title bar.

        tracking : typing.Optional[CreateLandingPagesRequestTracking]
            The tracking settings applied to this landing page.

        type : typing.Optional[CreateLandingPagesRequestType]
            The type of template the landing page has.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.landing_pages.create()


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            use_default_list=use_default_list,
            description=description,
            list_id=list_id,
            name=name,
            store_id=store_id,
            template_id=template_id,
            title=title,
            tracking=tracking,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        page_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Get information about a specific page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
            Landing Pages Instance

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.landing_pages.get(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            page_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete(self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
            await client.landing_pages.delete(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(page_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        page_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        list_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tracking: typing.Optional[UpdateLandingPagesRequestTracking] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LandingPage:
        """
        Update a landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        description : typing.Optional[str]
            The description of this landing page.

        list_id : typing.Optional[str]
            The list's ID associated with this landing page.

        name : typing.Optional[str]
            The name of this landing page.

        store_id : typing.Optional[str]
            The ID of the store associated with this landing page.

        title : typing.Optional[str]
            The title of this landing page seen in the browser's title bar.

        tracking : typing.Optional[UpdateLandingPagesRequestTracking]
            The tracking settings applied to this landing page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.landing_pages.update(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            page_id,
            description=description,
            list_id=list_id,
            name=name,
            store_id=store_id,
            title=title,
            tracking=tracking,
            request_options=request_options,
        )
        return _response.data

    async def create_action_publish(
        self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Publish a landing page that is in draft, unpublished, or has been previously published and edited.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
            await client.landing_pages.create_action_publish(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_publish(page_id, request_options=request_options)
        return _response.data

    async def create_action_unpublish(
        self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unpublish a landing page that is in draft or has been published.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

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
            await client.landing_pages.create_action_unpublish(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action_unpublish(page_id, request_options=request_options)
        return _response.data

    async def list_content(
        self,
        page_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListContentLandingPagesResponse:
        """
        Get the the HTML for your landing page.

        Parameters
        ----------
        page_id : str
            The unique id for the page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListContentLandingPagesResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.landing_pages.list_content(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_content(
            page_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data
