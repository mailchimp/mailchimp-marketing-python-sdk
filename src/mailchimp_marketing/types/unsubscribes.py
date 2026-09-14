# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .unsubscribes_links_item import UnsubscribesLinksItem
from .unsubscribes_merge_fields_value import UnsubscribesMergeFieldsValue


class Unsubscribes(UniversalBaseModel):
    """
    A member who unsubscribed from a specific campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[UnsubscribesLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The campaign id.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for a subscriber.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id.
    """

    list_is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the list used, namely if it's deleted or disabled.
    """

    merge_fields: typing.Optional[typing.Dict[str, UnsubscribesMergeFieldsValue]] = pydantic.Field(default=None)
    """
    A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    If available, the reason listed by the member for unsubscribing.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the member opted-out in ISO 8601 format.
    """

    vip: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
