# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignContentVariateContentsItem(UniversalBaseModel):
    content_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label used to identify the content option.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw HTML for the campaign.
    """

    plain_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
