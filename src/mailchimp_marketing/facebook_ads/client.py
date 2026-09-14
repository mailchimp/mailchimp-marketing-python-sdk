# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.facebook_ads import FacebookAds
from .raw_client import AsyncRawFacebookAdsClient, RawFacebookAdsClient
from .types.list_facebook_ads_request_sort_dir import ListFacebookAdsRequestSortDir
from .types.list_facebook_ads_request_sort_field import ListFacebookAdsRequestSortField
from .types.list_facebook_ads_response import ListFacebookAdsResponse


class FacebookAdsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFacebookAdsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFacebookAdsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFacebookAdsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_field: typing.Optional[ListFacebookAdsRequestSortField] = None,
        sort_dir: typing.Optional[ListFacebookAdsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[FacebookAds, ListFacebookAdsResponse]:
        """
        Get list of Facebook ads.

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

        sort_field : typing.Optional[ListFacebookAdsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFacebookAdsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[FacebookAds, ListFacebookAdsResponse]
            List of Facebook Ad Instances

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.facebook_ads.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            sort_field=sort_field,
            sort_dir=sort_dir,
            request_options=request_options,
        )

    def get(
        self,
        outreach_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FacebookAds:
        """
        Get details of a Facebook ad.

        Parameters
        ----------
        outreach_id : str
            The outreach id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FacebookAds
            Facebook Ad Instance

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.facebook_ads.get(
            outreach_id="outreach_id",
        )
        """
        _response = self._raw_client.get(
            outreach_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data


class AsyncFacebookAdsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFacebookAdsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFacebookAdsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFacebookAdsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_field: typing.Optional[ListFacebookAdsRequestSortField] = None,
        sort_dir: typing.Optional[ListFacebookAdsRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[FacebookAds, ListFacebookAdsResponse]:
        """
        Get list of Facebook ads.

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

        sort_field : typing.Optional[ListFacebookAdsRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFacebookAdsRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[FacebookAds, ListFacebookAdsResponse]
            List of Facebook Ad Instances

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.facebook_ads.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            sort_field=sort_field,
            sort_dir=sort_dir,
            request_options=request_options,
        )

    async def get(
        self,
        outreach_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FacebookAds:
        """
        Get details of a Facebook ad.

        Parameters
        ----------
        outreach_id : str
            The outreach id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FacebookAds
            Facebook Ad Instance

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.facebook_ads.get(
                outreach_id="outreach_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            outreach_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data
