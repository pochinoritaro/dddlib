"""ValueObject のテスト。"""

import pytest
from dddlib.domain.value_object import ValueObject


class SampleValueObject(ValueObject):
    """ValueObject を検証するためのテスト用値オブジェクト。"""

    value: int

    def validate(self) -> None:
        """_summary_

        Returns:
            _type_: _description_

        """


class HTTPStatusCode(ValueObject):
    """スネークケース変換を検証するためのテスト用値オブジェクト。"""

    value: int

    def validate(self) -> None:
        """_summary_

        Returns:
            _type_: _description_

        """


@pytest.mark.v1_0_0
@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("SampleValueObject", "sample_value_object"),
        ("HTTPStatusCode", "h_t_t_p_status_code"),
    ],
)
def test_to_snake_case_converts_class_name_to_snake_case(
    name: str,
    expected: str,
) -> None:
    """クラス名をスネークケースへ変換できることを確認する。"""
    assert SampleValueObject._to_snake_case(name) == expected


@pytest.mark.v1_0_0
def test_to_dict_returns_snake_case_class_name_and_value() -> None:
    """to_dict がクラス名由来のキーと値を返すことを確認する。"""
    actual = SampleValueObject(value=10)

    assert actual.to_dict() == {"sample_value_object": 10}


@pytest.mark.v1_0_0
def test_get_value_returns_raw_value() -> None:
    """get_value が保持している値をそのまま返すことを確認する。"""
    actual = SampleValueObject(value=10)

    assert actual.get_value() == 10


@pytest.mark.v1_0_0
def test_str_returns_class_name_and_field_representation() -> None:
    """__str__ がクラス名と辞書化した内容を表現することを確認する。"""
    actual = SampleValueObject(value=10)

    assert str(actual) == "SampleValueObject(sample_value_object=10)"
