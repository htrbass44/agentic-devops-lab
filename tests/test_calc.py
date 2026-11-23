import pytest

from app.calc import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


@pytest.mark.parametrize(("a", "b", "expected"), [(2.5, 4.0, 10.0), (-2.0, 3.0, -6.0), (0.0, 3.0, 0.0)])
def test_multiply(a: float, b: float, expected: float) -> None:
    """掛け算の結果を確認する。"""
    assert multiply(a, b) == expected


def test_multiply_invalid_operand() -> None:
    """数値以外の被乗数では型エラーになる。"""
    with pytest.raises(TypeError):
        multiply(None, 2.0)


@pytest.mark.parametrize(("a", "b", "expected"), [(5.0, 2.0, 2.5), (-6.0, 3.0, -2.0), (0.0, 3.0, 0.0)])
def test_divide(a: float, b: float, expected: float) -> None:
    """割り算の結果を確認する。"""
    assert divide(a, b) == expected


@pytest.mark.parametrize("divisor", [0.0, -0.0])
def test_divide_by_zero(divisor: float) -> None:
    """ゼロ除算では指定された例外を送出する。"""
    with pytest.raises(ValueError, match="^division by zero$"):
        divide(1.0, divisor)
