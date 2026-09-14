# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upsert_member_lists_request_location_latitude import UpsertMemberListsRequestLocationLatitude
from .upsert_member_lists_request_location_longitude import UpsertMemberListsRequestLocationLongitude


class UpsertMemberListsRequestLocation(UniversalBaseModel):
    """
    Subscriber location information.
    """

    latitude: typing.Optional[UpsertMemberListsRequestLocationLatitude] = None
    longitude: typing.Optional[UpsertMemberListsRequestLocationLongitude] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
