# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_template_folders_response_folders_item import ListTemplateFoldersResponseFoldersItem
from .list_template_folders_response_links_item import ListTemplateFoldersResponseLinksItem


class ListTemplateFoldersResponse(UniversalBaseModel):
    """
    A list of template folders
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListTemplateFoldersResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    folders: typing.Optional[typing.List[ListTemplateFoldersResponseFoldersItem]] = pydantic.Field(default=None)
    """
    An array of objects representing template folders.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
