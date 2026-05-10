"""エンティティの基底クラスを定義するモジュール。"""

from dataclasses import field
from typing import TYPE_CHECKING, Any, Self, override

from dddlib.domain.base.frozen_base import FrozenBase
from dddlib.domain.base.id_base import IdentifierBase

if TYPE_CHECKING:
    from collections.abc import Iterable


class Entity[T: IdentifierBase[Any]](FrozenBase):
    """ID による同一性を持つエンティティの基底クラス。"""

    id: T = field(init=False)

    def __post_init__(self) -> None:
        """直接生成を防止する。

        Raises:
            TypeError: ファクトリメソッドを経由せずに生成した場合。

        """
        if not hasattr(self, "_from_factory"):
            message = (
                f"{self.__class__.__name__} は直接初期化できません。"
                "`create()` などのファクトリメソッドを使用してください。"
            )
            raise TypeError(message)

    @classmethod
    def create(
        cls: type[Self],
        *args: object,
        **kwargs: object,
    ) -> Self:
        """エンティティ生成用のファクトリメソッド。

        Args:
            *args: 各エンティティ固有の位置引数。
            **kwargs: 各エンティティ固有の名前付き引数。

        Returns:
            生成されたエンティティ。

        Raises:
            NotImplementedError: 派生クラスで未実装の場合。

        """
        raise NotImplementedError

    @classmethod
    def _reconstruct(cls, **kwargs: object) -> Self:
        """既存状態からエンティティを再構築する。

        Args:
            **kwargs: 再構築する属性。`id` を含めること。

        Returns:
            再構築されたエンティティ。

        Raises:
            KeyError: `id` が含まれていない場合。

        """
        kwargs["_from_factory"] = True
        identifier = kwargs.pop("id")

        obj = cls.__new__(cls)
        object.__setattr__(obj, "id", identifier)
        for key, value in kwargs.items():
            object.__setattr__(obj, key, value)
        return obj

    @staticmethod
    def contains_entity(
        entities: Iterable[Entity[T]],
        entity: Entity[T],
    ) -> bool:
        """同じ ID を持つエンティティが存在するか判定する。

        Args:
            entities: 判定対象のエンティティ集合。
            entity: 比較対象のエンティティ。

        Returns:
            同じ ID を持つエンティティが存在する場合は True。

        """
        return any(existing.id == entity.id for existing in entities)

    @override
    def __eq__(self, other: object) -> bool:
        """同じ型かつ同じIDなら等価とみなす。

        Args:
            other: 比較対象。

        Returns:
            等価であればTrue。

        """
        return (
            type(self) is type(other)
            and isinstance(other, Entity)
            and self.id == other.id
        )

    @override
    def __hash__(self) -> int:
        """ID に基づくハッシュ値を返す。

        Returns:
            ID に対応するハッシュ値。

        """
        return hash((type(self), self.id))

    @override
    def __str__(self) -> str:
        """文字列表現を返す。

        Returns:
            `ClassName(id=...)` 形式の文字列。

        """
        return f"{self.__class__.__name__}(id={self.id})"

    def get_id(self) -> T:
        """ID オブジェクトを返す。

        Returns:
            エンティティの ID。

        """
        return self.id
