# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_campaigns_request_recipients_segment_opts import UpdateCampaignsRequestRecipientsSegmentOpts


class UpdateCampaignsRequestRecipients(UniversalBaseModel):
    """
    List settings for the campaign.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique list id.
    """

    segment_opts: typing.Optional[UpdateCampaignsRequestRecipientsSegmentOpts] = pydantic.Field(default=None)
    """
    An object representing all segmentation options. This object should contain a `saved_segment_id` to use an existing segment, or you can create a new segment by including both `match` and `conditions` options.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
