# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.conversation import Conversation
from ..types.conversation_message import ConversationMessage
from .raw_client import AsyncRawConversationsClient, RawConversationsClient
from .types.list_conversations_request_has_unread_messages import ListConversationsRequestHasUnreadMessages
from .types.list_conversations_response import ListConversationsResponse
from .types.list_messages_conversations_request_is_read import ListMessagesConversationsRequestIsRead
from .types.list_messages_conversations_response import ListMessagesConversationsResponse


class ConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        has_unread_messages: typing.Optional[ListConversationsRequestHasUnreadMessages] = None,
        list_id: typing.Optional[str] = None,
        campaign_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Conversation, ListConversationsResponse]:
        """
        Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

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

        has_unread_messages : typing.Optional[ListConversationsRequestHasUnreadMessages]
            Whether the conversation has any unread messages.

        list_id : typing.Optional[str]
            The unique id for the list.

        campaign_id : typing.Optional[str]
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Conversation, ListConversationsResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.conversations.list()
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
            has_unread_messages=has_unread_messages,
            list_id=list_id,
            campaign_id=campaign_id,
            request_options=request_options,
        )

    def get(
        self,
        conversation_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.conversations.get(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.get(
            conversation_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def list_messages(
        self,
        conversation_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_read: typing.Optional[ListMessagesConversationsRequestIsRead] = None,
        before_timestamp: typing.Optional[dt.datetime] = None,
        since_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMessagesConversationsResponse:
        """
        Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        is_read : typing.Optional[ListMessagesConversationsRequestIsRead]
            Whether a conversation message has been marked as read.

        before_timestamp : typing.Optional[dt.datetime]
            Restrict the response to messages created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_timestamp : typing.Optional[dt.datetime]
            Restrict the response to messages created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMessagesConversationsResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.conversations.list_messages(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.list_messages(
            conversation_id,
            fields=fields,
            exclude_fields=exclude_fields,
            is_read=is_read,
            before_timestamp=before_timestamp,
            since_timestamp=since_timestamp,
            request_options=request_options,
        )
        return _response.data

    def get_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMessage:
        """
        Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        message_id : str
            The unique id for the conversation message.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMessage


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.conversations.get_message(
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_message(
            conversation_id, message_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data


class AsyncConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        has_unread_messages: typing.Optional[ListConversationsRequestHasUnreadMessages] = None,
        list_id: typing.Optional[str] = None,
        campaign_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Conversation, ListConversationsResponse]:
        """
        Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

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

        has_unread_messages : typing.Optional[ListConversationsRequestHasUnreadMessages]
            Whether the conversation has any unread messages.

        list_id : typing.Optional[str]
            The unique id for the list.

        campaign_id : typing.Optional[str]
            The unique id for the campaign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Conversation, ListConversationsResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.conversations.list()
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
            has_unread_messages=has_unread_messages,
            list_id=list_id,
            campaign_id=campaign_id,
            request_options=request_options,
        )

    async def get(
        self,
        conversation_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            conversation_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def list_messages(
        self,
        conversation_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_read: typing.Optional[ListMessagesConversationsRequestIsRead] = None,
        before_timestamp: typing.Optional[dt.datetime] = None,
        since_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMessagesConversationsResponse:
        """
        Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        is_read : typing.Optional[ListMessagesConversationsRequestIsRead]
            Whether a conversation message has been marked as read.

        before_timestamp : typing.Optional[dt.datetime]
            Restrict the response to messages created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_timestamp : typing.Optional[dt.datetime]
            Restrict the response to messages created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMessagesConversationsResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.list_messages(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages(
            conversation_id,
            fields=fields,
            exclude_fields=exclude_fields,
            is_read=is_read,
            before_timestamp=before_timestamp,
            since_timestamp=since_timestamp,
            request_options=request_options,
        )
        return _response.data

    async def get_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMessage:
        """
        Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.

        Parameters
        ----------
        conversation_id : str
            The unique id for the conversation.

        message_id : str
            The unique id for the conversation message.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMessage


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get_message(
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message(
            conversation_id, message_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data
