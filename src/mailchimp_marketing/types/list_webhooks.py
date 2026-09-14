# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_webhooks_events import ListWebhooksEvents
from .list_webhooks_links_item import ListWebhooksLinksItem
from .list_webhooks_sources import ListWebhooksSources


class ListWebhooks(UniversalBaseModel):
    """
    Webhook configured for the given list.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListWebhooksLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    events: typing.Optional[ListWebhooksEvents] = pydantic.Field(default=None)
    """
    The events that can trigger the webhook and whether they are enabled.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An string that uniquely identifies this webhook.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for the list.
    """

    signing_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether outbound deliveries are HMAC-signed.
    """

    signing_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HMAC signing secret. Returned exactly once at creation. This should be stored securely; if lost, delete and recreate the webhook to obtain a new secret.
    """

    sources: typing.Optional[ListWebhooksSources] = pydantic.Field(default=None)
    """
    The possible sources of any events that can trigger the webhook and whether they are enabled.
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
