"""識別子を表す値オブジェクトの抽象基底クラスを定義するモジュール。"""

from abc import ABC, abstractmethod
from typing import Any, ClassVar, Self, cast

from dddlib.domain.value_object import ValueObject


class IdentifierBase[T](ValueObject[T], ABC):
    """識別子を表す値オブジェクトの抽象基底クラス。

    このクラスは、任意の型の値を保持する識別子の共通インターフェースを
    提供します。

    サブクラスでは、`value_type` に保持する値の実行時型を定義し、
    必要に応じて新規生成や既存値からの復元処理をクラスメソッドとして
    実装することを想定しています。
    """

    value_type: ClassVar[type[Any]]
    value: T

    def validate(self) -> T:
        """保持する値の型を検証して返す。

        Returns:
            検証済みの値。

        Raises:
            TypeError: value の型が `value_type` と一致しない場合。

        """
        if not isinstance(self.value, self.value_type):
            msg = f"value には {self.value_type.__name__} を指定してください。"
            raise TypeError(msg)
        return cast("T", self.value)

    @classmethod
    def new(cls) -> Self:
        """新しい識別子を生成する。

        Returns:
            新しい値を持つ識別子インスタンス。

        Raises:
            NotImplementedError: サブクラスで未実装の場合。

        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_value(cls, value: T) -> Self:
        """既存の値から識別子を生成する。

        Args:
            value: 識別子として利用する値。

        Returns:
            指定した値を持つ識別子インスタンス。

        Raises:
            NotImplementedError: サブクラスで未実装の場合。

        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_string(cls, value: str) -> Self:
        """文字列から識別子を生成する。

        Args:
            value: 識別子の文字列表現。

        Returns:
            指定した文字列から生成された識別子インスタンス。

        Raises:
            NotImplementedError: サブクラスで未実装の場合。

        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_hex(cls, value: str) -> Self:
        """16 進文字列から識別子を生成する。

        Args:
            value: 識別子の 16 進表現を表す文字列。

        Returns:
            指定した 16 進文字列から生成された識別子インスタンス。

        Raises:
            NotImplementedError: サブクラスで未実装の場合。

        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_int(cls, value: int) -> Self:
        """整数値から識別子を生成する。

        Args:
            value: 識別子を表す整数値。

        Returns:
            指定した整数値から生成された識別子インスタンス。

        Raises:
            NotImplementedError: サブクラスで未実装の場合。

        """
        raise NotImplementedError
