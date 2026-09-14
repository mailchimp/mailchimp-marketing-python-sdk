# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lists_abuse_reports_links_item import ListsAbuseReportsLinksItem
from .lists_abuse_reports_merge_fields_value import ListsAbuseReportsMergeFieldsValue


class ListsAbuseReports(UniversalBaseModel):
    """
    Details of abuse complaints for a specific list. An abuse complaint occurs when your recipient clicks to 'report spam' in their email program.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListsAbuseReportsLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The campaign id for the abuse report
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date for the abuse report
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for a subscriber.
    """

    email_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the lowercase version of the list member's email address.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id for the abuse report
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list id for the abuse report.
    """

    merge_fields: typing.Optional[typing.Dict[str, ListsAbuseReportsMergeFieldsValue]] = pydantic.Field(default=None)
    """
    A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    """

    vip: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
