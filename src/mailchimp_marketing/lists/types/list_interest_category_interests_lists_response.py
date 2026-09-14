# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.interest import Interest
from .list_interest_category_interests_lists_response_links_item import (
    ListInterestCategoryInterestsListsResponseLinksItem,
)


class ListInterestCategoryInterestsListsResponse(UniversalBaseModel):
    """
    A list of this category's interests
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListInterestCategoryInterestsListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    category_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id for the interest category.
    """

    interests: typing.Optional[typing.List[Interest]] = pydantic.Field(default=None)
    """
    An array of this category's interests
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique list id that the interests belong to.
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
