# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.url import URL

__all__ = ["ToolRuntimeListToolsParams"]


class ToolRuntimeListToolsParams(TypedDict, total=False):
    mcp_endpoint: URL

    tool_group_id: str

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]
