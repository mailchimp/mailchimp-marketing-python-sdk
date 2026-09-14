# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateListsRequestCampaignDefaults(UniversalBaseModel):
    """
    [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.
    """

    from_email: str = pydantic.Field()
    """
    The default from email for campaigns sent to this list.
    """

    from_name: str = pydantic.Field()
    """
    The default from name for campaigns sent to this list.
    """

    language: str = pydantic.Field()
    """
    The default language for this lists's forms.
    """

    subject: str = pydantic.Field()
    """
    The default subject line for campaigns sent to this list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
