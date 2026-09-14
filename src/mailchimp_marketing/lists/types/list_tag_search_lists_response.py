# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_tag_search_lists_response_tags_item import ListTagSearchListsResponseTagsItem


class ListTagSearchListsResponse(UniversalBaseModel):
    """
    A list of tags matching the input query.
    """

    tags: typing.Optional[typing.List[ListTagSearchListsResponseTagsItem]] = pydantic.Field(default=None)
    """
    A list of matching tags.
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
