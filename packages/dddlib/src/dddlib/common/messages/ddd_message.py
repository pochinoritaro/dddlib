"""メッセージの基底クラスを定義するモジュール。"""

from dataclasses import dataclass
from enum import Enum, EnumType


@dataclass(frozen=True, slots=True)
class Message:
    """コードとテンプレートを保持するメッセージ値オブジェクト。

    Attributes:
        code: メッセージの識別コード。
        template: フォーマット前のメッセージテンプレート。

    """

    code: str
    template: str

    @property
    def message(self) -> str:
        """テンプレート文字列を返す。

        Returns:
            str: テンプレート文字列。

        """
        return self.template

    def __str__(self) -> str:
        """文字列表現

        Returns:
            str: コード+テンプレートを返す

        """
        code = f"{self.code}: " if self.code else ""
        return f"{code}{self.template}"

    def format(self, *args: object, **kwargs: object) -> Message:
        """テンプレートをフォーマットした新しいメッセージを返す。

        Args:
            *args: 文字列フォーマットに渡す位置引数。
            **kwargs: 文字列フォーマットに渡すキーワード引数。

        Returns:
            Message: フォーマット後の新しいメッセージ。

        Raises:
            ValueError: フォーマットに失敗した場合に発生する。

        """
        try:
            return Message(self.code, self.template.format(*args, **kwargs))
        except (IndexError, KeyError, ValueError) as exc:
            msg = f"Message Generate failed: code={self.code}, template={self.template!r}"  # noqa: E501
            raise ValueError(msg) from exc


class MessageABC(EnumType):
    """Enumメンバーへのアクセス時にMessageを返すメタクラス。

    Args:
        EnumType: Enumのメタクラス。

    """

    def __getattribute__(cls, name: str) -> Message:
        """EnumメンバーをMessageとして返す。

        Args:
            name: 属性名。

        Returns:
            Message: Enumメンバーから生成したMessage。内部属性はそのまま返す。

        """
        if name.startswith("_"):
            return super().__getattribute__(name)

        attr = super().__getattribute__(name)
        if isinstance(attr, cls):
            return Message(code=attr.code, template=attr.template)

        return attr


class DDDMessage(Enum, metaclass=MessageABC):
    """業務別メッセージ定義の基底Enum。

    Args:
        Enum: Enumの基底クラス。
        metaclass: Messageを返すためのメタクラス。

    """

    def __init__(self, code: str, template: str) -> None:
        """Enum定義のコードとテンプレートを保持する。

        Args:
            code: メッセージコード。
            template: メッセージテンプレート。

        """
        self._code = code
        self._template = template

    @property
    def code(self) -> str:
        """メッセージコードを返す。

        Returns:
            str: メッセージコード。

        """
        return self._code

    @property
    def template(self) -> str:
        """メッセージテンプレートを返す。

        Returns:
            str: メッセージテンプレート。

        """
        return self._template

    def format(self, *args: object, **kwargs: object) -> Message:
        """メッセージテンプレートをフォーマットして返す。

        Args:
            *args: 文字列フォーマットに渡す位置引数。
            **kwargs: 文字列フォーマットに渡すキーワード引数。

        Returns:
            Message: フォーマット後の新しいメッセージ。

        """
        return Message(self._code, self._template).format(*args, **kwargs)
