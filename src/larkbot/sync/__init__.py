"""Synchronous FeishuBot implementation."""

from typing import Optional

from .bot import FeishuBot
from ..common import ResponseResult, LogLevel


_global_webhook_url: Optional[str] = None
_global_secret: Optional[str] = None


def set_url(webhook_url: str, secret: Optional[str] = None) -> None:
    """
    设置全局webhook地址和密钥

    Args:
        webhook_url: Webhook地址
        secret: 安全密钥
    """
    global _global_webhook_url, _global_secret
    _global_webhook_url = webhook_url
    _global_secret = secret


def create_bot_from_config(webhook_url: str, secret: Optional[str] = None) -> FeishuBot:
    """
    从配置创建机器人实例

    Args:
        webhook_url: Webhook地址
        secret: 安全密钥

    Returns:
        FeishuBot实例
    """
    return FeishuBot(webhook_url, secret)


def quick_log(
    level: LogLevel,
    message: str,
    webhook_url: Optional[str] = None,
    secret: Optional[str] = None
) -> ResponseResult:
    """
    快速发送日志消息（不需要创建实例）

    如果未提供webhook_url和secret，将使用set_url设置的全局值

    Args:
        level: 日志级别 (WARN, ERROR, INFO, DEBUG)
        message: 消息内容
        webhook_url: Webhook地址，如果未提供则使用全局设置
        secret: 安全密钥，如果未提供则使用全局设置

    Returns:
        发送结果

    Raises:
        ValueError: 当没有设置webhook_url时
    """
    url = webhook_url or _global_webhook_url
    sec = secret if secret is not None else _global_secret

    if not url:
        raise ValueError("webhook_url未设置，请先调用set_url()或直接传入webhook_url参数")

    with FeishuBot(url, sec) as bot:
        return bot.send_log_message(level, message)


__all__ = [
    "FeishuBot",
    "create_bot_from_config",
    "set_url",
    "quick_log",
]