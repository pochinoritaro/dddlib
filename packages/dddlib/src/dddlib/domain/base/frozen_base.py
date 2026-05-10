"""frozen な dataclass を自動適用するメタクラスを提供する。"""

from dataclasses import dataclass, field
from typing import dataclass_transform


@dataclass_transform(
    frozen_default=True,
    kw_only_default=True,
    field_specifiers=(field,),
)
class FrozenBase:
    """サブクラスを frozen dataclass として自動変換する基底クラス。"""

    def __init_subclass__(cls, **kwargs: object) -> None:
        """サブクラス定義時に frozen dataclass を自動適用する。

        Args:
            **kwargs: クラス定義時に渡される追加引数。

        """
        super().__init_subclass__(**kwargs)
        dataclass(cls, frozen=True, kw_only=True)
