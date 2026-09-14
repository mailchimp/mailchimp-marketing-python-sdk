# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListListsResponseConstraints(UniversalBaseModel):
    """
    Do particular authorization constraints around this collection limit creation of new instances?
    """

    current_total_instances: typing.Optional[int] = pydantic.Field(default=None)
    """
    How many total instances of this resource are already in use? This is independent of any filter conditions applied to the query. Value may be larger than max_instances. As a special case, -1 is returned when access is unlimited.
    """

    max_instances: int = pydantic.Field()
    """
    How many total instances of this resource are allowed? This is independent of any filter conditions applied to the query. As a special case, -1 indicates unlimited.
    """

    may_create: bool = pydantic.Field()
    """
    May the user create additional instances of this resource?
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
