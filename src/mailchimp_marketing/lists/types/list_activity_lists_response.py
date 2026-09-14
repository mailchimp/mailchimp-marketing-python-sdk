# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_activity_lists_response_activity_item import ListActivityListsResponseActivityItem
from .list_activity_lists_response_links_item import ListActivityListsResponseLinksItem


class ListActivityListsResponse(UniversalBaseModel):
    """
    Up to the previous 180 days of daily detailed aggregated activity stats for a specific list. Does not include AutoResponder or Automation activity.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListActivityListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    activity: typing.Optional[typing.List[ListActivityListsResponseActivityItem]] = pydantic.Field(default=None)
    """
    Recent list activity.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the list.
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
