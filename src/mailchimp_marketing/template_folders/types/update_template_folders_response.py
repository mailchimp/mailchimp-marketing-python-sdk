# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_template_folders_response_links_item import UpdateTemplateFoldersResponseLinksItem


class UpdateTemplateFoldersResponse(UniversalBaseModel):
    """
    A folder used to organize templates.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateTemplateFoldersResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of templates in the folder.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that uniquely identifies this template folder.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the folder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
