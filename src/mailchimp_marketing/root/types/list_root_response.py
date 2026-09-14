# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_root_response_contact import ListRootResponseContact
from .list_root_response_first_payment import ListRootResponseFirstPayment
from .list_root_response_industry_stats import ListRootResponseIndustryStats
from .list_root_response_links_item import ListRootResponseLinksItem
from .list_root_response_pricing_plan_type import ListRootResponsePricingPlanType


class ListRootResponse(UniversalBaseModel):
    """
    The API root resource links to all other resources available in the API.
    """

    links: typing_extensions.Annotated[
        typing.Optional[typing.List[ListRootResponseLinksItem]],
        FieldMetadata(alias="_links"),
        pydantic.Field(
            alias="_links", description="A list of link types and descriptions for the API schema documents."
        ),
    ] = None
    """
    A list of link types and descriptions for the API schema documents.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Mailchimp account ID.
    """

    account_industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-specified industry associated with the account.
    """

    account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account.
    """

    account_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timezone currently set for the account.
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the avatar for the user.
    """

    contact: typing.Optional[ListRootResponseContact] = pydantic.Field(default=None)
    """
    Information about the account contact.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account email address.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first name tied to the account.
    """

    first_payment: typing.Optional[ListRootResponseFirstPayment] = pydantic.Field(default=None)
    """
    Date of first payment for monthly plans.
    """

    industry_stats: typing.Optional[ListRootResponseIndustryStats] = pydantic.Field(default=None)
    """
    The [average campaign statistics](https://mailchimp.com/resources/research/email-marketing-benchmarks/?utm_source=mc-api&utm_medium=docs&utm_campaign=apidocs) for all campaigns in the account's specified industry.
    """

    last_login: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time of the last login for this account in ISO 8601 format.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last name tied to the account.
    """

    login_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID associated with the user who owns this API key. If you can login to multiple accounts, this ID will be the same for each account.
    """

    member_since: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time that the account was created in ISO 8601 format.
    """

    pricing_plan_type: typing.Optional[ListRootResponsePricingPlanType] = pydantic.Field(default=None)
    """
    The type of pricing plan the account is on.
    """

    pro_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Legacy - whether the account includes [Mailchimp Pro](https://mailchimp.com/help/about-legacy-pricing-plan/).
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [user role](https://mailchimp.com/help/manage-user-levels-in-your-account/) for the account.
    """

    total_subscribers: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of subscribers across all lists in the account.
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username tied to the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
