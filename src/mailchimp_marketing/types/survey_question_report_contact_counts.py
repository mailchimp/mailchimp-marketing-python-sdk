# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SurveyQuestionReportContactCounts(UniversalBaseModel):
    """
    For email question types, how many are new, known, or unknown contacts.
    """

    known: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of known contacts that responded to this survey.
    """

    new: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of new contacts that responded to this survey.
    """

    unknown: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unknown contacts that responded to this survey.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
