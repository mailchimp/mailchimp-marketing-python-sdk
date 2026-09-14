# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateFeedbackCampaignsResponse(UniversalBaseModel):
    """
    A specific feedback message from a specific campaign.
    """

    block_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The block id for the editable block that the feedback addresses.
    """

    is_complete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of feedback.
    """

    message: str = pydantic.Field()
    """
    The content of the feedback.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
