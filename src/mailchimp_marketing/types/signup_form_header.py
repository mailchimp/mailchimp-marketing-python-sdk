# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signup_form_header_image_align import SignupFormHeaderImageAlign
from .signup_form_header_image_border_style import SignupFormHeaderImageBorderStyle
from .signup_form_header_image_target import SignupFormHeaderImageTarget


class SignupFormHeader(UniversalBaseModel):
    """
    Options for customizing your signup form header.
    """

    image_align: typing.Optional[SignupFormHeaderImageAlign] = pydantic.Field(default=None)
    """
    Image alignment.
    """

    image_alt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Alt text for the image.
    """

    image_border_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Image border color.
    """

    image_border_style: typing.Optional[SignupFormHeaderImageBorderStyle] = pydantic.Field(default=None)
    """
    Image border style.
    """

    image_border_width: typing.Optional[str] = pydantic.Field(default=None)
    """
    Image border width.
    """

    image_height: typing.Optional[str] = pydantic.Field(default=None)
    """
    Image height, in pixels.
    """

    image_link: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that the header image will link to.
    """

    image_target: typing.Optional[SignupFormHeaderImageTarget] = pydantic.Field(default=None)
    """
    Image link target.
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Header image URL.
    """

    image_width: typing.Optional[str] = pydantic.Field(default=None)
    """
    Image width, in pixels.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Header text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
