"""pyproject.toml から mytool の設定を読み込むモジュール。"""

from dataclasses import dataclass

from dddlib_cli.config.config_base import ConfigBase


@dataclass(frozen=True, slots=True)
class ArchitectureConfig(ConfigBase):
    """_summary_"""

    domain: str
    infrastructure: str
    application: str
    presentation: str
