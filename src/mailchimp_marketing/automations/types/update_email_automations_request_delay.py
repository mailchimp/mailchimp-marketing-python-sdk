# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_email_automations_request_delay_action import UpdateEmailAutomationsRequestDelayAction
from .update_email_automations_request_delay_direction import UpdateEmailAutomationsRequestDelayDirection
from .update_email_automations_request_delay_type import UpdateEmailAutomationsRequestDelayType


class UpdateEmailAutomationsRequestDelay(UniversalBaseModel):
    """
    The delay settings for an automation email.
    """

    action: UpdateEmailAutomationsRequestDelayAction = pydantic.Field()
    """
    The action that triggers the delay of an automation emails.
    """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The delay amount for an automation email.
    """

    direction: typing.Optional[UpdateEmailAutomationsRequestDelayDirection] = pydantic.Field(default=None)
    """
    Whether the delay settings describe before or after the delay action of an automation email.
    """

    type: typing.Optional[UpdateEmailAutomationsRequestDelayType] = pydantic.Field(default=None)
    """
    The type of delay for an automation email.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
