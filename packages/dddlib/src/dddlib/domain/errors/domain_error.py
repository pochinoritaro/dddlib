"""ドメイン層の基底例外を提供するモジュール。"""

from dddlib.common.errors.ddd_error import DDDError


class DomainError(DDDError):
    """ドメイン層の基底例外"""
