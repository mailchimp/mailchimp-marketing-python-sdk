# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.template_instance import TemplateInstance
from .types.list_default_content_templates_response import ListDefaultContentTemplatesResponse
from .types.list_templates_request_content_type import ListTemplatesRequestContentType
from .types.list_templates_request_sort_dir import ListTemplatesRequestSortDir
from .types.list_templates_request_sort_field import ListTemplatesRequestSortField
from .types.list_templates_response import ListTemplatesResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_by: typing.Optional[str] = None,
        since_date_created: typing.Optional[str] = None,
        before_date_created: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        sort_field: typing.Optional[ListTemplatesRequestSortField] = None,
        content_type: typing.Optional[ListTemplatesRequestContentType] = None,
        sort_dir: typing.Optional[ListTemplatesRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[TemplateInstance, ListTemplatesResponse]:
        """
        Get a list of an account's available templates.

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

        created_by : typing.Optional[str]
            The Mailchimp account user who created the template.

        since_date_created : typing.Optional[str]
            Restrict the response to templates created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_date_created : typing.Optional[str]
            Restrict the response to templates created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        type : typing.Optional[str]
            Limit results based on template type.

        category : typing.Optional[str]
            Limit results based on category.

        folder_id : typing.Optional[str]
            The unique folder id.

        sort_field : typing.Optional[ListTemplatesRequestSortField]
            Returns user templates sorted by the specified field.

        content_type : typing.Optional[ListTemplatesRequestContentType]
            Limit results based on how the template's content is put together. Only templates of type `user` can be filtered by `content_type`. If you want to retrieve saved templates created with the legacy email editor, then filter `content_type` to `template`. If you'd rather pull your saved templates for the new editor, filter to `multichannel`. For code your own templates, filter to `html`.

        sort_dir : typing.Optional[ListTemplatesRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[TemplateInstance, ListTemplatesResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/templates",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "created_by": created_by,
                "since_date_created": since_date_created,
                "before_date_created": before_date_created,
                "type": type,
                "category": category,
                "folder_id": folder_id,
                "sort_field": sort_field,
                "content_type": content_type,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListTemplatesResponse,
                    parse_obj_as(
                        type_=ListTemplatesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.templates
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list(
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    created_by=created_by,
                    since_date_created=since_date_created,
                    before_date_created=before_date_created,
                    type=type,
                    category=category,
                    folder_id=folder_id,
                    sort_field=sort_field,
                    content_type=content_type,
                    sort_dir=sort_dir,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        html: str,
        name: str,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateInstance]:
        """
        Create a new template for the account. Only Classic templates are supported.

        Parameters
        ----------
        html : str
            The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.

        name : str
            The name of the template.

        folder_id : typing.Optional[str]
            The id of the folder the template is currently in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateInstance]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/templates",
            method="POST",
            json={
                "folder_id": folder_id,
                "html": html,
                "name": name,
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
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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
        self,
        template_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateInstance]:
        """
        Get information about a specific template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateInstance]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
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

    def update(
        self,
        template_id: str,
        *,
        folder_id: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateInstance]:
        """
        Update the name, HTML, or `folder_id` of an existing template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        folder_id : typing.Optional[str]
            The id of the folder the template is currently in.

        html : typing.Optional[str]
            The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.

        name : typing.Optional[str]
            The name of the template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateInstance]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
            method="PATCH",
            json={
                "folder_id": folder_id,
                "html": html,
                "name": name,
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
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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

    def list_default_content(
        self,
        template_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDefaultContentTemplatesResponse]:
        """
        Get the sections that you can edit in a template, including each section's default content.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDefaultContentTemplatesResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}/default-content",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDefaultContentTemplatesResponse,
                    parse_obj_as(
                        type_=ListDefaultContentTemplatesResponse,  # type: ignore
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


class AsyncRawTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_by: typing.Optional[str] = None,
        since_date_created: typing.Optional[str] = None,
        before_date_created: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        sort_field: typing.Optional[ListTemplatesRequestSortField] = None,
        content_type: typing.Optional[ListTemplatesRequestContentType] = None,
        sort_dir: typing.Optional[ListTemplatesRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[TemplateInstance, ListTemplatesResponse]:
        """
        Get a list of an account's available templates.

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

        created_by : typing.Optional[str]
            The Mailchimp account user who created the template.

        since_date_created : typing.Optional[str]
            Restrict the response to templates created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        before_date_created : typing.Optional[str]
            Restrict the response to templates created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        type : typing.Optional[str]
            Limit results based on template type.

        category : typing.Optional[str]
            Limit results based on category.

        folder_id : typing.Optional[str]
            The unique folder id.

        sort_field : typing.Optional[ListTemplatesRequestSortField]
            Returns user templates sorted by the specified field.

        content_type : typing.Optional[ListTemplatesRequestContentType]
            Limit results based on how the template's content is put together. Only templates of type `user` can be filtered by `content_type`. If you want to retrieve saved templates created with the legacy email editor, then filter `content_type` to `template`. If you'd rather pull your saved templates for the new editor, filter to `multichannel`. For code your own templates, filter to `html`.

        sort_dir : typing.Optional[ListTemplatesRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[TemplateInstance, ListTemplatesResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/templates",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "created_by": created_by,
                "since_date_created": since_date_created,
                "before_date_created": before_date_created,
                "type": type,
                "category": category,
                "folder_id": folder_id,
                "sort_field": sort_field,
                "content_type": content_type,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListTemplatesResponse,
                    parse_obj_as(
                        type_=ListTemplatesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.templates
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list(
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        created_by=created_by,
                        since_date_created=since_date_created,
                        before_date_created=before_date_created,
                        type=type,
                        category=category,
                        folder_id=folder_id,
                        sort_field=sort_field,
                        content_type=content_type,
                        sort_dir=sort_dir,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        html: str,
        name: str,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateInstance]:
        """
        Create a new template for the account. Only Classic templates are supported.

        Parameters
        ----------
        html : str
            The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.

        name : str
            The name of the template.

        folder_id : typing.Optional[str]
            The id of the folder the template is currently in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateInstance]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/templates",
            method="POST",
            json={
                "folder_id": folder_id,
                "html": html,
                "name": name,
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
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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
        self,
        template_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateInstance]:
        """
        Get information about a specific template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateInstance]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
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

    async def update(
        self,
        template_id: str,
        *,
        folder_id: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateInstance]:
        """
        Update the name, HTML, or `folder_id` of an existing template.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        folder_id : typing.Optional[str]
            The id of the folder the template is currently in.

        html : typing.Optional[str]
            The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.

        name : typing.Optional[str]
            The name of the template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateInstance]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}",
            method="PATCH",
            json={
                "folder_id": folder_id,
                "html": html,
                "name": name,
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
                    TemplateInstance,
                    parse_obj_as(
                        type_=TemplateInstance,  # type: ignore
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

    async def list_default_content(
        self,
        template_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDefaultContentTemplatesResponse]:
        """
        Get the sections that you can edit in a template, including each section's default content.

        Parameters
        ----------
        template_id : str
            The unique id for the template.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDefaultContentTemplatesResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/templates/{encode_path_param(template_id)}/default-content",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDefaultContentTemplatesResponse,
                    parse_obj_as(
                        type_=ListDefaultContentTemplatesResponse,  # type: ignore
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
