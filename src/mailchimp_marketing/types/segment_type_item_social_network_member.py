# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_type_item_social_network_member_field import SegmentTypeItemSocialNetworkMemberField
from .segment_type_item_social_network_member_op import SegmentTypeItemSocialNetworkMemberOp
from .segment_type_item_social_network_member_value import SegmentTypeItemSocialNetworkMemberValue


class SegmentTypeItemSocialNetworkMember(UniversalBaseModel):
    """
    Segment by social network in Social Profiles data.
    """

    field: SegmentTypeItemSocialNetworkMemberField = pydantic.Field()
    """
    Segment by social network in Social Profiles data.
    """

    op: SegmentTypeItemSocialNetworkMemberOp = pydantic.Field()
    """
    Members who are/not on a given social network.
    """

    value: SegmentTypeItemSocialNetworkMemberValue = pydantic.Field()
    """
    The social network to segment against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
