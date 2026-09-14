# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signup_form_styles_item_options_item import SignupFormStylesItemOptionsItem
from .signup_form_styles_item_selector import SignupFormStylesItemSelector


class SignupFormStylesItem(UniversalBaseModel):
    """
    Collection of Element style for List Signup Forms.
    """

    options: typing.Optional[typing.List[SignupFormStylesItemOptionsItem]] = pydantic.Field(default=None)
    """
    A collection of options for a selector.
    """

    selector: typing.Optional[SignupFormStylesItemSelector] = pydantic.Field(default=None)
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
