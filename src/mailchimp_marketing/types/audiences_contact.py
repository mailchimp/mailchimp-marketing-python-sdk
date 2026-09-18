# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audiences_contact_email_channel import AudiencesContactEmailChannel
from .audiences_contact_language import AudiencesContactLanguage
from .audiences_contact_merge_fields_value import AudiencesContactMergeFieldsValue
from .audiences_contact_sms_channel import AudiencesContactSmsChannel
from .audiences_contact_source import AudiencesContactSource
from .audiences_contact_status import AudiencesContactStatus


class AudiencesContact(UniversalBaseModel):
    """
    An instance of a contact.
    """

    audience_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for the audience.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date that the contact was created.
    """

    email_channel: typing.Optional[AudiencesContactEmailChannel] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for the contact.
    """

    language: typing.Optional[AudiencesContactLanguage] = pydantic.Field(default=None)
    """
    The contact's detected language. Empty string when no language has been detected or set.
    """

    last_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date that the contact was last updated.
    """

    merge_fields: typing.Optional[typing.Dict[str, AudiencesContactMergeFieldsValue]] = pydantic.Field(default=None)
    """
    A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    """

    sms_channel: typing.Optional[AudiencesContactSmsChannel] = None
    source: typing.Optional[AudiencesContactSource] = pydantic.Field(default=None)
    """
    The source from which the parent's entity was created.
    """

    status: typing.Optional[AudiencesContactStatus] = pydantic.Field(default=None)
    """
    The status of a contact.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags assigned to this contact.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
