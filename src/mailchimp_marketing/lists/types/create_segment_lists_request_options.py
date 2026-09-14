# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.segment_type import SegmentType
from .create_segment_lists_request_options_match import CreateSegmentListsRequestOptionsMatch


class CreateSegmentListsRequestOptions(UniversalBaseModel):
    """
    The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.
    """

    conditions: typing.Optional[SegmentType] = None
    match: typing.Optional[CreateSegmentListsRequestOptionsMatch] = pydantic.Field(default=None)
    """
    Match type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
