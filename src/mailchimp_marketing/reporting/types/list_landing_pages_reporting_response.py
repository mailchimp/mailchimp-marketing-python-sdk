# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.landing_page_report import LandingPageReport
from .list_landing_pages_reporting_response_links_item import ListLandingPagesReportingResponseLinksItem


class ListLandingPagesReportingResponse(UniversalBaseModel):
    """
    A collection of landing pages.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListLandingPagesReportingResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    landing_pages: typing.Optional[typing.List[LandingPageReport]] = None
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
