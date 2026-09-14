# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_member_tag_lists_request_tags_item_status import CreateMemberTagListsRequestTagsItemStatus


class CreateMemberTagListsRequestTagsItem(UniversalBaseModel):
    """
    Add or remove tags on a member by declaring a tag either active or inactive on a member.
    """

    name: str = pydantic.Field()
    """
    The name of the tag.
    """

    status: CreateMemberTagListsRequestTagsItemStatus = pydantic.Field()
    """
    The status for the tag on the member, pass in active to add a tag or inactive to remove it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
