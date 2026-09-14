# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacebookAdsFeedback(UniversalBaseModel):
    """
    Check if this ad is connected to a facebook page
    """

    audience: typing.Optional[str] = pydantic.Field(default=None)
    """
    Feedback regarding the audience of this Ad.
    """

    budget: typing.Optional[str] = pydantic.Field(default=None)
    """
    Feedback regarding the budget of this Ad.
    """

    compliance: typing.Optional[str] = pydantic.Field(default=None)
    """
    Feedback regarding the compliance of this Ad.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Feedback regarding the content of this Ad.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
