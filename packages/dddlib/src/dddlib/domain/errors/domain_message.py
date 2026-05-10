"""業務別のメッセージ定義を提供するモジュール。"""

from dddlib.common.messages import DDDMessage


class DomainMessage(DDDMessage):
    """ユーザー業務向けメッセージ定義。"""

    ENTITY_ERROR = ("DE01", "エラー")
