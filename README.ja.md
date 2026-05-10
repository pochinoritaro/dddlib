# dddlib

`dddlib` は、DDD の実装でよく使う基礎要素をまとめた Python ライブラリです。

このリポジトリは workspace 構成になっており、ライブラリ本体と CLI は別パッケージとして管理しています。

[English README](README.md)

## パッケージ

- [dddlib](packages/dddlib/README.ja.md): ドメインモデルの基底クラス、値オブジェクト、エンティティ、集約ルート、ドメインイベント、エラー、メッセージなどの基盤を提供します。
- [dddlib_cli](packages/dddlib_cli/README.ja.md): `dddlib` を利用した CLI を提供します。

## まず読む場所

詳細な使い方は各パッケージ README に委譲しています。

- ライブラリの導入と基本的な使い方は [dddlib](packages/dddlib/README.ja.md)
- CLI の起動方法とコマンド一覧は [dddlib_cli](packages/dddlib_cli/README.ja.md)

## ライセンス

このプロジェクトは [LICENSE.md](LICENSE.md) を参照してください。
