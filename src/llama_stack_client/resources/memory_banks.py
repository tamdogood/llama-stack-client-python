# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ..types import memory_bank_register_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.memory_bank_list_response import MemoryBankListResponse
from ..types.memory_bank_register_response import MemoryBankRegisterResponse
from ..types.memory_bank_retrieve_response import MemoryBankRetrieveResponse

__all__ = ["MemoryBanksResource", "AsyncMemoryBanksResource"]


class MemoryBanksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemoryBanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return MemoryBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryBanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return MemoryBanksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        memory_bank_id: str,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemoryBankRetrieveResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_bank_id:
            raise ValueError(f"Expected a non-empty value for `memory_bank_id` but received {memory_bank_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            Optional[MemoryBankRetrieveResponse],
            self._get(
                f"/v1/memory-banks/{memory_bank_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryBankRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryBankListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/memory-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[MemoryBankListResponse]._unwrapper,
            ),
            cast_to=cast(Type[MemoryBankListResponse], DataWrapper[MemoryBankListResponse]),
        )

    def register(
        self,
        *,
        memory_bank_id: str,
        params: memory_bank_register_params.Params,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_memory_bank_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryBankRegisterResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            MemoryBankRegisterResponse,
            self._post(
                "/v1/memory-banks",
                body=maybe_transform(
                    {
                        "memory_bank_id": memory_bank_id,
                        "params": params,
                        "provider_id": provider_id,
                        "provider_memory_bank_id": provider_memory_bank_id,
                    },
                    memory_bank_register_params.MemoryBankRegisterParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryBankRegisterResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def unregister(
        self,
        memory_bank_id: str,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_bank_id:
            raise ValueError(f"Expected a non-empty value for `memory_bank_id` but received {memory_bank_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/v1/memory-banks/{memory_bank_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMemoryBanksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoryBanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryBanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncMemoryBanksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        memory_bank_id: str,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemoryBankRetrieveResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_bank_id:
            raise ValueError(f"Expected a non-empty value for `memory_bank_id` but received {memory_bank_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            Optional[MemoryBankRetrieveResponse],
            await self._get(
                f"/v1/memory-banks/{memory_bank_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryBankRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryBankListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/memory-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[MemoryBankListResponse]._unwrapper,
            ),
            cast_to=cast(Type[MemoryBankListResponse], DataWrapper[MemoryBankListResponse]),
        )

    async def register(
        self,
        *,
        memory_bank_id: str,
        params: memory_bank_register_params.Params,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_memory_bank_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryBankRegisterResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            MemoryBankRegisterResponse,
            await self._post(
                "/v1/memory-banks",
                body=await async_maybe_transform(
                    {
                        "memory_bank_id": memory_bank_id,
                        "params": params,
                        "provider_id": provider_id,
                        "provider_memory_bank_id": provider_memory_bank_id,
                    },
                    memory_bank_register_params.MemoryBankRegisterParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryBankRegisterResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def unregister(
        self,
        memory_bank_id: str,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_bank_id:
            raise ValueError(f"Expected a non-empty value for `memory_bank_id` but received {memory_bank_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/v1/memory-banks/{memory_bank_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MemoryBanksResourceWithRawResponse:
    def __init__(self, memory_banks: MemoryBanksResource) -> None:
        self._memory_banks = memory_banks

        self.retrieve = to_raw_response_wrapper(
            memory_banks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            memory_banks.list,
        )
        self.register = to_raw_response_wrapper(
            memory_banks.register,
        )
        self.unregister = to_raw_response_wrapper(
            memory_banks.unregister,
        )


class AsyncMemoryBanksResourceWithRawResponse:
    def __init__(self, memory_banks: AsyncMemoryBanksResource) -> None:
        self._memory_banks = memory_banks

        self.retrieve = async_to_raw_response_wrapper(
            memory_banks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            memory_banks.list,
        )
        self.register = async_to_raw_response_wrapper(
            memory_banks.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            memory_banks.unregister,
        )


class MemoryBanksResourceWithStreamingResponse:
    def __init__(self, memory_banks: MemoryBanksResource) -> None:
        self._memory_banks = memory_banks

        self.retrieve = to_streamed_response_wrapper(
            memory_banks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            memory_banks.list,
        )
        self.register = to_streamed_response_wrapper(
            memory_banks.register,
        )
        self.unregister = to_streamed_response_wrapper(
            memory_banks.unregister,
        )


class AsyncMemoryBanksResourceWithStreamingResponse:
    def __init__(self, memory_banks: AsyncMemoryBanksResource) -> None:
        self._memory_banks = memory_banks

        self.retrieve = async_to_streamed_response_wrapper(
            memory_banks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            memory_banks.list,
        )
        self.register = async_to_streamed_response_wrapper(
            memory_banks.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            memory_banks.unregister,
        )
