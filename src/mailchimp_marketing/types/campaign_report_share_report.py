# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignReportShareReport(UniversalBaseModel):
    """
    The url and password for the [VIP report](https://mailchimp.com/help/share-a-campaign-report/).
    """

    share_password: typing.Optional[str] = pydantic.Field(default=None)
    """
    If password protected, the password for the VIP report.
    """

    share_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the VIP report.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
