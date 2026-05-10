"""FrozenBase のテスト。"""

from dataclasses import FrozenInstanceError

import pytest
from dddlib.domain.base.frozen_base import FrozenBase


class SampleFrozenValue(FrozenBase):
    """FrozenBase を継承したテスト用クラス。"""

    value: int
    label: str


@pytest.mark.v1_0_0
def test_frozen_base_applies_dataclass_behavior() -> None:
    """継承クラスが dataclass として初期化・比較できることを確認する。"""
    actual = SampleFrozenValue(value=1, label="one")

    assert actual.value == 1
    assert actual.label == "one"
    assert actual == SampleFrozenValue(value=1, label="one")


@pytest.mark.v1_0_0
def test_frozen_base_prevents_attribute_assignment() -> None:
    """継承クラスの属性が frozen として再代入できないことを確認する。"""
    actual = SampleFrozenValue(value=1, label="one")

    with pytest.raises(FrozenInstanceError):
        actual.value = 2
