# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .batch_webhook_links_item_item import BatchWebhookLinksItemItem


class BatchWebhook(UniversalBaseModel):
    """
    A webhook configured for batch status updates.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[BatchWebhookLinksItemItem]]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook receives requests or not.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this Batch Webhook.
    """

    signing_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether outbound deliveries are HMAC-signed.
    """

    signing_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HMAC signing secret. Returned exactly once at creation. This should be stored securely; if lost, delete and recreate the webhook to obtain a new secret.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A valid URL for the Webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
