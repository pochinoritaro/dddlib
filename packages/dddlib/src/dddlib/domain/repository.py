"""リポジトリの抽象基底クラスを定義するモジュール。"""

from abc import ABC, abstractmethod
from typing import Any

from dddlib.domain.base.id_base import IdentifierBase

from .aggregate_root import AggregateRoot


class Repository[
    T: AggregateRoot[IdentifierBase[Any]],
    ID: IdentifierBase[Any],
](
    ABC,
):
    """集約ルートを永続化するリポジトリの抽象基底クラス。

    このクラスは、ドメイン層から見た最小限の永続化契約だけを定義します。
    実際の保存先や検索方法は、インフラ層の実装に委ねます。
    """

    @abstractmethod
    def get(self, identifier: ID) -> T | None:
        """指定した識別子に対応する集約を取得する。

        Args:
            identifier: 取得対象の識別子。

        Returns:
            見つかった集約。存在しない場合は `None`。

        """
        raise NotImplementedError

    @abstractmethod
    def save(self, aggregate: T) -> None:
        """集約を保存する。

        Args:
            aggregate: 保存対象の集約。

        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, aggregate: T) -> None:
        """集約を削除する。

        Args:
            aggregate: 削除対象の集約。

        """
        raise NotImplementedError

    def exists(self, identifier: ID) -> bool:
        """指定した識別子に対応する集約が存在するか判定する。

        Args:
            identifier: 判定対象の識別子。

        Returns:
            存在する場合は `True`。

        """
        return self.get(identifier) is not None
