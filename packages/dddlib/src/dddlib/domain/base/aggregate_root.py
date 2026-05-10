"""集約ルートの基底クラスを定義するモジュール。"""

from typing import TYPE_CHECKING, Any

from dddlib.domain.base.id_base import IdentifierBase
from dddlib.domain.entity import Entity

if TYPE_CHECKING:
    from collections.abc import Iterable

    from dddlib.domain.base.domain_event import DomainEvent


class AggregateRoot[T: IdentifierBase[Any]](Entity[T]):
    """ドメインイベントを蓄積できる集約ルートの基底クラス。"""

    _domain_events: list[DomainEvent]

    def __post_init__(self) -> None:
        """集約ルートを初期化する。"""
        super().__post_init__()
        object.__setattr__(self, "_domain_events", [])

    def add_domain_event(self, event: DomainEvent) -> None:
        """ドメインイベントを追加する。

        Args:
            event: 追加するドメインイベント。

        """
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        """蓄積済みのドメインイベントを取得してクリアする。

        Returns:
            蓄積されていたドメインイベントの一覧。

        """
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events

    def peek_domain_events(self) -> list[DomainEvent]:
        """蓄積済みのドメインイベントを参照する。

        Returns:
            蓄積されているドメインイベントの一覧。

        """
        return self._domain_events.copy()

    def extend_domain_events(self, events: Iterable[DomainEvent]) -> None:
        """複数のドメインイベントを追加する。

        Args:
            events: 追加するドメインイベント群。

        """
        self._domain_events.extend(events)
