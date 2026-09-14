# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .automation_workflow_links_item import AutomationWorkflowLinksItem
from .automation_workflow_recipients import AutomationWorkflowRecipients
from .automation_workflow_report_summary import AutomationWorkflowReportSummary
from .automation_workflow_settings import AutomationWorkflowSettings
from .automation_workflow_status import AutomationWorkflowStatus
from .automation_workflow_tracking import AutomationWorkflowTracking
from .automation_workflow_trigger_settings import AutomationWorkflowTriggerSettings


class AutomationWorkflow(UniversalBaseModel):
    """
    A summary of an individual Automation workflow's settings and content.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[AutomationWorkflowLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    create_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the Automation was created in ISO 8601 format.
    """

    emails_sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of emails sent for the Automation.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that identifies the Automation.
    """

    recipients: typing.Optional[AutomationWorkflowRecipients] = pydantic.Field(default=None)
    """
    List settings for the Automation.
    """

    report_summary: typing.Optional[AutomationWorkflowReportSummary] = pydantic.Field(default=None)
    """
    A summary of opens and clicks for sent campaigns.
    """

    settings: typing.Optional[AutomationWorkflowSettings] = pydantic.Field(default=None)
    """
    The settings for the Automation workflow.
    """

    start_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the Automation was started in ISO 8601 format.
    """

    status: typing.Optional[AutomationWorkflowStatus] = pydantic.Field(default=None)
    """
    The current status of the Automation.
    """

    tracking: typing.Optional[AutomationWorkflowTracking] = pydantic.Field(default=None)
    """
    The tracking options for the Automation.
    """

    trigger_settings: typing.Optional[AutomationWorkflowTriggerSettings] = pydantic.Field(default=None)
    """
    Available triggers for Automation workflows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
