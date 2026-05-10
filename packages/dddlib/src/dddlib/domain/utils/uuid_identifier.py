"""UUID ベースの識別子を表す値オブジェクトを定義するモジュール。"""

from typing import ClassVar, Self
from uuid import UUID, uuid4

from dddlib.domain.base.id_base import IdentifierBase


class UUIDIdentifier(IdentifierBase[UUID]):
    """UUID ベースの識別子を表す値オブジェクト基底クラス。"""

    value_type: ClassVar[type[UUID]] = UUID

    @classmethod
    def new(cls) -> Self:
        """新しい識別子を生成する。

        Returns:
            新しい UUID を持つ識別子インスタンス。

        """
        return cls(value=uuid4())

    @classmethod
    def from_value(cls, value: UUID) -> Self:
        """既存の UUID から識別子を生成する。

        Args:
            value: 識別子として利用する UUID。

        Returns:
            指定した UUID を持つ識別子インスタンス。

        """
        return cls(value=value)

    @classmethod
    def from_string(cls, value: str) -> Self:
        """UUID 文字列から識別子を生成する。

        Args:
            value: UUID 形式の文字列。

        Returns:
            指定した文字列から生成された識別子インスタンス。

        Raises:
            ValueError: UUID 形式の文字列ではない場合。

        """
        return cls(value=UUID(value))

    @classmethod
    def from_hex(cls, value: str) -> Self:
        """16 進文字列から識別子を生成する。

        Args:
            value: UUID の 16 進表現を表す文字列。

        Returns:
            指定した 16 進文字列から生成された識別子インスタンス。

        Raises:
            ValueError: UUID の 16 進表現として不正な場合。

        """
        return cls(value=UUID(hex=value))

    @classmethod
    def from_int(cls, value: int) -> Self:
        """整数値から識別子を生成する。

        Args:
            value: UUID を表す 128 ビット整数。

        Returns:
            指定した整数値から生成された識別子インスタンス。

        Raises:
            ValueError: UUID として扱えない整数値の場合。

        """
        return cls(value=UUID(int=value))
