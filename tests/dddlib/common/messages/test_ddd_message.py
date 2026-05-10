"""DDDMessage のテスト。"""

import pytest
from dddlib.common.messages.ddd_message import DDDMessage


class TestMessage(DDDMessage):
    """DDDMessage のテスト用メッセージ。"""

    REQUIRED = ("E001", "{field_name} は必須です。")
    INVALID = ("E002", "{field_name} が不正です。")
    PLAIN = ("E999", "固定メッセージ")


@pytest.mark.v1_0_0
def test_code_property_returns_code() -> None:
    """code プロパティがメッセージコードを返すことを確認する。"""
    assert TestMessage.REQUIRED.code == "E001"


@pytest.mark.v1_0_0
def test_message_property_returns_message_template() -> None:
    """message プロパティがメッセージテンプレートを返すことを確認する。"""
    assert TestMessage.REQUIRED.template == "{field_name} は必須です。"


@pytest.mark.v1_0_0
def test_format_with_kwargs_returns_formatted_message() -> None:
    """名前付き引数でメッセージを整形できることを確認する。"""
    actual = TestMessage.REQUIRED.format(field_name="name")

    assert actual.template == "name は必須です。"


@pytest.mark.v1_0_0
def test_format_with_missing_kwargs_raises_value_error() -> None:
    """必要な名前付き引数が不足した場合にValueErrorを送出することを確認する。"""
    with pytest.raises(
        ValueError,
        match=r"Message Generate failed",
    ):
        TestMessage.REQUIRED.format()


@pytest.mark.v1_0_0
def test_format() -> None:
    """名前付き引数でメッセージを整形できることを確認する。"""
    actual_1 = TestMessage.REQUIRED.format(field_name="key")
    actual_2 = TestMessage.PLAIN

    assert type(actual_1) is type(actual_2)
