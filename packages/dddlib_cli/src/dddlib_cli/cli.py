"""dddlib CLI のエントリポイントを定義するモジュール。"""

import typer

from dddlib_cli.commands.initialize import (
    command as init_command,
)

app = typer.Typer(help="dddlib の CLI です。")
app.add_typer(init_command, name="init")
