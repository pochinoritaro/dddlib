"""ドメインイベントの基底クラスを定義するモジュール。"""

from dataclasses import field
from typing import TYPE_CHECKING, Any

from dddlib.domain.base.frozen_base import FrozenBase

if TYPE_CHECKING:
    from datetime import datetime

    from dddlib.domain.base.id_base import IdentifierBase


class DomainEvent(FrozenBase):
    """集約で発生した事実を表すドメインイベントの基底クラス。"""

    aggregate_id: IdentifierBase[Any] = field(init=False)
    occurred_at: datetime = field(init=False)

    @classmethod
    def _reconstruct(
        cls,
        *,
        aggregate_id: IdentifierBase[Any],
        occurred_at: datetime,
        **kwargs: object,
    ) -> DomainEvent:
        """既存状態からドメインイベントを再構築する。

        Args:
            aggregate_id: 集約の識別子。
            occurred_at: 発生日時。
            **kwargs: 派生クラス固有の属性。

        Returns:
            再構築されたドメインイベント。

        """
        obj = cls.__new__(cls)
        object.__setattr__(obj, "aggregate_id", aggregate_id)
        object.__setattr__(obj, "occurred_at", occurred_at)
        for key, value in kwargs.items():
            object.__setattr__(obj, key, value)
        return obj
