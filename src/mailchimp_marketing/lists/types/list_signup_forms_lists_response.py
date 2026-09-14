# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.signup_form import SignupForm
from .list_signup_forms_lists_response_links_item import ListSignupFormsListsResponseLinksItem


class ListSignupFormsListsResponse(UniversalBaseModel):
    """
    List Signup Forms.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSignupFormsListsResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id.
    """

    signup_forms: typing.Optional[typing.List[SignupForm]] = pydantic.Field(default=None)
    """
    List signup form.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
