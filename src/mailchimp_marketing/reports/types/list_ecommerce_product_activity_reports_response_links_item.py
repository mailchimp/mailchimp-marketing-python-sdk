# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_ecommerce_product_activity_reports_response_links_item_method import (
    ListEcommerceProductActivityReportsResponseLinksItemMethod,
)


class ListEcommerceProductActivityReportsResponseLinksItem(UniversalBaseModel):
    """
    This object represents a link from the resource where it is found to another resource or action that may be performed.
    """

    href: typing.Optional[str] = pydantic.Field(default=None)
    """
    This property contains a fully-qualified URL that can be called to retrieve the linked resource or perform the linked action.
    """

    method: typing.Optional[ListEcommerceProductActivityReportsResponseLinksItemMethod] = pydantic.Field(default=None)
    """
    The HTTP method that should be used when accessing the URL defined in 'href'.
    """

    rel: typing.Optional[str] = pydantic.Field(default=None)
    """
    As with an HTML 'rel' attribute, this describes the type of link.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(
            alias="schema",
            description="For HTTP methods that can receive bodies (POST and PUT), this is a URL representing the schema that the body should conform to.",
        ),
    ] = None
    """
    For HTTP methods that can receive bodies (POST and PUT), this is a URL representing the schema that the body should conform to.
    """

    target_schema: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetSchema"),
        pydantic.Field(
            alias="targetSchema",
            description="For GETs, this is a URL representing the schema that the response should conform to.",
        ),
    ] = None
    """
    For GETs, this is a URL representing the schema that the response should conform to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
