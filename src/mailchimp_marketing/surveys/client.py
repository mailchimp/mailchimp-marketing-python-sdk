# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.campaign import Campaign
from .raw_client import AsyncRawSurveysClient, RawSurveysClient


class SurveysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSurveysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSurveysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSurveysClient
        """
        return self._raw_client

    def create_list_survey_action_create_email(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Campaign:
        """
        Utilize the List ID and Survey ID to generate a Campaign that links to your survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign
            Campaign Instance

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.surveys.create_list_survey_action_create_email(
            list_id="list_id",
            survey_id="survey_id",
        )
        """
        _response = self._raw_client.create_list_survey_action_create_email(
            list_id, survey_id, request_options=request_options
        )
        return _response.data

    def create_list_survey_action_publish(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Publish a survey that is in draft, unpublished, or has been previously published and edited.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Survey Published

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.surveys.create_list_survey_action_publish(
            list_id="list_id",
            survey_id="survey_id",
        )
        """
        _response = self._raw_client.create_list_survey_action_publish(
            list_id, survey_id, request_options=request_options
        )
        return _response.data

    def create_list_survey_action_unpublish(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Unpublish a survey that has been published.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Survey Instance

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.surveys.create_list_survey_action_unpublish(
            list_id="list_id",
            survey_id="survey_id",
        )
        """
        _response = self._raw_client.create_list_survey_action_unpublish(
            list_id, survey_id, request_options=request_options
        )
        return _response.data


class AsyncSurveysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSurveysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSurveysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSurveysClient
        """
        return self._raw_client

    async def create_list_survey_action_create_email(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Campaign:
        """
        Utilize the List ID and Survey ID to generate a Campaign that links to your survey.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Campaign
            Campaign Instance

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.surveys.create_list_survey_action_create_email(
                list_id="list_id",
                survey_id="survey_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_list_survey_action_create_email(
            list_id, survey_id, request_options=request_options
        )
        return _response.data

    async def create_list_survey_action_publish(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Publish a survey that is in draft, unpublished, or has been previously published and edited.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Survey Published

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.surveys.create_list_survey_action_publish(
                list_id="list_id",
                survey_id="survey_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_list_survey_action_publish(
            list_id, survey_id, request_options=request_options
        )
        return _response.data

    async def create_list_survey_action_unpublish(
        self, list_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Unpublish a survey that has been published.

        Parameters
        ----------
        list_id : str
            The unique ID for the list.

        survey_id : str
            The ID of the survey.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Survey Instance

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.surveys.create_list_survey_action_unpublish(
                list_id="list_id",
                survey_id="survey_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_list_survey_action_unpublish(
            list_id, survey_id, request_options=request_options
        )
        return _response.data
