# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.batch_webhook import BatchWebhook
from .raw_client import AsyncRawBatchWebhooksClient, RawBatchWebhooksClient
from .types.list_batch_webhooks_response import ListBatchWebhooksResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BatchWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBatchWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBatchWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBatchWebhooksClient
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


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.batch_webhooks.list()
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
        url: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.batch_webhooks.create(
            url="http://yourdomain.com/webhook",
        )
        """
        _response = self._raw_client.create(url=url, enabled=enabled, request_options=request_options)
        return _response.data

    def get(
        self,
        batch_webhook_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.batch_webhooks.get(
            batch_webhook_id="batch_webhook_id",
        )
        """
        _response = self._raw_client.get(
            batch_webhook_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete(self, batch_webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.batch_webhooks.delete(
            batch_webhook_id="batch_webhook_id",
        )
        """
        _response = self._raw_client.delete(batch_webhook_id, request_options=request_options)
        return _response.data

    def update(
        self,
        batch_webhook_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.batch_webhooks.update(
            batch_webhook_id="batch_webhook_id",
        )
        """
        _response = self._raw_client.update(batch_webhook_id, enabled=enabled, url=url, request_options=request_options)
        return _response.data


class AsyncBatchWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBatchWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBatchWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBatchWebhooksClient
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


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.batch_webhooks.list()
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
        url: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.batch_webhooks.create(
                url="http://yourdomain.com/webhook",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(url=url, enabled=enabled, request_options=request_options)
        return _response.data

    async def get(
        self,
        batch_webhook_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.batch_webhooks.get(
                batch_webhook_id="batch_webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            batch_webhook_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete(self, batch_webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.batch_webhooks.delete(
                batch_webhook_id="batch_webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(batch_webhook_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        batch_webhook_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchWebhook:
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
        BatchWebhook


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.batch_webhooks.update(
                batch_webhook_id="batch_webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            batch_webhook_id, enabled=enabled, url=url, request_options=request_options
        )
        return _response.data
