from typing import Coroutine, Union

from swagger_codegen.api.adapter.base import HttpClientAdapter
from swagger_codegen.api.configuration import Configuration
from swagger_codegen.api.request import ApiRequest
from swagger_codegen.api.response import ApiResponse
from swagger_codegen.api.response_deserializer import (
    DefaultResponseDeserializer,
    ResponseDeserializer,
)


class ApiClient:
    def __init__(
        self,
        configuration: Configuration,
        adapter: HttpClientAdapter,
        deserializer: ResponseDeserializer = DefaultResponseDeserializer(),
    ):
        self._configuration = configuration
        self._adapter = adapter
        self._deserializer = deserializer

    def call_api(
        self, api_request: ApiRequest
    ) -> Union[ApiResponse, Coroutine[None, None, ApiResponse]]:
        method = api_request.clone(
            path=self._configuration.host + api_request.path,
        )
        return self._adapter.call(method)
