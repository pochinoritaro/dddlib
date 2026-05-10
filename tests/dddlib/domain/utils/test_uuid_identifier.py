"""UUIDIdentifier のテスト。"""

from uuid import UUID

import pytest
from dddlib.domain.utils.uuid_identifier import UUIDIdentifier


@pytest.mark.v1_0_0
def test_uuid_identifier_new_creates_uuid_value() -> None:
    """new が UUID を保持した識別子を生成することを確認する。"""
    actual = UUIDIdentifier.new()

    assert isinstance(actual.value, UUID)


@pytest.mark.v1_0_0
def test_uuid_identifier_from_value_wraps_existing_uuid() -> None:
    """from_value が既存の UUID をそのまま保持することを確認する。"""
    value = UUID("12345678-1234-5678-1234-567812345678")

    actual = UUIDIdentifier.from_value(value)

    assert actual.value == value


@pytest.mark.v1_0_0
def test_uuid_identifier_from_value_rejects_non_uuid_value() -> None:
    """from_value が UUID 以外の値を拒否することを確認する。"""
    with pytest.raises(TypeError, match="UUID"):
        UUIDIdentifier.from_value("not-a-uuid")  # type: ignore[arg-type]


@pytest.mark.v1_0_0
def test_uuid_identifier_from_string_parses_uuid_string() -> None:
    """from_string が UUID 文字列を解析できることを確認する。"""
    actual = UUIDIdentifier.from_string("12345678-1234-5678-1234-567812345678")

    assert actual.value == UUID("12345678-1234-5678-1234-567812345678")


@pytest.mark.v1_0_0
def test_uuid_identifier_from_string_raises_for_invalid_string() -> None:
    """from_string が不正な UUID 文字列で ValueError を送出することを確認する。"""
    with pytest.raises(ValueError):
        UUIDIdentifier.from_string("invalid")


@pytest.mark.v1_0_0
def test_uuid_identifier_from_hex_parses_hex_string() -> None:
    """from_hex が 16 進文字列を解析できることを確認する。"""
    actual = UUIDIdentifier.from_hex("12345678123456781234567812345678")

    assert actual.value == UUID("12345678-1234-5678-1234-567812345678")


@pytest.mark.v1_0_0
def test_uuid_identifier_from_hex_raises_for_invalid_hex() -> None:
    """from_hex が不正な 16 進文字列で ValueError を送出することを確認する。"""
    with pytest.raises(ValueError):
        UUIDIdentifier.from_hex("xyz")


@pytest.mark.v1_0_0
def test_uuid_identifier_from_int_parses_integer() -> None:
    """from_int が整数値から UUID を生成できることを確認する。"""
    value = UUID("12345678-1234-5678-1234-567812345678").int

    actual = UUIDIdentifier.from_int(value)

    assert actual.value == UUID("12345678-1234-5678-1234-567812345678")


@pytest.mark.v1_0_0
def test_uuid_identifier_from_int_raises_for_invalid_integer() -> None:
    """from_int が不正な整数値で ValueError を送出することを確認する。"""
    with pytest.raises(ValueError):
        UUIDIdentifier.from_int(-1)
