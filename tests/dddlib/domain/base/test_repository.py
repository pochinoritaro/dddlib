"""Repository のテスト。"""

from typing import ClassVar, Self

import pytest
from dddlib.domain.aggregate_root import AggregateRoot
from dddlib.domain.base.id_base import IdentifierBase
from dddlib.domain.repository import Repository


class SampleIdentifier(IdentifierBase[str]):
    """Repository を検証するためのテスト用識別子。"""

    value_type: ClassVar[type[str]] = str

    @classmethod
    def new(cls) -> Self:
        """未使用の抽象メソッドを満たす。"""
        return cls(value="generated-id")

    @classmethod
    def from_value(cls, value: str) -> Self:
        """指定値から識別子を生成する。"""
        return cls(value=value)

    @classmethod
    def from_string(cls, value: str) -> Self:
        """文字列から識別子を生成する。"""
        return cls(value=value)

    @classmethod
    def from_hex(cls, value: str) -> Self:
        """16 進文字列から識別子を生成する。"""
        return cls(value=value)

    @classmethod
    def from_int(cls, value: int) -> Self:
        """整数から識別子を生成する。"""
        return cls(value=str(value))


class SampleAggregate(AggregateRoot[SampleIdentifier]):
    """Repository を検証するためのテスト用集約。"""

    name: str

    @classmethod
    def create(cls, **kwargs: object) -> Self:
        """create 経路を提供する。"""
        name = str(kwargs["name"])
        return cls._reconstruct(
            id=SampleIdentifier.from_value(f"{name}-id"),
            name=name,
        )


class DelegatingRepository(
    Repository[SampleAggregate, SampleIdentifier],
):
    """基底クラス実装を検証するためのテスト用リポジトリ。"""

    def get(self, identifier: SampleIdentifier) -> SampleAggregate | None:
        """存在確認用の最小実装。"""
        if identifier.value == "found":
            return SampleAggregate.create(name="found")
        return None

    def save(self, aggregate: SampleAggregate) -> None:
        """保存処理のダミー実装。"""
        _ = aggregate

    def remove(self, aggregate: SampleAggregate) -> None:
        """削除処理のダミー実装。"""
        _ = aggregate


class IncompleteRepository(
    Repository[SampleAggregate, SampleIdentifier],
):
    """基底クラスの抽象性を検証するための未実装リポジトリ。"""


@pytest.mark.v1_0_0
def test_repository_exists_uses_get_result() -> None:
    """exists が get の結果で判定することを確認する。"""
    repository = DelegatingRepository()

    assert repository.exists(SampleIdentifier.from_value("found")) is True
    assert repository.exists(SampleIdentifier.from_value("missing")) is False


@pytest.mark.v1_0_0
def test_repository_base_is_abstract() -> None:
    """Repository が直接生成できないことを確認する。"""
    with pytest.raises(TypeError):
        IncompleteRepository()
