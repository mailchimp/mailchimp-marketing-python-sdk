# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_audience_contact_request_tags_item_name_status import PatchAudienceContactRequestTagsItemNameStatus


class PatchAudienceContactRequestTagsItemName(UniversalBaseModel):
    name: str
    status: PatchAudienceContactRequestTagsItemNameStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
