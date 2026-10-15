# Copyright 2021-2026 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Every RPC of every ``ondewo.vtsi`` service is reachable through BOTH the sync and the async client.

The expectations are DERIVED from the generated descriptors (``DESCRIPTOR.services_by_name`` of every
``ondewo/vtsi/*_pb2.py``), not listed here, so the next API release that adds an RPC fails this module until
both wrappers exist, and one that adds a service fails it until both wrapper classes exist - without anybody
having to remember to extend a list. The wrapper of ``Rpc`` is ``snake_case(Rpc)`` on the class named after the
service in ``ondewo.vtsi.client.services.<snake_case(Service)>`` and its ``async_`` twin, and it must call
``self.stub.Rpc``. An async wrapper of a STREAMING RPC must not be a coroutine function: grpc.aio returns an async
iterator for it, and ``await``-ing that fails at runtime, which ``make build``'s generated async copies get wrong.
"""

import importlib
import inspect
import pkgutil
import re
from types import ModuleType
from typing import (
    Any,
    List,
    Set,
    Tuple,
)

import pytest

import ondewo.vtsi

# (service name, rpc method descriptor)
Case = Tuple[str, Any]

# RPCs whose wrapper is knowingly missing or wrong. Strict xfail: whoever fixes one must delete its entry here, and
# no NEW gap can hide behind this set. Empty since 9.2.0, which fixed the caller/listener wrapper names and added
# the scheduled-caller wrappers this test found missing when it was written.
KNOWN_GAPS: Set[str] = set()


def _snake_case(name: str) -> str:
    """
    Convert a proto name to the wrapper naming convention.

    Args:
        name (str):
            A CamelCase proto service or RPC name, e.g. ``ListVtsiEventSubscriptions``.

    Returns:
        str:
            ``list_vtsi_event_subscriptions``.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _vtsi_pb2_modules() -> List[ModuleType]:
    """
    Import every generated ``ondewo.vtsi.*_pb2`` module.

    Returns:
        List[ModuleType]:
            The modules, sorted by name.
    """
    names: List[str] = sorted(
        info.name for info in pkgutil.iter_modules(ondewo.vtsi.__path__) if info.name.endswith("_pb2")
    )
    assert names, "no generated ondewo.vtsi *_pb2 module found - this test would inspect nothing"
    return [importlib.import_module(f"ondewo.vtsi.{name}") for name in names]


SERVICES: List[Tuple[str, Any]] = [
    (name, service) for module in _vtsi_pb2_modules() for name, service in module.DESCRIPTOR.services_by_name.items()
]
CASES: List[Any] = [
    pytest.param(
        (name, method),
        id=f"{name}.{method.name}",
        marks=[pytest.mark.xfail(strict=True, reason="known gap, see KNOWN_GAPS")]
        if f"{name}.{method.name}" in KNOWN_GAPS
        else [],
    )
    for name, service in SERVICES
    for method in service.methods
]


def _wrapper_class(service_name: str, asynchronous: bool) -> Any:
    """
    Return the hand-written wrapper class of a service.

    Args:
        service_name (str):
            The proto service name, e.g. ``Calls``.
        asynchronous (bool):
            Whether to return the ``async_`` twin.

    Returns:
        Any:
            The class.
    """
    prefix: str = "async_" if asynchronous else ""
    module: ModuleType = importlib.import_module(f"ondewo.vtsi.client.services.{prefix}{_snake_case(service_name)}")
    wrapper: Any = getattr(module, service_name, None)
    assert wrapper is not None, f"{module.__name__} defines no class {service_name}"
    return wrapper


def test_the_descriptors_carry_the_services_this_test_derives_from() -> None:
    """Guard against a vacuous pass: the derived case list is not empty and names the known services."""
    names: List[str] = [name for name, _ in SERVICES]
    for must_contain in ("Calls", "Projects"):
        assert must_contain in names
    assert len(CASES) > len(SERVICES)
    rpcs: Set[str] = {f"{name}.{method.name}" for name, service in SERVICES for method in service.methods}
    assert KNOWN_GAPS <= rpcs, f"KNOWN_GAPS names RPCs that no longer exist: {sorted(KNOWN_GAPS - rpcs)}"


@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("case", CASES)
def test_every_rpc_has_a_wrapper_that_calls_its_stub(case: Case, asynchronous: bool) -> None:
    """The service's wrapper class has ``snake_case(Rpc)``, which calls ``self.stub.<Rpc>``."""
    service_name, method = case
    wrapper: Any = _wrapper_class(service_name, asynchronous)
    function: Any = getattr(wrapper, _snake_case(method.name), None)
    assert function is not None, f"{wrapper.__module__}.{service_name} has no {_snake_case(method.name)}()"
    assert f"self.stub.{method.name}(" in inspect.getsource(function)
    streaming: bool = method.server_streaming or method.client_streaming
    if not asynchronous:
        assert not inspect.iscoroutinefunction(function)
    else:
        assert inspect.iscoroutinefunction(function) is not streaming, (
            f"async {service_name}.{_snake_case(method.name)} must "
            + ("return the stream, not await it" if streaming else "be a coroutine function")
        )
