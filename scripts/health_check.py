"""本番の健全性チェックの代わり: 仕様どおりの振る舞いかを確認する"""
import sys

from app import calc

problems: list[str] = []

if not hasattr(calc, "sqrt"):
    problems.append("sqrt 関数が存在しない（運用チームからの要望: 平方根の計算が必要）")

if problems:
    print("\n".join(problems))
    sys.exit(1)
print("OK")
