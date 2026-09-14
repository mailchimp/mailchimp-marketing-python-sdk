# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sms_campaign_links_item import SmsCampaignLinksItem


class SmsCampaign(UniversalBaseModel):
    """
    A single SMS campaign.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this campaign.
    """

    web_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID used in the Mailchimp web application.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the campaign.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the campaign.
    """

    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel for this campaign (sms or whatsapp).
    """

    list_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The numeric ID of the list associated with this campaign.
    """

    recipient_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of recipients for this campaign.
    """

    create_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the campaign was created.
    """

    send_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the campaign is scheduled to send.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the campaign was last updated.
    """

    expire_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the campaign will stop sending in ISO 8601 format.
    """

    is_send_now: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the campaign is configured to send immediately.
    """

    folder_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the folder this campaign is in.
    """

    segments: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The segment IDs used to target recipients for this campaign.
    """

    excluded_segments: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The segment IDs excluded from receiving this campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[SmsCampaignLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
