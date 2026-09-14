# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_default_content_templates_response_links_item import ListDefaultContentTemplatesResponseLinksItem


class ListDefaultContentTemplatesResponse(UniversalBaseModel):
    """
    Default content for a template.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListDefaultContentTemplatesResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    sections: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The sections that you can edit in the template, including each section's default content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
