# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_member_lists_request_location_latitude import UpdateMemberListsRequestLocationLatitude
from .update_member_lists_request_location_longitude import UpdateMemberListsRequestLocationLongitude


class UpdateMemberListsRequestLocation(UniversalBaseModel):
    """
    Subscriber location information.
    """

    latitude: typing.Optional[UpdateMemberListsRequestLocationLatitude] = None
    longitude: typing.Optional[UpdateMemberListsRequestLocationLongitude] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
