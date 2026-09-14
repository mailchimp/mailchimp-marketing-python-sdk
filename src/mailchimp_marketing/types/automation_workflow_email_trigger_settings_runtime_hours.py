# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automation_workflow_email_trigger_settings_runtime_hours_type import (
    AutomationWorkflowEmailTriggerSettingsRuntimeHoursType,
)


class AutomationWorkflowEmailTriggerSettingsRuntimeHours(UniversalBaseModel):
    """
    The hours an Automation workflow can send.
    """

    type: AutomationWorkflowEmailTriggerSettingsRuntimeHoursType = pydantic.Field()
    """
    When to send the Automation email.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
