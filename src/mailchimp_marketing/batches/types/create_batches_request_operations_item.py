# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_batches_request_operations_item_headers import CreateBatchesRequestOperationsItemHeaders
from .create_batches_request_operations_item_method import CreateBatchesRequestOperationsItemMethod
from .create_batches_request_operations_item_params import CreateBatchesRequestOperationsItemParams


class CreateBatchesRequestOperationsItem(UniversalBaseModel):
    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string containing the JSON body to use with the request.
    """

    headers: typing.Optional[CreateBatchesRequestOperationsItemHeaders] = pydantic.Field(default=None)
    """
    Any HTTP headers to include with the request.
    """

    method: CreateBatchesRequestOperationsItemMethod = pydantic.Field()
    """
    The HTTP method to use for the operation.
    """

    operation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional client-supplied id returned with the operation results.
    """

    params: typing.Optional[CreateBatchesRequestOperationsItemParams] = pydantic.Field(default=None)
    """
    Any request query parameters. Example parameters: {"count":10, "offset":0}
    """

    path: str = pydantic.Field()
    """
    The relative path to use for the operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
