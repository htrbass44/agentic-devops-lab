from collections.abc import Callable

import pytest

from app.calc import add, divide, multiply, power, sqrt, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 5), (0, 0, 0), (-2, -3, -5), (10**100, 10**100, 2 * 10**100)],
)
def test_add(a: float, b: float, expected: float) -> None:
    """足し算の結果を確認する。"""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(5, 3, 2), (0, 0, 0), (-2, -3, 1), (10**100, -(10**100), 2 * 10**100)],
)
def test_subtract(a: float, b: float, expected: float) -> None:
    """引き算の結果を確認する。"""
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2.5, 4.0, 10.0),
        (-2.0, 3.0, -6.0),
        (0.0, 3.0, 0.0),
        (0, 0, 0),
        (-2, -3, 6),
        (10**100, 10**100, 10**200),
    ],
)
def test_multiply(a: float, b: float, expected: float) -> None:
    """掛け算の結果を確認する。"""
    assert multiply(a, b) == expected


def test_multiply_invalid_operand() -> None:
    """数値以外の被乗数では型エラーになる。"""
    with pytest.raises(TypeError):
        multiply(None, 2.0)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (5.0, 2.0, 2.5),
        (-6.0, 3.0, -2.0),
        (0.0, 3.0, 0.0),
        (-6.0, -3.0, 2.0),
        (6.0, -3.0, -2.0),
        (1e100, 2.0, 5e99),
        (1.0, 1e-100, 1e100),
    ],
)
def test_divide(a: float, b: float, expected: float) -> None:
    """割り算の結果を確認する。"""
    assert divide(a, b) == expected


@pytest.mark.parametrize("divisor", [0.0, -0.0])
def test_divide_by_zero(divisor: float) -> None:
    """ゼロ除算では指定された例外を送出する。"""
    with pytest.raises(ValueError, match="^division by zero$"):
        divide(1.0, divisor)


@pytest.mark.parametrize(
    ("base", "exp", "expected"),
    [
        (2.0, 3, 8.0),
        (-2.0, 3, -8.0),
        (2.0, 0, 1.0),
        (2.0, -2, 0.25),
        (-2.0, 2, 4.0),
        (-2.0, -3, -0.125),
        (0.0, 0, 1.0),
        (0.0, 3, 0.0),
        (10**100, 2, 10**200),
    ],
)
def test_power(base: float, exp: int, expected: float) -> None:
    """べき乗の結果を確認する。"""
    assert power(base, exp) == expected


@pytest.mark.parametrize(
    ("operation", "a", "b", "expected"),
    [
        (add, 0.1, 0.2, 0.3),
        (subtract, 0.3, 0.1, 0.2),
        (multiply, 0.1, 0.2, 0.02),
        (divide, 0.3, 0.1, 3.0),
        (power, 1.1, 3, 1.331),
    ],
)
def test_decimal_rounding(
    operation: Callable[..., float], a: float, b: float | int, expected: float
) -> None:
    """小数の演算結果を丸め誤差を考慮して確認する。"""
    assert operation(a, b) == pytest.approx(expected)


def test_power_invalid_exponent() -> None:
    """整数でない指数では型エラーになる。"""
    with pytest.raises(TypeError):
        power(2.0, None)


def test_power_zero_to_negative_exponent() -> None:
    """ゼロの負のべき乗ではゼロ除算エラーになる。"""
    with pytest.raises(ZeroDivisionError):
        power(0.0, -1)


@pytest.mark.parametrize(
    ("value", "expected"),
    [(9.0, 3.0), (0.0, 0.0), (2.25, 1.5)],
)
def test_sqrt(value: float, expected: float) -> None:
    """平方根の結果を確認する。"""
    assert sqrt(value) == expected


def test_sqrt_negative_value() -> None:
    """負数の平方根では値エラーになる。"""
    with pytest.raises(ValueError):
        sqrt(-1.0)
