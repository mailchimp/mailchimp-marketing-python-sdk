# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignReportFacebookLikes(UniversalBaseModel):
    """
    An object describing campaign engagement on Facebook.
    """

    facebook_likes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of Facebook likes for the campaign.
    """

    recipient_likes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of recipients who liked the campaign on Facebook.
    """

    unique_likes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique likes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
