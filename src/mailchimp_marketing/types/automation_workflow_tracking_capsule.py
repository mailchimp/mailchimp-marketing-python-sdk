# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AutomationWorkflowTrackingCapsule(UniversalBaseModel):
    """
    Deprecated
    """

    notes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Update contact notes for a campaign based on a subscriber's email addresses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
