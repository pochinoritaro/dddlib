"""共通エラーの基底クラスモジュール"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dddlib.common.messages.ddd_message import Message


class DDDError(Exception):
    """Messageからコードと本文を保持する共通例外。

    Args:
        Exception: Python標準の例外基底クラス。

    """

    _code: str
    _message: str

    def __init__(
        self,
        err: Message,
    ) -> None:
        """Messageを受け取り、例外メッセージとして初期化する。

        Args:
            err: 例外情報を保持するMessage。

        """
        error_message = f"{err.code}: {err.template}"
        super().__init__(error_message)
        self._code = err.code
        self._message = err.template

    @property
    def code(self) -> str:
        """例外コードを返す。

        Returns:
            str: 例外コード。

        """
        return self._code

    @property
    def message(self) -> str:
        """例外メッセージ本文を返す。

        Returns:
            str: 例外メッセージ本文。

        """
        return self._message
