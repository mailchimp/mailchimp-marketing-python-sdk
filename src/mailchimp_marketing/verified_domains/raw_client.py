# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_action_verify_verified_domains_response import CreateActionVerifyVerifiedDomainsResponse
from .types.create_verified_domains_response import CreateVerifiedDomainsResponse
from .types.get_verified_domains_response import GetVerifiedDomainsResponse
from .types.list_verified_domains_response import ListVerifiedDomainsResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawVerifiedDomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListVerifiedDomainsResponse]:
        """
        Get all of the sending domains on the account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListVerifiedDomainsResponse]
            The domains on the account.
        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/verified-domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=ListVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self, *, verification_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateVerifiedDomainsResponse]:
        """
        Add a domain to the account.

        Parameters
        ----------
        verification_email : str
            The e-mail address at the domain you want to verify. This will receive a two-factor challenge to be used in the verify action.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateVerifiedDomainsResponse]
            The newly-created domain.
        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/verified-domains",
            method="POST",
            json={
                "verification_email": verification_email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=CreateVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, domain_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetVerifiedDomainsResponse]:
        """
        Get the details for a single domain on the account.

        Parameters
        ----------
        domain_name : str
            The domain name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetVerifiedDomainsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=GetVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, domain_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a verified domain from the account.

        Parameters
        ----------
        domain_name : str
            The domain name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_action_verify(
        self, domain_name: str, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateActionVerifyVerifiedDomainsResponse]:
        """
        Verify a domain for sending.

        Parameters
        ----------
        domain_name : str
            The domain name.

        code : str
            The code that was sent to the email address provided when adding a new domain to verify.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateActionVerifyVerifiedDomainsResponse]
            The domain being verified for sending.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}/actions/verify",
            method="POST",
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateActionVerifyVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=CreateActionVerifyVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVerifiedDomainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListVerifiedDomainsResponse]:
        """
        Get all of the sending domains on the account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListVerifiedDomainsResponse]
            The domains on the account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/verified-domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=ListVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self, *, verification_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateVerifiedDomainsResponse]:
        """
        Add a domain to the account.

        Parameters
        ----------
        verification_email : str
            The e-mail address at the domain you want to verify. This will receive a two-factor challenge to be used in the verify action.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateVerifiedDomainsResponse]
            The newly-created domain.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/verified-domains",
            method="POST",
            json={
                "verification_email": verification_email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=CreateVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, domain_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetVerifiedDomainsResponse]:
        """
        Get the details for a single domain on the account.

        Parameters
        ----------
        domain_name : str
            The domain name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetVerifiedDomainsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=GetVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, domain_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a verified domain from the account.

        Parameters
        ----------
        domain_name : str
            The domain name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_action_verify(
        self, domain_name: str, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateActionVerifyVerifiedDomainsResponse]:
        """
        Verify a domain for sending.

        Parameters
        ----------
        domain_name : str
            The domain name.

        code : str
            The code that was sent to the email address provided when adding a new domain to verify.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateActionVerifyVerifiedDomainsResponse]
            The domain being verified for sending.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/verified-domains/{encode_path_param(domain_name)}/actions/verify",
            method="POST",
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateActionVerifyVerifiedDomainsResponse,
                    parse_obj_as(
                        type_=CreateActionVerifyVerifiedDomainsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
