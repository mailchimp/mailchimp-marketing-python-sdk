# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_content_links_item import CampaignContentLinksItem
from .campaign_content_variate_contents_item import CampaignContentVariateContentsItem


class CampaignContent(UniversalBaseModel):
    """
    The HTML and plain-text content for a campaign.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[CampaignContentLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    archive_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Archive HTML for the campaign.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw HTML for the campaign.
    """

    plain_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.
    """

    variate_contents: typing.Optional[typing.List[CampaignContentVariateContentsItem]] = pydantic.Field(default=None)
    """
    Content options for multivariate campaigns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
