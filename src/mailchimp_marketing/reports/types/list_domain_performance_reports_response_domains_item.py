# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListDomainPerformanceReportsResponseDomainsItem(UniversalBaseModel):
    """
    A single email domain's performance
    """

    bounces: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of bounces at a domain.
    """

    bounces_pct: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total bounces from this domain.
    """

    clicks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of clicks for a domain.
    """

    clicks_pct: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total clicks from this domain.
    """

    delivered: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of successful deliveries for a domain.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the domain (gmail.com, hotmail.com, yahoo.com).
    """

    emails_pct: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total emails that went to this domain.
    """

    emails_sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of emails sent to that specific domain.
    """

    opens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of opens for a domain.
    """

    opens_pct: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total opens from this domain.
    """

    unsubs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of unsubscribes for a domain.
    """

    unsubs_pct: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of total unsubscribes from this domain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
