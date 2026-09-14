# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateAutomationsRequestSettings(UniversalBaseModel):
    """
    The settings for the Automation workflow.
    """

    from_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'from' name for the Automation (not an email address).
    """

    reply_to: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reply-to email address for the Automation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
