# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.batch_webhook import BatchWebhook
from .list_batch_webhooks_response_links_item import ListBatchWebhooksResponseLinksItem


class ListBatchWebhooksResponse(UniversalBaseModel):
    """
    Manage webhooks for batch requests.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListBatchWebhooksResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    webhooks: typing.Optional[typing.List[BatchWebhook]] = pydantic.Field(default=None)
    """
    An array of objects, each representing a Batch Webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
