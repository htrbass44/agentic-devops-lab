"""シンプルな電卓モジュール"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数を掛け合わせる。"""
    return a * b


def divide(a: float, b: float) -> float:
    """2つの数を割り、ゼロ除算の場合は例外を送出する。"""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
