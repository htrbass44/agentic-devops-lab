# シンプルな電卓ライブラリ

Python で基本的な算術演算を行うシンプルなライブラリです。実装は `app/`、pytest によるテストは `tests/` にあります。Python 3.12 を前提としています。

## 提供関数

`app.calc` モジュールから次の関数を利用できます。

| 関数 | 説明 |
| --- | --- |
| `add(a, b)` | 2つの数を足します。 |
| `subtract(a, b)` | 2つ目の数を1つ目の数から引きます。 |
| `multiply(a, b)` | 2つの数を掛けます。 |
| `divide(a, b)` | 1つ目の数を2つ目の数で割ります。`b` が `0` の場合は `ValueError` を送出します。 |
| `power(base, exp)` | `base` を整数の指数 `exp` 乗します。ゼロの負のべき乗では `ZeroDivisionError` を送出します。 |
| `sqrt(value)` | 数値の平方根を返します。負数の場合は `ValueError` を送出します。 |

### 使用例

```python
from app.calc import add, divide, multiply, power, sqrt, subtract

print(add(2, 3))        # 5
print(subtract(5, 3))   # 2
print(multiply(2, 3))   # 6
print(divide(6, 3))     # 2.0
print(power(2, -2))     # 0.25
print(sqrt(9))          # 3.0
```

## セットアップ

リポジトリのルートで開発用依存関係をインストールします（`AGENTS.md` 参照）。

```bash
pip install -r requirements-dev.txt
```

## テストと lint

テストは次のコマンドで実行します。

```bash
pytest -q
```

Lint の実行コマンド:

```bash
ruff check .
```

## `.github` 配下のファイル

| ファイル | 役割 |
| --- | --- |
| `.github/copilot-instructions.md` | Copilot 向けに、プロジェクトの構成・コーディング規約・テスト・PR のルールを指示します。 |
| `.github/agents/test-writer.agent.md` | テストの追加・改善を担当するエージェントの役割と制約を定義します。 |
| `.github/workflows/ci.yml` | push と pull request で Ruff と pytest を実行する CI ワークフローです。 |
| `.github/workflows/copilot-setup-steps.yml` | Copilot の開発環境セットアップ手順を定義し、依存関係のインストールを行います。 |
| `.github/workflows/health-check.yml` | 手動または週次で健全性チェックを実行し、失敗時に Issue を作成します。 |
