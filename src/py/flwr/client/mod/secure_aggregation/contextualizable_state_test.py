# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
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
# ==============================================================================
"""Tests for the contextualizable state."""


from dataclasses import dataclass, field
from typing import Dict, List

import numpy as np

from flwr.common.typing import NDArray, NDArrayFloat, NDArrayInt

from .contextualizable_state import ContextualizableState


def test_state_with_common_types() -> None:
    """Test the state with common types supported in ConfigsRecord."""

    # Prepare
    @dataclass
    class TestState(ContextualizableState):  # pylint: disable=R0902
        """."""

        int_: int = 123
        float_: float = 9.2435
        str_: str = "some text"
        bytes_: bytes = b"some bytes @#$%^&*"
        bool_: bool = True

        empty_list: List[int] = field(default_factory=list)
        int_list: List[int] = field(default_factory=lambda: [1, 2, 3, 4, 5])
        float_list: List[float] = field(default_factory=lambda: [0.12, 1.0, 321.5])
        str_list: List[str] = field(default_factory=lambda: ["fsdag"])
        bytes_list: List[bytes] = field(default_factory=lambda: [b"a", b"b", b"c"])
        bool_list: List[bool] = field(default_factory=lambda: [True, False])

    state = TestState()

    # Execute
    recon_state = TestState.from_configsrecord(state.to_configsrecord())

    # Assert
    assert recon_state == state


def test_state_with_ndarray() -> None:
    """Test the state with ndarray."""

    # Prepare
    @dataclass
    class TestState(ContextualizableState):
        """."""

        arr: NDArray = field(default_factory=lambda: np.array(["sfd", "1"]))
        int_arr: NDArrayInt = field(default_factory=lambda: np.arange(10))
        float_arr: NDArrayFloat = field(
            default_factory=lambda: np.arange(3).astype(float)
        )

        empty_list: List[NDArray] = field(default_factory=list)
        int_arr_list: List[NDArrayInt] = field(
            default_factory=lambda: [np.arange(3), np.arange(9)]
        )

    state = TestState()

    # Execute
    recon_state = TestState.from_configsrecord(state.to_configsrecord())

    # Assert
    assert all(recon_state.arr == state.arr)
    assert all(recon_state.int_arr == state.int_arr)
    assert all(recon_state.float_arr == state.float_arr)
    assert recon_state.empty_list == state.empty_list
    assert all(
        all(arr1 == arr2)
        for arr1, arr2 in zip(recon_state.int_arr_list, state.int_arr_list)
    )


def test_state_with_dict() -> None:
    """Test the state with dictionaries."""

    # Prepare
    @dataclass
    class TestState(ContextualizableState):
        """."""

        d1: Dict[int, bytes] = field(default_factory=lambda: {-2: b"!~0241", 99: b""})
        d2: Dict[str, NDArray] = field(default_factory=lambda: {"a1": np.arange(5)})

    state = TestState()

    # Execute
    recon_state = TestState.from_configsrecord(state.to_configsrecord())

    # Assert
    assert recon_state.d1 == state.d1
    assert list(recon_state.d2.keys()) == list(recon_state.d2.keys())
    assert all(
        all(v1 == v2) for v1, v2 in zip(recon_state.d2.values(), state.d2.values())
    )
