# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.automation_workflow_email import AutomationWorkflowEmail
from .list_emails_automations_response_links_item_item import ListEmailsAutomationsResponseLinksItemItem


class ListEmailsAutomationsResponse(UniversalBaseModel):
    """
    A summary of the emails in an Automation workflow.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[ListEmailsAutomationsResponseLinksItemItem]]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    emails: typing.Optional[typing.List[AutomationWorkflowEmail]] = pydantic.Field(default=None)
    """
    An array of objects, each representing an email in an Automation workflow.
    """

    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items matching the query regardless of pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
