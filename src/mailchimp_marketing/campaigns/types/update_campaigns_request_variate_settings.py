# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_campaigns_request_variate_settings_send_times_item import (
    UpdateCampaignsRequestVariateSettingsSendTimesItem,
)
from .update_campaigns_request_variate_settings_winner_criteria import (
    UpdateCampaignsRequestVariateSettingsWinnerCriteria,
)


class UpdateCampaignsRequestVariateSettings(UniversalBaseModel):
    """
    The settings specific to A/B test campaigns.
    """

    from_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The possible from names. The number of from_names provided must match the number of reply_to_addresses. If no from_names are provided, settings.from_name will be used.
    """

    reply_to_addresses: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The possible reply-to addresses. The number of reply_to_addresses provided must match the number of from_names. If no reply_to_addresses are provided, settings.reply_to will be used.
    """

    send_times: typing.Optional[typing.List[UpdateCampaignsRequestVariateSettingsSendTimesItem]] = pydantic.Field(
        default=None
    )
    """
    The possible send times to test. The times provided should be in the format YYYY-MM-DD HH:MM:SS or ISO 8601 date-time format. If send_times are provided to test, the test_size will be set to 100% and winner_criteria will be ignored.
    """

    subject_lines: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The possible subject lines to test. If no subject lines are provided, settings.subject_line will be used.
    """

    test_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The percentage of recipients to send the test combinations to, must be a value between 10 and 100.
    """

    wait_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of minutes to wait before choosing the winning campaign. The value of wait_time must be greater than 0 and in whole hours, specified in minutes.
    """

    winner_criteria: typing.Optional[UpdateCampaignsRequestVariateSettingsWinnerCriteria] = pydantic.Field(default=None)
    """
    The combination that performs the best. This may be determined automatically by click rate, open rate, or total revenue -- or you may choose manually based on the reporting data you find the most valuable. For Multivariate Campaigns testing send_time, winner_criteria is ignored. For Multivariate Campaigns with 'manual' as the winner_criteria, the winner must be chosen in the Mailchimp web application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
