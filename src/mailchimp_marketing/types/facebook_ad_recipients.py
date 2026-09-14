# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facebook_ad_recipients_segment_opts import FacebookAdRecipientsSegmentOpts


class FacebookAdRecipients(UniversalBaseModel):
    """
    High level audience information for who the outreach targets.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique list id.
    """

    list_is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the list used, namely if it's deleted or disabled.
    """

    list_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the list.
    """

    recipient_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of the recipients on the associated list. Formatted as an integer.
    """

    segment_opts: typing.Optional[FacebookAdRecipientsSegmentOpts] = pydantic.Field(default=None)
    """
    An object representing all segmentation options. This object should contain a `saved_segment_id` to use an existing segment, or you can create a new segment by including both `match` and `conditions` options.
    """

    segment_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the [segment](https://mailchimp.com/help/save-and-manage-segments/) used for the campaign. Formatted as a string marked up with HTML.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
