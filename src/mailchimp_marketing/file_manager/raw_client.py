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
from ..types.gallery_file import GalleryFile
from .types.create_folder_file_manager_response import CreateFolderFileManagerResponse
from .types.get_folder_file_manager_response import GetFolderFileManagerResponse
from .types.list_file_manager_response_item import ListFileManagerResponseItem
from .types.list_files_file_manager_request_sort_dir import ListFilesFileManagerRequestSortDir
from .types.list_files_file_manager_request_sort_field import ListFilesFileManagerRequestSortField
from .types.list_files_file_manager_response import ListFilesFileManagerResponse
from .types.list_folder_files_file_manager_request_sort_dir import ListFolderFilesFileManagerRequestSortDir
from .types.list_folder_files_file_manager_request_sort_field import ListFolderFilesFileManagerRequestSortField
from .types.list_folder_files_file_manager_response import ListFolderFilesFileManagerResponse
from .types.list_folders_file_manager_response import ListFoldersFileManagerResponse
from .types.list_folders_file_manager_response_folders_item import ListFoldersFileManagerResponseFoldersItem
from .types.update_folder_file_manager_response import UpdateFolderFileManagerResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawFileManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListFileManagerResponseItem]]:
        """
        Get information about the file-manager endpoint's resources

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListFileManagerResponseItem]]
            A file manager.
        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/file-manager",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListFileManagerResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListFileManagerResponseItem],  # type: ignore
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

    def list_files(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        sort_field: typing.Optional[ListFilesFileManagerRequestSortField] = None,
        sort_dir: typing.Optional[ListFilesFileManagerRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[GalleryFile, ListFilesFileManagerResponse]:
        """
        Get a list of available images and files stored in the File Manager for the account.

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

        type : typing.Optional[str]
            The file type for the File Manager file.

        created_by : typing.Optional[str]
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        sort_field : typing.Optional[ListFilesFileManagerRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFilesFileManagerRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[GalleryFile, ListFilesFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/file-manager/files",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFilesFileManagerResponse,
                    parse_obj_as(
                        type_=ListFilesFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.files
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_files(
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    type=type,
                    created_by=created_by,
                    before_created_at=before_created_at,
                    since_created_at=since_created_at,
                    sort_field=sort_field,
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

    def create_file(
        self,
        *,
        file_data: str,
        name: str,
        folder_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GalleryFile]:
        """
        Upload a new image or file to the File Manager.

        Parameters
        ----------
        file_data : str
            The base64-encoded contents of the file.

        name : str
            The name of the file.

        folder_id : typing.Optional[int]
            The id of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GalleryFile]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/file-manager/files",
            method="POST",
            json={
                "file_data": file_data,
                "folder_id": folder_id,
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    def get_file(
        self,
        file_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GalleryFile]:
        """
        Get information about a specific file in the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GalleryFile]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Remove a specific file from the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
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

    def update_file(
        self,
        file_id: str,
        *,
        folder_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GalleryFile]:
        """
        Update a file in the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        folder_id : typing.Optional[int]
            The id of the folder. Setting `folder_id` to `0` will remove a file from its current folder.

        name : typing.Optional[str]
            The name of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GalleryFile]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
            method="PATCH",
            json={
                "folder_id": folder_id,
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    def list_folders(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListFoldersFileManagerResponseFoldersItem, ListFoldersFileManagerResponse]:
        """
        Get a list of all folders in the File Manager.

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
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListFoldersFileManagerResponseFoldersItem, ListFoldersFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "3.0/file-manager/folders",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFoldersFileManagerResponse,
                    parse_obj_as(
                        type_=ListFoldersFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.folders
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_folders(
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    created_by=created_by,
                    before_created_at=before_created_at,
                    since_created_at=since_created_at,
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

    def create_folder(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateFolderFileManagerResponse]:
        """
        Create a new folder in the File Manager.

        Parameters
        ----------
        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateFolderFileManagerResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "3.0/file-manager/folders",
            method="POST",
            json={
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
                    CreateFolderFileManagerResponse,
                    parse_obj_as(
                        type_=CreateFolderFileManagerResponse,  # type: ignore
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

    def get_folder(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetFolderFileManagerResponse]:
        """
        Get information about a specific folder in the File Manager.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFolderFileManagerResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
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
                    GetFolderFileManagerResponse,
                    parse_obj_as(
                        type_=GetFolderFileManagerResponse,  # type: ignore
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

    def delete_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific folder in the File Manager.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
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

    def update_folder(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateFolderFileManagerResponse]:
        """
        Update a specific File Manager folder.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateFolderFileManagerResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
            method="PATCH",
            json={
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
                    UpdateFolderFileManagerResponse,
                    parse_obj_as(
                        type_=UpdateFolderFileManagerResponse,  # type: ignore
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

    def list_folder_files(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        sort_field: typing.Optional[ListFolderFilesFileManagerRequestSortField] = None,
        sort_dir: typing.Optional[ListFolderFilesFileManagerRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[GalleryFile, ListFolderFilesFileManagerResponse]:
        """
        Get a list of available images and files stored in this folder.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            The file type for the File Manager file.

        created_by : typing.Optional[str]
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        sort_field : typing.Optional[ListFolderFilesFileManagerRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFolderFilesFileManagerRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[GalleryFile, ListFolderFilesFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}/files",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFolderFilesFileManagerResponse,
                    parse_obj_as(
                        type_=ListFolderFilesFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.files
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_folder_files(
                    folder_id,
                    fields=fields,
                    exclude_fields=exclude_fields,
                    count=count,
                    offset=offset + 1,
                    type=type,
                    created_by=created_by,
                    before_created_at=before_created_at,
                    since_created_at=since_created_at,
                    sort_field=sort_field,
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


class AsyncRawFileManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListFileManagerResponseItem]]:
        """
        Get information about the file-manager endpoint's resources

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListFileManagerResponseItem]]
            A file manager.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/file-manager",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListFileManagerResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListFileManagerResponseItem],  # type: ignore
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

    async def list_files(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        sort_field: typing.Optional[ListFilesFileManagerRequestSortField] = None,
        sort_dir: typing.Optional[ListFilesFileManagerRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[GalleryFile, ListFilesFileManagerResponse]:
        """
        Get a list of available images and files stored in the File Manager for the account.

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

        type : typing.Optional[str]
            The file type for the File Manager file.

        created_by : typing.Optional[str]
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        sort_field : typing.Optional[ListFilesFileManagerRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFilesFileManagerRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[GalleryFile, ListFilesFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/file-manager/files",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFilesFileManagerResponse,
                    parse_obj_as(
                        type_=ListFilesFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.files
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_files(
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        type=type,
                        created_by=created_by,
                        before_created_at=before_created_at,
                        since_created_at=since_created_at,
                        sort_field=sort_field,
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

    async def create_file(
        self,
        *,
        file_data: str,
        name: str,
        folder_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GalleryFile]:
        """
        Upload a new image or file to the File Manager.

        Parameters
        ----------
        file_data : str
            The base64-encoded contents of the file.

        name : str
            The name of the file.

        folder_id : typing.Optional[int]
            The id of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GalleryFile]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/file-manager/files",
            method="POST",
            json={
                "file_data": file_data,
                "folder_id": folder_id,
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    async def get_file(
        self,
        file_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GalleryFile]:
        """
        Get information about a specific file in the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GalleryFile]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    async def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Remove a specific file from the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
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

    async def update_file(
        self,
        file_id: str,
        *,
        folder_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GalleryFile]:
        """
        Update a file in the File Manager.

        Parameters
        ----------
        file_id : str
            The unique id for the File Manager file.

        folder_id : typing.Optional[int]
            The id of the folder. Setting `folder_id` to `0` will remove a file from its current folder.

        name : typing.Optional[str]
            The name of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GalleryFile]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/files/{encode_path_param(file_id)}",
            method="PATCH",
            json={
                "folder_id": folder_id,
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
                    GalleryFile,
                    parse_obj_as(
                        type_=GalleryFile,  # type: ignore
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

    async def list_folders(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListFoldersFileManagerResponseFoldersItem, ListFoldersFileManagerResponse]:
        """
        Get a list of all folders in the File Manager.

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
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListFoldersFileManagerResponseFoldersItem, ListFoldersFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "3.0/file-manager/folders",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFoldersFileManagerResponse,
                    parse_obj_as(
                        type_=ListFoldersFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.folders
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_folders(
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        created_by=created_by,
                        before_created_at=before_created_at,
                        since_created_at=since_created_at,
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

    async def create_folder(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateFolderFileManagerResponse]:
        """
        Create a new folder in the File Manager.

        Parameters
        ----------
        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateFolderFileManagerResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "3.0/file-manager/folders",
            method="POST",
            json={
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
                    CreateFolderFileManagerResponse,
                    parse_obj_as(
                        type_=CreateFolderFileManagerResponse,  # type: ignore
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

    async def get_folder(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetFolderFileManagerResponse]:
        """
        Get information about a specific folder in the File Manager.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFolderFileManagerResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
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
                    GetFolderFileManagerResponse,
                    parse_obj_as(
                        type_=GetFolderFileManagerResponse,  # type: ignore
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

    async def delete_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific folder in the File Manager.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
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

    async def update_folder(
        self, folder_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateFolderFileManagerResponse]:
        """
        Update a specific File Manager folder.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        name : str
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateFolderFileManagerResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}",
            method="PATCH",
            json={
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
                    UpdateFolderFileManagerResponse,
                    parse_obj_as(
                        type_=UpdateFolderFileManagerResponse,  # type: ignore
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

    async def list_folder_files(
        self,
        folder_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        before_created_at: typing.Optional[str] = None,
        since_created_at: typing.Optional[str] = None,
        sort_field: typing.Optional[ListFolderFilesFileManagerRequestSortField] = None,
        sort_dir: typing.Optional[ListFolderFilesFileManagerRequestSortDir] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[GalleryFile, ListFolderFilesFileManagerResponse]:
        """
        Get a list of available images and files stored in this folder.

        Parameters
        ----------
        folder_id : str
            The unique id for the File Manager folder.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        type : typing.Optional[str]
            The file type for the File Manager file.

        created_by : typing.Optional[str]
            The Mailchimp account user who created the File Manager file.

        before_created_at : typing.Optional[str]
            Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        since_created_at : typing.Optional[str]
            Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.

        sort_field : typing.Optional[ListFolderFilesFileManagerRequestSortField]
            Returns files sorted by the specified field.

        sort_dir : typing.Optional[ListFolderFilesFileManagerRequestSortDir]
            Determines the order direction for sorted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[GalleryFile, ListFolderFilesFileManagerResponse]

        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"3.0/file-manager/folders/{encode_path_param(folder_id)}/files",
            method="GET",
            params={
                "fields": ",".join(map(str, fields)) if isinstance(fields, (list, tuple, set)) else fields,
                "exclude_fields": ",".join(map(str, exclude_fields))
                if isinstance(exclude_fields, (list, tuple, set))
                else exclude_fields,
                "count": count,
                "offset": offset,
                "type": type,
                "created_by": created_by,
                "before_created_at": before_created_at,
                "since_created_at": since_created_at,
                "sort_field": sort_field,
                "sort_dir": sort_dir,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFolderFilesFileManagerResponse,
                    parse_obj_as(
                        type_=ListFolderFilesFileManagerResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.files
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_folder_files(
                        folder_id,
                        fields=fields,
                        exclude_fields=exclude_fields,
                        count=count,
                        offset=offset + 1,
                        type=type,
                        created_by=created_by,
                        before_created_at=before_created_at,
                        since_created_at=since_created_at,
                        sort_field=sort_field,
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
