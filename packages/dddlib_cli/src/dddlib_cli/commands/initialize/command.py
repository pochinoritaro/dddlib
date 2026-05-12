"""`dddlib init` コマンドを提供するモジュール。"""

import typer

command = typer.Typer(help="プロジェクト初期化を行います。")


@command.callback(invoke_without_command=True)
def main() -> None:
    """`dddlib init` を実行する。"""
    typer.echo("dddlib init")
