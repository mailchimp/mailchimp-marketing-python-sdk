# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signup_form_lists_request_styles_item_options_item import CreateSignupFormListsRequestStylesItemOptionsItem
from .create_signup_form_lists_request_styles_item_selector import CreateSignupFormListsRequestStylesItemSelector


class CreateSignupFormListsRequestStylesItem(UniversalBaseModel):
    """
    Collection of Element style for List Signup Forms.
    """

    options: typing.Optional[typing.List[CreateSignupFormListsRequestStylesItemOptionsItem]] = pydantic.Field(
        default=None
    )
    """
    A collection of options for a selector.
    """

    selector: typing.Optional[CreateSignupFormListsRequestStylesItemSelector] = pydantic.Field(default=None)
    """
    A string that identifies the element selector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
