# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_folders_folders_item import CampaignFoldersFoldersItem
from .campaign_folders_links_item import CampaignFoldersLinksItem


class CampaignFolders(UniversalBaseModel):
    """
    A list of campaign folders
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[CampaignFoldersLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    folders: typing.Optional[typing.List[CampaignFoldersFoldersItem]] = pydantic.Field(default=None)
    """
    An array of objects representing campaign folders.
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
