# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automation_workflow_trigger_settings_runtime_days_item import AutomationWorkflowTriggerSettingsRuntimeDaysItem
from .automation_workflow_trigger_settings_runtime_hours import AutomationWorkflowTriggerSettingsRuntimeHours


class AutomationWorkflowTriggerSettingsRuntime(UniversalBaseModel):
    """
    A workflow's runtime settings for an Automation.
    """

    days: typing.Optional[typing.List[AutomationWorkflowTriggerSettingsRuntimeDaysItem]] = pydantic.Field(default=None)
    """
    The days an Automation workflow can send.
    """

    hours: typing.Optional[AutomationWorkflowTriggerSettingsRuntimeHours] = pydantic.Field(default=None)
    """
    The hours an Automation workflow can send.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
