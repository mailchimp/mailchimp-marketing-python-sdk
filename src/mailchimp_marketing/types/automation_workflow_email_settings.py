# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AutomationWorkflowEmailSettings(UniversalBaseModel):
    """
    Settings for the campaign including the email subject, from name, and from email address.
    """

    authenticate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Mailchimp [authenticated](https://mailchimp.com/help/about-email-authentication/) the campaign. Defaults to `true`.
    """

    auto_fb_post: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of [Facebook](https://mailchimp.com/help/connect-or-disconnect-the-facebook-integration/) page ids to auto-post to.
    """

    auto_footer: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Automatically append Mailchimp's [default footer](https://mailchimp.com/help/about-campaign-footers/) to the campaign.
    """

    auto_tweet: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Automatically tweet a link to the [campaign archive](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) page when the campaign is sent.
    """

    drag_and_drop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the campaign uses the drag-and-drop editor.
    """

    fb_comments: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allows Facebook comments on the campaign (also force-enables the Campaign Archive toolbar). Defaults to `true`.
    """

    from_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'from' name on the campaign (not an email address).
    """

    inline_css: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Automatically inline the CSS included with the campaign content.
    """

    preview_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preview text for the campaign.
    """

    reply_to: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reply-to email address for the campaign.
    """

    subject_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subject line for the campaign.
    """

    template_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id for the template used in this campaign.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the campaign.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
