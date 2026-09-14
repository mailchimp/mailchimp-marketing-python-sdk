# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_content_landing_pages_response_links_item import ListContentLandingPagesResponseLinksItem


class ListContentLandingPagesResponse(UniversalBaseModel):
    """
    The HTML content for a landing page.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListContentLandingPagesResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw HTML for the landing page.
    """

    json_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="json"),
        pydantic.Field(alias="json", description="The JSON Structure for the landing page"),
    ] = None
    """
    The JSON Structure for the landing page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
