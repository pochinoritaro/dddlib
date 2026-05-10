"""IdentifierBase のテスト。"""

from typing import ClassVar, Self

import pytest
from dddlib.domain.base.id_base import IdentifierBase


class SampleIdentifier(IdentifierBase[str]):
    """IdentifierBase を検証するためのテスト用識別子。"""

    value_type: ClassVar[type[str]] = str

    @classmethod
    def new(cls) -> Self:
        """基底クラスの未実装例外を確認するために委譲する。"""
        return super().new()

    @classmethod
    def from_value(cls, value: str) -> Self:
        """基底クラスの未実装例外を確認するために委譲する。"""
        return super().from_value(value)

    @classmethod
    def from_string(cls, value: str) -> Self:
        """基底クラスの未実装例外を確認するために委譲する。"""
        return super().from_string(value)

    @classmethod
    def from_hex(cls, value: str) -> Self:
        """基底クラスの未実装例外を確認するために委譲する。"""
        return super().from_hex(value)

    @classmethod
    def from_int(cls, value: int) -> Self:
        """基底クラスの未実装例外を確認するために委譲する。"""
        return super().from_int(value)


@pytest.mark.v1_0_0
def test_identifier_base_accepts_value_of_declared_type() -> None:
    """宣言した型の値では正しくインスタンス化できることを確認する。"""
    actual = SampleIdentifier(value="sample-id")

    assert actual.value == "sample-id"


@pytest.mark.v1_0_0
def test_identifier_base_rejects_value_of_undeclared_type() -> None:
    """宣言した型以外の値では TypeError になることを確認する。"""
    with pytest.raises(TypeError, match="str"):
        SampleIdentifier(value=100)  # type: ignore[arg-type]


@pytest.mark.v1_0_0
@pytest.mark.parametrize(
    ("factory_name", "argument"),
    [
        ("new", None),
        ("from_value", "sample-id"),
        ("from_string", "sample-id"),
        ("from_hex", "abcdef"),
        ("from_int", 1),
    ],
)
def test_identifier_base_abstract_factories_raise_not_implemented_error(
    factory_name: str,
    argument: str | int | None,
) -> None:
    """抽象ファクトリの基底実装を確認する。

    NotImplementedError を送出することを確認する。
    """
    factory = getattr(SampleIdentifier, factory_name)

    if argument is None:
        with pytest.raises(NotImplementedError):
            factory()
    else:
        with pytest.raises(NotImplementedError):
            factory(argument)
