"""値オブジェクトの基底クラスを定義するモジュール。"""

import re
from abc import ABC, abstractmethod

from dddlib.domain.base.frozen_base import FrozenBase


class ValueObject[T](FrozenBase, ABC):
    """単一値を持つ値オブジェクトの基底クラス。"""

    value: T

    def __post_init__(self) -> None:
        """生成後に値を検証し、必要なら正規化した値を設定する。"""
        validated = self.validate()
        object.__setattr__(self, "value", validated)

    @abstractmethod
    def validate(self) -> T:
        """値を検証し、必要なら正規化済みの値を返す。

        Args:
            args: 位置引数
            kwargs: キーワード引数

        Returns:
            検証済みの値。

        Raises:
            ValueError: 値が不正な場合。

        """
        raise NotImplementedError

    @classmethod
    def _to_snake_case(cls, name: str) -> str:
        """クラス名をスネークケースに変換する。

        Args:
            name: 変換対象のクラス名。

        Returns:
            スネークケースへ変換した文字列。

        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    def to_dict(self) -> dict[str, T]:
        """値オブジェクトを辞書形式に変換する。

        Returns:
            クラス名のスネークケースをキー、value を値とする辞書。

        """
        key = self._to_snake_case(self.__class__.__name__)
        return {key: self.value}

    def get_value(self) -> T:
        """保持している値を返す。

        Returns:
            保持している値。

        """
        return self.value

    def __str__(self) -> str:
        """値オブジェクトの文字列表現を返す。

        Returns:
            `ClassName(field=value)` 形式の文字列。

        """
        fields_repr = ", ".join(
            f"{key}={value!r}" for key, value in self.to_dict().items()
        )
        return f"{self.__class__.__name__}({fields_repr})"
