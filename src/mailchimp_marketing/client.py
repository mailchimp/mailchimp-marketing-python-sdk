# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import MailchimpClientEnvironment

if typing.TYPE_CHECKING:
    from .account_exports.client import AccountExportsClient, AsyncAccountExportsClient
    from .activity_feed.client import ActivityFeedClient, AsyncActivityFeedClient
    from .authorized_apps.client import AsyncAuthorizedAppsClient, AuthorizedAppsClient
    from .automations.client import AsyncAutomationsClient, AutomationsClient
    from .batch_webhooks.client import AsyncBatchWebhooksClient, BatchWebhooksClient
    from .batches.client import AsyncBatchesClient, BatchesClient
    from .campaign_folders.client import AsyncCampaignFoldersClient, CampaignFoldersClient
    from .campaigns.client import AsyncCampaignsClient, CampaignsClient
    from .connected_sites.client import AsyncConnectedSitesClient, ConnectedSitesClient
    from .conversations.client import AsyncConversationsClient, ConversationsClient
    from .customer_journeys.client import AsyncCustomerJourneysClient, CustomerJourneysClient
    from .ecommerce.client import AsyncEcommerceClient, EcommerceClient
    from .facebook_ads.client import AsyncFacebookAdsClient, FacebookAdsClient
    from .file_manager.client import AsyncFileManagerClient, FileManagerClient
    from .landing_pages.client import AsyncLandingPagesClient, LandingPagesClient
    from .lists.client import AsyncListsClient, ListsClient
    from .ping.client import AsyncPingClient, PingClient
    from .reporting.client import AsyncReportingClient, ReportingClient
    from .reports.client import AsyncReportsClient, ReportsClient
    from .root.client import AsyncRootClient, RootClient
    from .search_campaigns.client import AsyncSearchCampaignsClient, SearchCampaignsClient
    from .search_members.client import AsyncSearchMembersClient, SearchMembersClient
    from .sms_campaigns.client import AsyncSmsCampaignsClient, SmsCampaignsClient
    from .surveys.client import AsyncSurveysClient, SurveysClient
    from .template_folders.client import AsyncTemplateFoldersClient, TemplateFoldersClient
    from .templates.client import AsyncTemplatesClient, TemplatesClient
    from .verified_domains.client import AsyncVerifiedDomainsClient, VerifiedDomainsClient


class MailchimpClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MailchimpClientEnvironment
        The environment to use for requests from the client. from .environment import MailchimpClientEnvironment



        Defaults to MailchimpClientEnvironment.DEFAULT



    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from mailchimp_marketing import MailchimpClient

    client = MailchimpClient(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MailchimpClientEnvironment = MailchimpClientEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._root: typing.Optional[RootClient] = None
        self._account_exports: typing.Optional[AccountExportsClient] = None
        self._activity_feed: typing.Optional[ActivityFeedClient] = None
        self._authorized_apps: typing.Optional[AuthorizedAppsClient] = None
        self._automations: typing.Optional[AutomationsClient] = None
        self._batch_webhooks: typing.Optional[BatchWebhooksClient] = None
        self._batches: typing.Optional[BatchesClient] = None
        self._campaign_folders: typing.Optional[CampaignFoldersClient] = None
        self._campaigns: typing.Optional[CampaignsClient] = None
        self._connected_sites: typing.Optional[ConnectedSitesClient] = None
        self._conversations: typing.Optional[ConversationsClient] = None
        self._customer_journeys: typing.Optional[CustomerJourneysClient] = None
        self._ecommerce: typing.Optional[EcommerceClient] = None
        self._facebook_ads: typing.Optional[FacebookAdsClient] = None
        self._file_manager: typing.Optional[FileManagerClient] = None
        self._landing_pages: typing.Optional[LandingPagesClient] = None
        self._lists: typing.Optional[ListsClient] = None
        self._surveys: typing.Optional[SurveysClient] = None
        self._ping: typing.Optional[PingClient] = None
        self._reporting: typing.Optional[ReportingClient] = None
        self._reports: typing.Optional[ReportsClient] = None
        self._search_campaigns: typing.Optional[SearchCampaignsClient] = None
        self._sms_campaigns: typing.Optional[SmsCampaignsClient] = None
        self._search_members: typing.Optional[SearchMembersClient] = None
        self._template_folders: typing.Optional[TemplateFoldersClient] = None
        self._templates: typing.Optional[TemplatesClient] = None
        self._verified_domains: typing.Optional[VerifiedDomainsClient] = None

    @property
    def root(self):
        if self._root is None:
            from .root.client import RootClient  # noqa: E402

            self._root = RootClient(client_wrapper=self._client_wrapper)
        return self._root

    @property
    def account_exports(self):
        if self._account_exports is None:
            from .account_exports.client import AccountExportsClient  # noqa: E402

            self._account_exports = AccountExportsClient(client_wrapper=self._client_wrapper)
        return self._account_exports

    @property
    def activity_feed(self):
        if self._activity_feed is None:
            from .activity_feed.client import ActivityFeedClient  # noqa: E402

            self._activity_feed = ActivityFeedClient(client_wrapper=self._client_wrapper)
        return self._activity_feed

    @property
    def authorized_apps(self):
        if self._authorized_apps is None:
            from .authorized_apps.client import AuthorizedAppsClient  # noqa: E402

            self._authorized_apps = AuthorizedAppsClient(client_wrapper=self._client_wrapper)
        return self._authorized_apps

    @property
    def automations(self):
        if self._automations is None:
            from .automations.client import AutomationsClient  # noqa: E402

            self._automations = AutomationsClient(client_wrapper=self._client_wrapper)
        return self._automations

    @property
    def batch_webhooks(self):
        if self._batch_webhooks is None:
            from .batch_webhooks.client import BatchWebhooksClient  # noqa: E402

            self._batch_webhooks = BatchWebhooksClient(client_wrapper=self._client_wrapper)
        return self._batch_webhooks

    @property
    def batches(self):
        if self._batches is None:
            from .batches.client import BatchesClient  # noqa: E402

            self._batches = BatchesClient(client_wrapper=self._client_wrapper)
        return self._batches

    @property
    def campaign_folders(self):
        if self._campaign_folders is None:
            from .campaign_folders.client import CampaignFoldersClient  # noqa: E402

            self._campaign_folders = CampaignFoldersClient(client_wrapper=self._client_wrapper)
        return self._campaign_folders

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .campaigns.client import CampaignsClient  # noqa: E402

            self._campaigns = CampaignsClient(client_wrapper=self._client_wrapper)
        return self._campaigns

    @property
    def connected_sites(self):
        if self._connected_sites is None:
            from .connected_sites.client import ConnectedSitesClient  # noqa: E402

            self._connected_sites = ConnectedSitesClient(client_wrapper=self._client_wrapper)
        return self._connected_sites

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import ConversationsClient  # noqa: E402

            self._conversations = ConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def customer_journeys(self):
        if self._customer_journeys is None:
            from .customer_journeys.client import CustomerJourneysClient  # noqa: E402

            self._customer_journeys = CustomerJourneysClient(client_wrapper=self._client_wrapper)
        return self._customer_journeys

    @property
    def ecommerce(self):
        if self._ecommerce is None:
            from .ecommerce.client import EcommerceClient  # noqa: E402

            self._ecommerce = EcommerceClient(client_wrapper=self._client_wrapper)
        return self._ecommerce

    @property
    def facebook_ads(self):
        if self._facebook_ads is None:
            from .facebook_ads.client import FacebookAdsClient  # noqa: E402

            self._facebook_ads = FacebookAdsClient(client_wrapper=self._client_wrapper)
        return self._facebook_ads

    @property
    def file_manager(self):
        if self._file_manager is None:
            from .file_manager.client import FileManagerClient  # noqa: E402

            self._file_manager = FileManagerClient(client_wrapper=self._client_wrapper)
        return self._file_manager

    @property
    def landing_pages(self):
        if self._landing_pages is None:
            from .landing_pages.client import LandingPagesClient  # noqa: E402

            self._landing_pages = LandingPagesClient(client_wrapper=self._client_wrapper)
        return self._landing_pages

    @property
    def lists(self):
        if self._lists is None:
            from .lists.client import ListsClient  # noqa: E402

            self._lists = ListsClient(client_wrapper=self._client_wrapper)
        return self._lists

    @property
    def surveys(self):
        if self._surveys is None:
            from .surveys.client import SurveysClient  # noqa: E402

            self._surveys = SurveysClient(client_wrapper=self._client_wrapper)
        return self._surveys

    @property
    def ping(self):
        if self._ping is None:
            from .ping.client import PingClient  # noqa: E402

            self._ping = PingClient(client_wrapper=self._client_wrapper)
        return self._ping

    @property
    def reporting(self):
        if self._reporting is None:
            from .reporting.client import ReportingClient  # noqa: E402

            self._reporting = ReportingClient(client_wrapper=self._client_wrapper)
        return self._reporting

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import ReportsClient  # noqa: E402

            self._reports = ReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def search_campaigns(self):
        if self._search_campaigns is None:
            from .search_campaigns.client import SearchCampaignsClient  # noqa: E402

            self._search_campaigns = SearchCampaignsClient(client_wrapper=self._client_wrapper)
        return self._search_campaigns

    @property
    def sms_campaigns(self):
        if self._sms_campaigns is None:
            from .sms_campaigns.client import SmsCampaignsClient  # noqa: E402

            self._sms_campaigns = SmsCampaignsClient(client_wrapper=self._client_wrapper)
        return self._sms_campaigns

    @property
    def search_members(self):
        if self._search_members is None:
            from .search_members.client import SearchMembersClient  # noqa: E402

            self._search_members = SearchMembersClient(client_wrapper=self._client_wrapper)
        return self._search_members

    @property
    def template_folders(self):
        if self._template_folders is None:
            from .template_folders.client import TemplateFoldersClient  # noqa: E402

            self._template_folders = TemplateFoldersClient(client_wrapper=self._client_wrapper)
        return self._template_folders

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import TemplatesClient  # noqa: E402

            self._templates = TemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def verified_domains(self):
        if self._verified_domains is None:
            from .verified_domains.client import VerifiedDomainsClient  # noqa: E402

            self._verified_domains = VerifiedDomainsClient(client_wrapper=self._client_wrapper)
        return self._verified_domains


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp  # type: ignore[import-not-found]
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncMailchimpClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MailchimpClientEnvironment
        The environment to use for requests from the client. from .environment import MailchimpClientEnvironment



        Defaults to MailchimpClientEnvironment.DEFAULT



    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from mailchimp_marketing import AsyncMailchimpClient

    client = AsyncMailchimpClient(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MailchimpClientEnvironment = MailchimpClientEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._root: typing.Optional[AsyncRootClient] = None
        self._account_exports: typing.Optional[AsyncAccountExportsClient] = None
        self._activity_feed: typing.Optional[AsyncActivityFeedClient] = None
        self._authorized_apps: typing.Optional[AsyncAuthorizedAppsClient] = None
        self._automations: typing.Optional[AsyncAutomationsClient] = None
        self._batch_webhooks: typing.Optional[AsyncBatchWebhooksClient] = None
        self._batches: typing.Optional[AsyncBatchesClient] = None
        self._campaign_folders: typing.Optional[AsyncCampaignFoldersClient] = None
        self._campaigns: typing.Optional[AsyncCampaignsClient] = None
        self._connected_sites: typing.Optional[AsyncConnectedSitesClient] = None
        self._conversations: typing.Optional[AsyncConversationsClient] = None
        self._customer_journeys: typing.Optional[AsyncCustomerJourneysClient] = None
        self._ecommerce: typing.Optional[AsyncEcommerceClient] = None
        self._facebook_ads: typing.Optional[AsyncFacebookAdsClient] = None
        self._file_manager: typing.Optional[AsyncFileManagerClient] = None
        self._landing_pages: typing.Optional[AsyncLandingPagesClient] = None
        self._lists: typing.Optional[AsyncListsClient] = None
        self._surveys: typing.Optional[AsyncSurveysClient] = None
        self._ping: typing.Optional[AsyncPingClient] = None
        self._reporting: typing.Optional[AsyncReportingClient] = None
        self._reports: typing.Optional[AsyncReportsClient] = None
        self._search_campaigns: typing.Optional[AsyncSearchCampaignsClient] = None
        self._sms_campaigns: typing.Optional[AsyncSmsCampaignsClient] = None
        self._search_members: typing.Optional[AsyncSearchMembersClient] = None
        self._template_folders: typing.Optional[AsyncTemplateFoldersClient] = None
        self._templates: typing.Optional[AsyncTemplatesClient] = None
        self._verified_domains: typing.Optional[AsyncVerifiedDomainsClient] = None

    @property
    def root(self):
        if self._root is None:
            from .root.client import AsyncRootClient  # noqa: E402

            self._root = AsyncRootClient(client_wrapper=self._client_wrapper)
        return self._root

    @property
    def account_exports(self):
        if self._account_exports is None:
            from .account_exports.client import AsyncAccountExportsClient  # noqa: E402

            self._account_exports = AsyncAccountExportsClient(client_wrapper=self._client_wrapper)
        return self._account_exports

    @property
    def activity_feed(self):
        if self._activity_feed is None:
            from .activity_feed.client import AsyncActivityFeedClient  # noqa: E402

            self._activity_feed = AsyncActivityFeedClient(client_wrapper=self._client_wrapper)
        return self._activity_feed

    @property
    def authorized_apps(self):
        if self._authorized_apps is None:
            from .authorized_apps.client import AsyncAuthorizedAppsClient  # noqa: E402

            self._authorized_apps = AsyncAuthorizedAppsClient(client_wrapper=self._client_wrapper)
        return self._authorized_apps

    @property
    def automations(self):
        if self._automations is None:
            from .automations.client import AsyncAutomationsClient  # noqa: E402

            self._automations = AsyncAutomationsClient(client_wrapper=self._client_wrapper)
        return self._automations

    @property
    def batch_webhooks(self):
        if self._batch_webhooks is None:
            from .batch_webhooks.client import AsyncBatchWebhooksClient  # noqa: E402

            self._batch_webhooks = AsyncBatchWebhooksClient(client_wrapper=self._client_wrapper)
        return self._batch_webhooks

    @property
    def batches(self):
        if self._batches is None:
            from .batches.client import AsyncBatchesClient  # noqa: E402

            self._batches = AsyncBatchesClient(client_wrapper=self._client_wrapper)
        return self._batches

    @property
    def campaign_folders(self):
        if self._campaign_folders is None:
            from .campaign_folders.client import AsyncCampaignFoldersClient  # noqa: E402

            self._campaign_folders = AsyncCampaignFoldersClient(client_wrapper=self._client_wrapper)
        return self._campaign_folders

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .campaigns.client import AsyncCampaignsClient  # noqa: E402

            self._campaigns = AsyncCampaignsClient(client_wrapper=self._client_wrapper)
        return self._campaigns

    @property
    def connected_sites(self):
        if self._connected_sites is None:
            from .connected_sites.client import AsyncConnectedSitesClient  # noqa: E402

            self._connected_sites = AsyncConnectedSitesClient(client_wrapper=self._client_wrapper)
        return self._connected_sites

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import AsyncConversationsClient  # noqa: E402

            self._conversations = AsyncConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def customer_journeys(self):
        if self._customer_journeys is None:
            from .customer_journeys.client import AsyncCustomerJourneysClient  # noqa: E402

            self._customer_journeys = AsyncCustomerJourneysClient(client_wrapper=self._client_wrapper)
        return self._customer_journeys

    @property
    def ecommerce(self):
        if self._ecommerce is None:
            from .ecommerce.client import AsyncEcommerceClient  # noqa: E402

            self._ecommerce = AsyncEcommerceClient(client_wrapper=self._client_wrapper)
        return self._ecommerce

    @property
    def facebook_ads(self):
        if self._facebook_ads is None:
            from .facebook_ads.client import AsyncFacebookAdsClient  # noqa: E402

            self._facebook_ads = AsyncFacebookAdsClient(client_wrapper=self._client_wrapper)
        return self._facebook_ads

    @property
    def file_manager(self):
        if self._file_manager is None:
            from .file_manager.client import AsyncFileManagerClient  # noqa: E402

            self._file_manager = AsyncFileManagerClient(client_wrapper=self._client_wrapper)
        return self._file_manager

    @property
    def landing_pages(self):
        if self._landing_pages is None:
            from .landing_pages.client import AsyncLandingPagesClient  # noqa: E402

            self._landing_pages = AsyncLandingPagesClient(client_wrapper=self._client_wrapper)
        return self._landing_pages

    @property
    def lists(self):
        if self._lists is None:
            from .lists.client import AsyncListsClient  # noqa: E402

            self._lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        return self._lists

    @property
    def surveys(self):
        if self._surveys is None:
            from .surveys.client import AsyncSurveysClient  # noqa: E402

            self._surveys = AsyncSurveysClient(client_wrapper=self._client_wrapper)
        return self._surveys

    @property
    def ping(self):
        if self._ping is None:
            from .ping.client import AsyncPingClient  # noqa: E402

            self._ping = AsyncPingClient(client_wrapper=self._client_wrapper)
        return self._ping

    @property
    def reporting(self):
        if self._reporting is None:
            from .reporting.client import AsyncReportingClient  # noqa: E402

            self._reporting = AsyncReportingClient(client_wrapper=self._client_wrapper)
        return self._reporting

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import AsyncReportsClient  # noqa: E402

            self._reports = AsyncReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def search_campaigns(self):
        if self._search_campaigns is None:
            from .search_campaigns.client import AsyncSearchCampaignsClient  # noqa: E402

            self._search_campaigns = AsyncSearchCampaignsClient(client_wrapper=self._client_wrapper)
        return self._search_campaigns

    @property
    def sms_campaigns(self):
        if self._sms_campaigns is None:
            from .sms_campaigns.client import AsyncSmsCampaignsClient  # noqa: E402

            self._sms_campaigns = AsyncSmsCampaignsClient(client_wrapper=self._client_wrapper)
        return self._sms_campaigns

    @property
    def search_members(self):
        if self._search_members is None:
            from .search_members.client import AsyncSearchMembersClient  # noqa: E402

            self._search_members = AsyncSearchMembersClient(client_wrapper=self._client_wrapper)
        return self._search_members

    @property
    def template_folders(self):
        if self._template_folders is None:
            from .template_folders.client import AsyncTemplateFoldersClient  # noqa: E402

            self._template_folders = AsyncTemplateFoldersClient(client_wrapper=self._client_wrapper)
        return self._template_folders

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import AsyncTemplatesClient  # noqa: E402

            self._templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def verified_domains(self):
        if self._verified_domains is None:
            from .verified_domains.client import AsyncVerifiedDomainsClient  # noqa: E402

            self._verified_domains = AsyncVerifiedDomainsClient(client_wrapper=self._client_wrapper)
        return self._verified_domains


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MailchimpClientEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
