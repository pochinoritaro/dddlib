"""Entity のテスト。"""

from typing import ClassVar, Self

import pytest
from dddlib.domain.base.id_base import IdentifierBase
from dddlib.domain.entity import Entity


class SampleIdentifier(IdentifierBase[str]):
    """Entity を検証するためのテスト用識別子。"""

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


class SampleEntity(Entity[str]):
    """Entity を検証するためのテスト用エンティティ。"""

    name: str

    @classmethod
    def create(cls, **kwargs: object) -> Self:
        """create 経由の生成経路を提供する。"""
        name = str(kwargs["name"])
        return cls._reconstruct(
            id=SampleIdentifier.from_value(f"{name}-id"),
            name=name,
        )


class DelegatingEntity(Entity[str]):
    """基底クラス実装を検証するためのテスト用エンティティ。"""

    name: str

    @classmethod
    def create(cls, **kwargs: object) -> Self:
        """基底クラスの抽象ファクトリ実装へ委譲する。"""
        return super().create(**kwargs)


@pytest.mark.v1_0_0
def test_entity_direct_instantiation_requires_factory() -> None:
    """直接生成では create 経路の制約により TypeError になることを確認する。"""
    with pytest.raises(TypeError, match="create"):
        SampleEntity(name="sample")


@pytest.mark.v1_0_0
def test_entity_post_init_allows_instantiation_when_factory_flag_exists() -> (
    None
):
    """ファクトリ経路フラグがある場合は __post_init__ を通過することを確認する。"""
    SampleEntity._from_factory = True

    try:
        actual = SampleEntity(name="sample")
    finally:
        delattr(SampleEntity, "_from_factory")

    assert actual.name == "sample"


@pytest.mark.v1_0_0
def test_entity_base_create_raises_not_implemented_error() -> None:
    """基底クラスの create 実装が NotImplementedError を送出することを確認する。"""
    with pytest.raises(NotImplementedError):
        DelegatingEntity.create(name="sample")


@pytest.mark.v1_0_0
def test_entity_reconstruct_restores_id_and_fields() -> None:
    """_reconstruct が ID と属性を復元したインスタンスを返すことを確認する。"""
    identifier = SampleIdentifier.from_value("sample-id")

    actual = SampleEntity._reconstruct(id=identifier, name="sample")

    assert actual.id == identifier
    assert actual.name == "sample"


@pytest.mark.v1_0_0
def test_entity_reconstruct_raises_key_error_when_id_is_missing() -> None:
    """_reconstruct は id がない場合に KeyError を送出することを確認する。"""
    with pytest.raises(KeyError, match="id"):
        SampleEntity._reconstruct(name="sample")


@pytest.mark.v1_0_0
@pytest.mark.parametrize(
    ("target", "expected"),
    [
        (SampleEntity.create(name="sample"), True),
        (SampleEntity.create(name="other"), False),
    ],
)
def test_contains_entity_returns_membership_by_identifier(
    target: SampleEntity,
    expected: bool,
) -> None:
    """contains_entity が ID 一致で所属判定することを確認する。"""
    entity = SampleEntity.create(name="sample")
    entities = [entity]

    assert SampleEntity.contains_entity(entities, target) is expected


@pytest.mark.v1_0_0
def test_entity_base_equality_depends_on_identifier() -> None:
    """基底の __eq__ は ID 一致のみで真になることを確認する。"""
    left = SampleEntity._reconstruct(
        id=SampleIdentifier.from_value("same-id"),
        name="left",
    )
    right = SampleEntity._reconstruct(
        id=SampleIdentifier.from_value("same-id"),
        name="right",
    )
    other = SampleEntity._reconstruct(
        id=SampleIdentifier.from_value("other-id"),
        name="left",
    )

    assert Entity.__eq__(left, right) is True
    assert Entity.__eq__(left, other) is False


@pytest.mark.v1_0_0
def test_entity_base_hash_uses_identifier_hash() -> None:
    """基底の __hash__ が ID のハッシュ値を使うことを確認する。"""
    entity = SampleEntity.create(name="sample")

    assert Entity.__hash__(entity) == hash(entity.id)


@pytest.mark.v1_0_0
def test_entity_base_str_returns_class_name_and_identifier() -> None:
    """基底の __str__ がクラス名と ID を表現することを確認する。"""
    entity = SampleEntity.create(name="sample")

    assert (
        Entity.__str__(entity)
        == "SampleEntity(id=SampleIdentifier(sample_identifier='sample-id'))"
    )
