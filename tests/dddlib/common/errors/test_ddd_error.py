"""DDDError のテスト。"""

from dataclasses import dataclass

import pytest
from dddlib.common.errors.ddd_error import DDDError
from dddlib.common.messages.ddd_message import Message


@dataclass(frozen=True)
class DummyDDDMessage(Message):
    """DDDMessage の簡易代替オブジェクト。"""

    code: str
    template: str


@pytest.mark.v1_0_0
def test_ddd_error_sets_code_and_message() -> None:
    """プロパティが元メッセージの値を返すことを確認する。"""
    err = DummyDDDMessage(code="E001", template="input is invalid")

    actual = DDDError(err)

    assert actual.code == "E001"
    assert actual.message == "input is invalid"


@pytest.mark.v1_0_0
def test_ddd_error_formats_exception_message() -> None:
    """例外文字列が `code: message` 形式になることを確認する。"""
    err = DummyDDDMessage(code="E001", template="input is invalid")

    actual = DDDError(err)

    assert str(actual) == "E001: input is invalid"


@pytest.mark.v1_0_0
def test_ddd_error_is_exception() -> None:
    """DDDError が例外として送出および捕捉できることを確認する。"""
    err = DummyDDDMessage(code="E001", template="input is invalid")

    with pytest.raises(DDDError, match=r"^E001: input is invalid$"):
        raise DDDError(err)
